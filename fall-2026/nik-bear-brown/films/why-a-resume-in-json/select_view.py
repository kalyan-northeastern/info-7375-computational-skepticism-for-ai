#!/usr/bin/env python3
"""select_view.py — one long record, one page per opportunity: which roles in the record fit this posting?

The film's second piece of real evidence. Stdlib only. It scores each role in the attested CV record by how many of
the posting's keywords appear in that role's own text (organization, title, details), and lists the roles it would put
on a one-page view. It SUGGESTS. A person decides what goes on the page; the script only shows that the choice comes
from the record and changes with the opportunity, without editing a document.

    python3 select_view.py            # uses selection_targets.json next to this file
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
ONE_PAGE = 6   # how many roles a one-page view holds here; a choice, not a rule

facts = json.load(open(os.path.join(ROOT, "facts", "professor-bear-cv.json"), encoding="utf-8"))
roles = facts["experience"]
targets = json.load(open(os.path.join(HERE, "selection_targets.json"), encoding="utf-8"))

def words(s):
    return set(re.findall(r"[a-z][a-z\-]{3,}", s.lower()))

def role_text(r):
    return " ".join([r.get("organization", ""), r.get("title", "")] + list(r.get("details", [])))

print(f"The record holds {len(roles)} roles, {len(json.dumps(facts, ensure_ascii=False)):,} characters. A one-page view holds {ONE_PAGE}.\n")
picked = []
for t in targets:
    kw = set(t["keywords"])
    scored = sorted(((len(kw & words(role_text(r))), i, r) for i, r in enumerate(roles)), key=lambda x: (-x[0], x[1]))
    top = scored[:ONE_PAGE]
    picked.append({i for _, i, _ in top})
    print(t["name"])
    print(f"  posting: {t['title']}  ({len(kw)} keywords)")
    for s, i, r in top:
        print(f"  {s:>2} shared  [{i:>2}] {r['title']}, {r['organization']} ({r.get('start','?')}-{r.get('end','?')})")
    print()
both = picked[0] & picked[1]
print(f"Roles on both one-page views: {len(both)} of {ONE_PAGE}. Only on A: {len(picked[0]-picked[1])}. Only on B: {len(picked[1]-picked[0])}.")
print("Left off both views, still in the record:", len(roles) - len(picked[0] | picked[1]), "of", len(roles), "roles.")
