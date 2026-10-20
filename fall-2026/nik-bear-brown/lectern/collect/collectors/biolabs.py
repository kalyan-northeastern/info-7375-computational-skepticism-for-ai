#!/usr/bin/env python3
"""biolabs.py: read public lab directory pages and score each lab page for data-heavy biology.

Adapted from the Biojobs repository's biolab_devops_cli.py (MIT licence). What was kept: the data-signal keywords, the
directory -> lab -> people crawl, the portal and fundraising deny lists, tracking-parameter stripping, and the rule that an
HTTP error page is never parsed for links. What was changed, on purpose:
  * robots.txt is read first, per host, and a disallowed page is skipped (the original never read it);
  * the User-Agent says what this is (the original sent a browser's);
  * no email is decoded, de-obfuscated or guessed: only a mailto: link the page itself publishes is recorded, and only in
    the local, untracked record;
  * no outreach email is drafted and no search for a person is built: those belong to Professor Bear;
  * the output is one lab record per page (a subset of lab-outreach/LAB-RECORD.md), not a CSV of leads.

  python3 -m collectors.biolabs --seed "Harvard Medical School labs" --max-labs 10
  python3 -m collectors.biolabs --all --min-score 2          # every seed in config/biolabs.json

Writes lab-records/biolabs-<date>.jsonl (local, gitignored: it may hold published email addresses). Prints counts only.
A record's fit is a count of words on the lab's own page, not a verdict: Professor Bear gives the verdict.
Stdlib only.
"""
import argparse, datetime as dt, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser
from html.parser import HTMLParser

for _p in (os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
    if os.path.exists(os.path.join(_p, "lectern_paths.py")):
        sys.path.insert(0, _p)
        break
import lectern_paths as lp

CFG = json.load(open(lp.config("biolabs.json"), encoding="utf-8"))
SKIP_EXT = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".zip")
MAILTO = re.compile(r'^mailto:([^?]+)', re.I)


class Page(HTMLParser):
    """Links (href, text), the meta description, the first paragraph, and visible text."""
    def __init__(self):
        super().__init__()
        self.links, self.text, self.meta, self.first_p = [], [], "", ""
        self._href, self._buf, self._skip, self._in_p, self._p = None, [], 0, False, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self._skip += 1
        elif tag == "a" and a.get("href"):
            self._href, self._buf = a["href"], []
        elif tag == "meta" and (a.get("name") or "").lower() == "description":
            self.meta = (a.get("content") or "").strip()
        elif tag == "p" and not self.first_p:
            self._in_p, self._p = True, []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._skip:
            self._skip -= 1
        elif tag == "a" and self._href is not None:
            self.links.append((self._href, " ".join("".join(self._buf).split())))
            self._href = None
        elif tag == "p" and self._in_p:
            t = " ".join("".join(self._p).split())
            if len(t) >= 60:
                self.first_p, self._in_p = t, False

    def handle_data(self, d):
        if self._skip:
            return
        self.text.append(d)
        if self._href is not None:
            self._buf.append(d)
        if self._in_p:
            self._p.append(d)


def canonical_url(u):
    p = urllib.parse.urlparse(u)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True) if k not in CFG["tracking_params"]]
    u = urllib.parse.urlunparse(p._replace(fragment="", query=urllib.parse.urlencode(q)))
    for old, new in CFG["host_rewrites"].items():
        if old in u.replace("https://", "").replace("http://", ""):
            u = u.replace(old.split("/")[0], new.split("/")[0], 1)
    return u


def in_scope(url, base_host):
    p = urllib.parse.urlparse(url)
    host = (p.hostname or "").lower()
    if p.scheme not in ("http", "https") or url.lower().endswith(SKIP_EXT):
        return False
    if any(host.startswith(x) for x in CFG["deny_host_prefixes"]) or any(x in (p.path or "") for x in CFG["deny_path_parts"]):
        return False
    reg = ".".join(base_host.split(".")[-2:])                  # stay inside the seed's own organisation (e.g. harvard.edu)
    return host == reg or host.endswith("." + reg)


def looks_like_lab(href, text):
    h, t = href.lower(), text.lower()
    if not text or len(text) < 3 or any(b in t for b in CFG["skip_anchor_words"]):
        return False
    return any(k in t or k in h for k in CFG["lab_link_words"])


def looks_like_people(href, text):
    return any(k in href.lower() or k in text.lower() for k in CFG["people_hints"])


