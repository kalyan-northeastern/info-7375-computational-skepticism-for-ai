#!/usr/bin/env python3
"""Parity test for the Discord messages: lectern/notify.py build_messages() and shared/lib/messages.js must produce the
same rows in the same order and byte-identical message text from the same new listings. Nothing is sent.

  python3 tools/parity_messages.py --lectern LECTERN_DIR --earlier RUN_DIR --later RUN_DIR
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def _default_lectern():
    """The sibling Python Lectern, when this folder sits beside it (as in the course repository)."""
    d = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "lectern")
    return d if os.path.isdir(d) else None



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectern", default=_default_lectern()); ap.add_argument("--earlier", required=True); ap.add_argument("--later", required=True)
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp   # the Python Lectern's own map of where its files are (config/, collect/, publish/, audit/)
    import publish_delta as pd, notify
    e, l = pd.load_run(a.earlier), pd.load_run(a.later)
    state = {k: {**v, "fp": pd.fingerprint(v)} for k, v in e["kept"].items()}
    new, _, _ = pd.diff(state, l)
    watched = sorted(pd.watched_companies())
    first_time = sorted({r["company"] for r in new if r["company"] not in {v["company"] for v in state.values()}})
    already = [f"{new[0]['source']}:{new[0]['source_id']}"] if new else []
    rows, msgs = notify.build_messages(new, set(watched), set(first_time), set(already))
    out = subprocess.run(["node", os.path.join(HERE, "js_messages.js")], input=json.dumps(
        {"new": new, "watched": watched, "first_time": first_time, "already": already}), capture_output=True, text=True, check=True).stdout
    js = json.loads(out)
    py_rows = [f"{r['source']}:{r['source_id']}" for r in rows]
    print(f"new {len(new)}; posted rows python {len(py_rows)}, javascript {len(js['rows'])}; messages python {len(msgs)}, javascript {len(js['messages'])}")
    ok = py_rows == js["rows"] and msgs == js["messages"]
    print("PARITY: same rows in the same order and byte-identical messages" if ok else "DIFFERENT")
    if not ok:
        for i, (x, y) in enumerate(zip(msgs, js["messages"])):
            if x != y:
                for n, (p, q) in enumerate(zip(x, y)):
                    if p != q:
                        print(f"message {i} first differs at char {n}: {x[max(0,n-40):n+40]!r} vs {y[max(0,n-40):n+40]!r}"); break
                break
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
