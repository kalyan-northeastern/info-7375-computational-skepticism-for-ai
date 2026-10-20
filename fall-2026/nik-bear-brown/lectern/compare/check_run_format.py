#!/usr/bin/env python3
"""check_run_format.py: does a run folder use the one output format every form must write?

The format is what the Python writes to runs/DATE/: all-jobs-DATE.json and jobs-of-interest-DATE.json, each with a
`records` list. Without one format nothing can be compared. This checks the fields and the types, not the judgments.

  python3 compare/check_run_format.py runs/2026-10-18
  python3 compare/check_run_format.py forms/muse/runs/2026-10-21
"""
import glob, json, os, sys

ALL_FIELDS = {"source": str, "company": str, "source_id": str, "title": str, "url": (str, type(None)), "date_posted": (str, type(None)), "kept": bool}
KEPT_FIELDS = {"source": str, "company": str, "source_id": str, "title": str, "url": str, "matched": dict}


def check_file(path, fields):
    problems = []
    d = json.load(open(path, encoding="utf-8"))
    if not isinstance(d.get("records"), list):
        return [f"{os.path.basename(path)}: no 'records' list"]
    for i, r in enumerate(d["records"]):
        for k, t in fields.items():
            if k not in r:
                problems.append(f"{os.path.basename(path)} record {i}: missing '{k}'")
            elif not isinstance(r[k], t):
                problems.append(f"{os.path.basename(path)} record {i}: '{k}' is {type(r[k]).__name__}")
        if len(problems) > 20:
            problems.append("(stopping after 20)")
            break
    return problems


def check_run(folder):
    problems, seen = [], {}
    for prefix, fields in (("all-jobs-", ALL_FIELDS), ("jobs-of-interest-", KEPT_FIELDS)):
        files = sorted(glob.glob(os.path.join(folder, prefix + "*.json")))
        if not files:
            problems.append(f"no {prefix}*.json in {folder}")
            continue
        problems += check_file(files[-1], fields)
        seen[prefix] = len(json.load(open(files[-1], encoding="utf-8"))["records"])
    return problems, seen


def main(argv=None):
    folder = (argv or sys.argv[1:] or [None])[0]
    if not folder:
        print(__doc__)
        return 2
    problems, seen = check_run(folder)
    for p in problems:
        print("PROBLEM:", p)
    print(f"{folder}: {seen} records; " + ("format ok" if not problems else f"{len(problems)} problem(s)"))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