def data_signal(text):
    low = text.lower()
    hits = sorted({k for k in CFG["data_keywords"] if re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", low)})
    return len(hits), hits


class Reader:
    """One polite fetcher: honest User-Agent, robots.txt first, a delay between requests, errors never parsed."""
    def __init__(self, delay=None, opener=None):
        self.delay, self.robots, self.last, self.open = (delay if delay is not None else CFG["delay_seconds"]), {}, 0.0, opener or urllib.request.urlopen

    def allowed(self, url):
        p = urllib.parse.urlparse(url)
        key = f"{p.scheme}://{p.netloc}"
        if key not in self.robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                req = urllib.request.Request(key + "/robots.txt", headers={"User-Agent": CFG["user_agent"]})
                with self.open(req, timeout=15) as r:
                    rp.parse(r.read().decode("utf-8", "replace").splitlines())
            except urllib.error.HTTPError as e:
                rp.parse([] if e.code in (404, 410) else ["User-agent: *", "Disallow: /"])     # no file: allowed; blocked or unreadable: not
            except Exception:
                rp.parse(["User-agent: *", "Disallow: /"])
            self.robots[key] = rp
        return self.robots[key].can_fetch(CFG["user_agent"], url)

    def get(self, url):
        """Returns (status, html). status is 'robots' if disallowed, 'error' on a failure; html only for 2xx HTML."""
        if not self.allowed(url):
            return "robots", ""
        wait = self.delay - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        self.last = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": CFG["user_agent"]})
            with self.open(req, timeout=20) as r:
                if "html" not in (r.headers.get("Content-Type", "") or "").lower():
                    return str(r.status), ""
                return str(r.status), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return str(e.code), ""                                # an error page is never parsed
        except Exception:
            return "error", ""


def harvest(reader, seed_url, max_labs):
    status, html = reader.get(seed_url)
    if not html:
        return status, []
    pg = Page(); pg.feed(html)
    base_host = (urllib.parse.urlparse(seed_url).hostname or "").lower()
    seen, out = set(), []
    for href, text in pg.links:
        if MAILTO.match(href) or href.lower().endswith(SKIP_EXT) or not looks_like_lab(href, text):
            continue
        u = canonical_url(urllib.parse.urljoin(seed_url, href))
        if u in seen or not in_scope(u, base_host):
            continue
        seen.add(u); out.append((text, u))
        if len(out) >= max_labs:
            break
    return status, out


def read_lab(reader, name, url, seed_name, with_people=True):
    status, html = reader.get(url)
    rec = {"lab_name": name, "lab_url": url, "seed": seed_name, "read_at": dt.date.today().isoformat(), "http_status": status,
           "host": urllib.parse.urlparse(url).hostname, "status": "read" if html else ("blocked_by_robots" if status == "robots" else "not_read"),
           "data_signal": 0, "matched": [], "what_the_lab_says_verbatim": None, "people_page_url": None, "published_mailto": [], "reader": "script"}
    if not html:
        return rec
    pg = Page(); pg.feed(html)
    score, hits = data_signal(" ".join(pg.text) + " " + pg.meta)    # the page text and its own meta description
    rec["data_signal"], rec["matched"] = score, hits
    desc = pg.meta or pg.first_p
    rec["what_the_lab_says_verbatim"] = desc[:300] if desc else None            # the page's own words, never a model's summary
    mails = {m.group(1).strip() for href, _ in pg.links if (m := MAILTO.match(href))}
    people = [urllib.parse.urljoin(url, h) for h, t in pg.links if not MAILTO.match(h) and looks_like_people(h, t)]
    base_host = (urllib.parse.urlparse(url).hostname or "").lower()
    people = [canonical_url(p) for p in people if in_scope(canonical_url(p), base_host)]
    if people:
        rec["people_page_url"] = people[0]
        if with_people:
            st2, h2 = reader.get(people[0])
            if h2:
                p2 = Page(); p2.feed(h2)
                mails |= {m.group(1).strip() for href, _ in p2.links if (m := MAILTO.match(href))}
    rec["published_mailto"] = sorted(mails)                                      # only what the page links; local record only
    return rec


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", help="a seed's name from config/biolabs.json")
    ap.add_argument("--all", action="store_true", help="every seed")
    ap.add_argument("--max-labs", type=int, default=25)
    ap.add_argument("--min-score", type=int, default=0, help="keep labs whose data-signal is at least this")
    ap.add_argument("--no-people", action="store_true", help="do not read people pages")
    ap.add_argument("--out", default=os.path.join(lp.ROOT, "lab-records", f"biolabs-{dt.date.today().isoformat()}.jsonl"))
    a = ap.parse_args(argv)
    seeds = [s for s in CFG["seeds"] if a.all or s["name"] == a.seed]
    if not seeds:
        print("name a seed with --seed, or use --all. Seeds: " + "; ".join(s["name"] for s in CFG["seeds"]), file=sys.stderr)
        return 2
    reader, recs = Reader(), []
    for s in seeds:
        status, labs = harvest(reader, s["url"], a.max_labs)
        print(f"seed {s['name']}: HTTP {status}, {len(labs)} candidate lab links", file=sys.stderr)
        for name, url in labs:
            r = read_lab(reader, name, url, s["name"], with_people=not a.no_people)
            if r["status"] != "read" or r["data_signal"] >= a.min_score:
                recs.append(r)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    read = [r for r in recs if r["status"] == "read"]
    print(f"{len(recs)} records ({len(read)} read, {sum(1 for r in recs if r['status']=='blocked_by_robots')} blocked by robots, "
          f"{sum(1 for r in recs if r['status']=='not_read')} not read); {sum(1 for r in read if r['data_signal']>=2)} with data-signal 2 or more; "
          f"wrote {os.path.relpath(a.out, lp.ROOT)} (local, untracked)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
