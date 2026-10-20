#!/usr/bin/env python3
"""Parity test for the delta: lectern/publish_delta.py and shared/lib/delta.js must put the same postings in
new, changed and gone, with the same reasons, when given the same two runs. (The hash differs by design, so a state
file is not interchangeable; the classification must be identical.)

  python3 tools/parity_delta.py --lectern LECTERN_DIR --earlier RUN_DIR --later RUN_DIR
"""
import argparse, json, os, subprocess, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))

def _default_lectern():
    """The Python Lectern, when this folder sits inside it (as in the course repository: lectern/n8n/)."""
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))      # lectern/, which holds n8n/
    return d if os.path.exists(os.path.join(d, "lectern_paths.py")) else None



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectern", default=_default_lectern())
    ap.add_argument("--earlier", required=True, help="a runs/<date> folder with jobs-of-interest and all-jobs")
    ap.add_argument("--later", required=True)
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp   # the Python Lectern's own map of where its files are (config/, collect/, publish/, audit/)
    import publish_delta as pd
    e, l = pd.load_run(a.earlier), pd.load_run(a.later)
    state = {k: {**v, "fp": pd.fingerprint(v)} for k, v in e["kept"].items()}
    new, changed, gone = pd.diff(state, l)
    py = {"new": sorted(pd.key_of(r) for r in new),
          "changed": sorted((pd.key_of(r), sorted(c["field"] for c in r["changes"])) for r in changed),
          "gone": sorted((pd.key_of(r), r["why"]) for r in gone)}

    def f(d, p):
        return sorted(glob.glob(os.path.join(d, p)))[-1]
    out = subprocess.run(["node", os.path.join(HERE, "js_delta.js"), f(a.earlier, "jobs-of-interest-*.json"), f(a.earlier, "all-jobs-*.json"),
                          f(a.later, "jobs-of-interest-*.json"), f(a.later, "all-jobs-*.json"), l["date"]],
                         capture_output=True, text=True, check=True).stdout
    j = json.loads(out)
    js = {"new": sorted(r["key"] for r in j["new"]),
          "changed": sorted((r["key"], sorted(r["fields"])) for r in j["changed"]),
          "gone": sorted((r["key"], r["why"]) for r in j["gone"])}
    py["changed"] = [(k, fs) for k, fs in py["changed"]]
    print(f"python: new {len(py['new'])}, changed {len(py['changed'])}, gone {len(py['gone'])}   javascript: new {len(js['new'])}, changed {len(js['changed'])}, gone {len(js['gone'])}")
    same = True
    for part in ("new", "changed", "gone"):
        if [list(x) if isinstance(x, tuple) else x for x in py[part]] != [list(x) if isinstance(x, tuple) else x for x in js[part]]:
            same = False
            ps, jsx = set(map(str, py[part])), set(map(str, js[part]))
            print(f"DIFFERENT in {part}: only python {len(ps - jsx)}, only javascript {len(jsx - ps)}; e.g. {sorted(ps ^ jsx)[:3]}")
    if same:
        print("PARITY: new, changed and gone are identical, including the reasons")
    return 0 if same else 1


if __name__ == "__main__":
    raise SystemExit(main())
