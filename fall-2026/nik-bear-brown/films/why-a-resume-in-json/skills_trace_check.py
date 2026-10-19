#!/usr/bin/env python3
"""skills_trace_check.py — does every skill on the derived résumé appear in the CV record it came from?

The film's real evidence. Stdlib only. A skill passes if its words appear, case-insensitively, in the text of the
attested CV record (facts/professor-bear-cv.json). It is a literal check: it finds a skill nobody wrote down in the
record; it cannot tell whether the record is true, or whether a skill that appears once is well supported.

    python3 skills_trace_check.py
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
facts = json.load(open(os.path.join(ROOT, "facts", "professor-bear-cv.json"), encoding="utf-8"))
derived = json.load(open(os.path.join(ROOT, "greenhouse-watch-demo", "resumes", "professor-bear.json"), encoding="utf-8"))

# the record's own text, minus its comments and attestation notes (which discuss skills without claiming them)
record = {k: v for k, v in facts.items() if not k.startswith("_") and k not in ("attestation_note", "pending_owner_review")}
text = json.dumps(record, ensure_ascii=False).lower()
text = re.sub(r"[^a-z0-9+#]+", " ", text)

def appears(skill):
    s = re.sub(r"[^a-z0-9+#]+", " ", skill.lower()).strip()
    return len(re.findall(r"(?<![a-z0-9])" + re.escape(s) + r"(?![a-z0-9])", text))

total = missing = 0
print(f"Record: attested {facts['attested_date']}; derived résumé: attested={derived['attested']}\n")
for group, skills in derived["skills"].items():
    if not isinstance(skills, list):
        continue
    for s in skills:
        total += 1
        n = appears(s)
        if n == 0:
            missing += 1
        print(f"  {'MISSING' if n == 0 else 'found  '} {group:28} {s:26} appears {n}x in the record")
print(f"\n{total} skills on the derived résumé; {total - missing} appear in the record; {missing} do not.")
sys.exit(1 if missing else 0)
