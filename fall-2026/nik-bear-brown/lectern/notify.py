#!/usr/bin/env python3
"""notify.py — post new listings to the public Discord channel, so they are seen without anyone asking.

Standing rule (Professor Bear, 2026-10-19): whenever a run finds new possible listings, they are posted to the
#professor-bear channel automatically. This module is that step. It builds the messages from a delta, drops
companies that are no longer on the watch list, remembers what it has already posted, and sends.

The webhook is a secret kept in the home folder (~/.discord-webhooks/professor-bear, or the older
~/.lectern-webhook). It is never printed, logged or committed. The channel is public: a message with a local path,
an email address or a webhook URL is refused.
"""
import json, os, re, sys, urllib.error, urllib.request

CHANNEL = "professor-bear"
PRIORITY = ["Anthropic", "OpenAI", "Microsoft", "Google", "Figma", "Canva", "GitHub", "Notion"]   # his most-wanted, 2026-10-18
MAX_CHUNK = 1300
FOOTER = "Every row links to the live posting. A person decides; the machine only ranks words."


def webhook_url(channel=CHANNEL):
    home = os.path.expanduser("~")
    paths = [os.path.join(home, ".discord-webhooks", channel)] + ([os.path.join(home, ".lectern-webhook")] if channel == CHANNEL else [])
    for p in paths:
        if os.path.isfile(p):
            if os.stat(p).st_mode & 0o077:
                raise SystemExit(f"refusing: {os.path.basename(p)} is readable by others; chmod 600 it")
            url = "".join(open(p).read().split())
            if re.fullmatch(r"https://(discord|discordapp)\.com/api/webhooks/\d+/[\w-]+", url):
                return url
            raise SystemExit(f"{os.path.basename(p)} does not hold a Discord webhook URL")
    raise SystemExit(f"no webhook saved for channel '{channel}'")


def matched_words(m):
    if not isinstance(m, dict):
        return ""
    words = []
    for k, v in m.items():
        if isinstance(v, dict):
            v = [w for x in v.values() if isinstance(x, list) for w in x]
        if isinstance(v, list):
            words += [w for w in v if w not in words]
    return ", ".join(words[:4])


def order(rows):
    rank = {c: i for i, c in enumerate(PRIORITY)}
    return sorted(rows, key=lambda r: (rank.get(r["company"], 99), r["company"], r.get("title") or ""))


def build_messages(new, watched, first_time=(), already=()):
    """Return (rows_to_post, [message texts]). Drops unwatched companies and rows already posted."""
    rows = [r for r in new if r["company"] in watched and f"{r['source']}:{r['source_id']}" not in already]
    rows = order(rows)
    if not rows:
        return [], []
    lines = []
    for r in rows:
        loc = (r.get("location_text") or "").split(" | ")[0].split(";")[0][:40]
        tag = " (newly watched)" if r["company"] in first_time else ""
        lines.append(f"**{r['company']}**{tag}: {(r.get('title') or '')[:100]}" + (f" · {loc}" if loc else "")
                     + (f" ({matched_words(r.get('matched'))})" if matched_words(r.get("matched")) else "")
                     + f" {r.get('url') or ''}")
    msgs, chunk, size = [], [], 0
    for ln in lines:
        if size + len(ln) > MAX_CHUNK and chunk:
            msgs.append("\n".join(chunk)); chunk, size = [], 0
        chunk.append(ln); size += len(ln) + 1
    if chunk:
        msgs.append("\n".join(chunk))
    msgs[-1] += "\n\n" + FOOTER
    return rows, msgs


def post(title, text, send):
    """One embed. Returns True if Discord accepted it."""
    if re.search(r"/[U]sers/|/home/\w+|[\w.+-]+@[\w-]+\.[\w.]+|discord(app)?\.com/api/webhooks", title + text):
        print("NOT SENT: text contains a local path, email address or webhook URL")
        return False
    if not send:
        print(f"DRY RUN, #{CHANNEL}, nothing sent: {title} ({len(text)} chars)")
        return False
    payload = {"username": "Professor Bear", "embeds": [{"title": "Jobs: " + title, "description": text, "color": 0xD97757}]}
    req = urllib.request.Request(webhook_url(), data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "lectern-notify/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"posted to #{CHANNEL}: HTTP {r.status}")
            return 200 <= r.status < 300
    except urllib.error.HTTPError as e:
        print(f"Discord refused it: HTTP {e.code}")
        return False


def post_new(new, watched, first_time, posted_path, label, send):
    """Post the new listings not yet posted; record the ones Discord accepted. Returns how many were posted."""
    already = set(json.load(open(posted_path)) if os.path.exists(posted_path) else [])
    rows, msgs = build_messages(new, watched, first_time, already)
    if not rows:
        print("Nothing new to post to Discord.")
        return 0
    title = f"{len(rows)} new possible listings ({label})"
    sent_ok = True
    for i, m in enumerate(msgs):
        sent_ok = post(title + (f" ({i + 1}/{len(msgs)})" if len(msgs) > 1 else ""), m, send) and sent_ok
    if send and sent_ok:
        already |= {f"{r['source']}:{r['source_id']}" for r in rows}
        json.dump(sorted(already), open(posted_path, "w"))
        return len(rows)
    return 0
