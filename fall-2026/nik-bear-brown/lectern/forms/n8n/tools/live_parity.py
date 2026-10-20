#!/usr/bin/env python3
"""Live check of the HTTP path: read a few small real boards with workflow 01 in a disposable n8n profile AND with the
Python Lectern, seconds apart, and compare the normalised postings. Uses the network (the public job-board APIs only).

  python3 tools/live_parity.py --lectern LECTERN_DIR [--boards Netlify "Jasper AI" Airtable]
"""
import argparse, copy, json, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import test_headless as t




def _default_lectern():
    """The Python Lectern, when this folder sits inside it (as in the course repository: lectern/forms/n8n/)."""
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))      # lectern/, which holds forms/n8n/
    return d if os.path.exists(os.path.join(d, "lectern_paths.py")) else None
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lectern", default=_default_lectern()); ap.add_argument("--boards", nargs="+", default=["Netlify", "Jasper AI", "Airtable"])
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp   # the Python Lectern's own map of where its files are (config/, collect/, publish/, audit/)
    import collect
    cfg = json.load(open(lp.config("sources.json"), encoding="utf-8"))
    boards = {b["company"]: (s["provider"], b["slug"]) for s in cfg["sources"] for b in s["boards"]}
    ok_all = True
    with tempfile.TemporaryDirectory(prefix="lectern-live-") as tmp:
        os.chmod(tmp, 0o700)
        wf = json.loads((t.ROOT / "01-collect" / "workflow.json").read_text())
        for n in wf["nodes"]:
            if n["name"] == "Fixture input":
                n["parameters"]["jsCode"] = "return [{json: {mode: 'live', only: %s}}];" % json.dumps(a.boards)
        run = t.Runner(tmp); run.import_all([wf], tmp)
        ex = run.execute(wf["id"])
        if t.err(ex):
            sys.exit("n8n run failed: " + t.err(ex))
        out = t.items(ex, "Normalise")[0]
        print("n8n status:", [(s["company"], s["status"], s.get("postings"), s.get("reason")) for s in out["sources"]])
        for co in a.boards:
            prov, slug = boards[co]
            py = collect.normalise(prov, co, collect.fetch_board(prov, slug))
            py = {v["source_id"]: {k: x for k, x in v.items() if k != "original"} for v in py}
            js = {v["source_id"]: v for v in out["views"] if v["company"] == co}
            same = t.canon(py) == t.canon(js)
            ok_all &= same
            print(f"  {co:10} ({prov}): python {len(py)} postings, n8n {len(js)}; identical on every field: {same}")
    print("LIVE PARITY" if ok_all else "LIVE DIFFERENCE")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
