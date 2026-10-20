#!/usr/bin/env python3
"""Parity test: the Python filter (lectern/collect.py) and the JavaScript ports in shared/lib, run over the same raw
board payloads, must agree on every posting: same text, same fields, same keep decision, same matched words.

Needs a Lectern checkout with saved raw payloads (they are not in this repository: they are full copies of
companies' job ads). Example:
  python3 tools/parity_real_data.py --lectern ../../info-7375-.../fall-2026/nik-bear-brown/lectern --raw RAWDIR
"""
import argparse, json, os, subprocess, sys, tempfile, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))

def _default_lectern():
    """The Python Lectern, when this folder sits inside it (as in the course repository: lectern/n8n/)."""
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))      # lectern/, which holds n8n/
    return d if os.path.exists(os.path.join(d, "lectern_paths.py")) else None



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectern", default=_default_lectern())
    ap.add_argument("--raw", required=True, help="a runs/<date>/raw folder")
    ap.add_argument("--keywords", help="default: <lectern>/keywords.json")
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp   # the Python Lectern's own map of where its files are (config/, collect/, publish/, audit/)
    import collect
    kwp = a.keywords or lp.config("keywords.json")
    kw = json.load(open(kwp, encoding="utf-8"))
    cfg = json.load(open(lp.config("sources.json"), encoding="utf-8"))
    spec = []
    for s in cfg["sources"]:
        for b in s["boards"]:
            pat = os.path.join(a.raw, f"{s['provider']}-{b['slug'].replace(' ', '_').lower()}-*.json")
            for f in sorted(glob.glob(pat))[-1:]:
                spec.append({"provider": s["provider"], "company": b["company"], "file": os.path.abspath(f)})
    if not spec:
        raise SystemExit(f"no raw payloads under {a.raw}")

    views = []
    for s in spec:
        views.extend(collect.normalise(s["provider"], s["company"], json.load(open(s["file"], encoding="utf-8"))))
    seen, py = set(), {}
    for v in views:
        k = (v["source"], v["source_id"])
        if k in seen:
            continue
        seen.add(k)
        reason, matched = None, None
        if not v["title"]: reason = "missing-title"
        elif not v["url"]: reason = "missing-url"
        elif not v["date_posted"]: reason = "unparseable-date"
        else:
            m, why = collect.judge(v, kw)
            matched, reason = (m, None) if m else (None, why)
        py[k] = {**{f: v[f] for f in ("title", "text", "location_text", "department", "date_posted", "job_ref", "url")},
                 "kept": bool(matched), "matched": matched, "reject_reason": reason}

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as t:
        json.dump(spec, t)
    out = subprocess.run(["node", os.path.join(HERE, "js_run.js"), kwp, t.name], capture_output=True, text=True, check=True).stdout
    os.unlink(t.name)
    js = {(r["source"], r["source_id"]): r for r in json.loads(out)["records"]}

    keys_py, keys_js = set(py), set(js)
    diffs = {}
    for k in sorted(keys_py & keys_js):
        for f in ("title", "text", "location_text", "department", "date_posted", "job_ref", "url", "kept", "reject_reason"):
            if py[k][f] != js[k][f]:
                diffs.setdefault(f, []).append(k)
        if json.loads(json.dumps(py[k]["matched"])) != js[k]["matched"]:
            diffs.setdefault("matched", []).append(k)
    print(f"boards read: {len(spec)}   postings: python {len(keys_py)}, javascript {len(keys_js)}   only-in-one: {len(keys_py ^ keys_js)}")
    print(f"kept: python {sum(r['kept'] for r in py.values())}, javascript {sum(r['kept'] for r in js.values())}")
    if not diffs and keys_py == keys_js:
        print(f"PARITY: all {len(keys_py)} postings identical on every field, keep decision and matched words")
        return 0
    for f, ks in diffs.items():
        print(f"DIFFERENT in {f}: {len(ks)} postings, e.g. {ks[:3]}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
