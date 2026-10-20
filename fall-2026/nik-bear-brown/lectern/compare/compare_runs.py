#!/usr/bin/env python3
"""compare_runs.py: how far does a form's run agree with the reference run (the Python's)?

Reads the kept decision per posting from two run folders in the standard format and reports, in plain counts: postings
both saw, postings only one saw, and where both saw a posting but disagreed on keeping it. It judges nothing: every
disagreement is a question for a person (the form may be wrong, or right where the keyword filter was wrong).
Agreement between forms is weak evidence, because they read the same boards and may share a spec; read the rejects too.

  python3 compare/compare_runs.py runs/2026-10-18 forms/muse/runs/2026-10-18 [--out report.md]
"""
import argparse, glob, json, os


def load(folder):
    f = sorted(glob.glob(os.path.join(folder, "all-jobs-*.json")))[-1]
    return {(r["source"], r["source_id"]): r for r in json.load(open(f, encoding="utf-8"))["records"]}


def compare(ref, other):
    both = ref.keys() & other.keys()
    disagree = sorted(k for k in both if bool(ref[k]["kept"]) != bool(other[k]["kept"]))
    return {"reference": len(ref), "form": len(other), "both": len(both), "only_reference": sorted(ref.keys() - other.keys()),
            "only_form": sorted(other.keys() - ref.keys()), "kept_by_reference": sum(1 for k in both if ref[k]["kept"]),
            "kept_by_form": sum(1 for k in both if other[k]["kept"]), "kept_by_both": sum(1 for k in both if ref[k]["kept"] and other[k]["kept"]),
            "disagree": disagree, "agreement_rate": round(1 - len(disagree) / len(both), 4) if both else None}


def report(c, ref, other):
    L = ["# Run comparison", "", "## Executive summary", "",
         f"The reference run and the form's run both saw {c['both']} postings. They agree on keeping or rejecting {c['agreement_rate']:.1%} of them; "
         f"{len(c['disagree'])} disagree. {len(c['only_reference'])} postings only the reference saw and {len(c['only_form'])} only the form saw. "
         "Every disagreement is a question, not a verdict.", "", "| | Reference | Form |", "|---|---|---|",
         f"| postings read | {c['reference']} | {c['form']} |", f"| kept (of those both saw) | {c['kept_by_reference']} | {c['kept_by_form']} |",
         f"| kept by both | {c['kept_by_both']} | |", "", "## Disagreements", "", "| Company | Title | Reference kept | Form kept |", "|---|---|---|---|"]
    for k in c["disagree"][:200]:
        L.append(f"| {ref[k]['company']} | {ref[k]['title'][:70]} | {ref[k]['kept']} | {other[k]['kept']} |")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reference"); ap.add_argument("form"); ap.add_argument("--out")
    a = ap.parse_args(argv)
    ref, other = load(a.reference), load(a.form)
    c = compare(ref, other)
    text = report(c, ref, other)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
    print(text.split("## Disagreements")[0].strip().split("\n", 3)[-1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
