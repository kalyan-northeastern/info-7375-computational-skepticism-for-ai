# 09 — The Reallocation Engine, Audited: build a useful tool that doubts itself

100 points · **not published in Canvas** · exported due date Mon Jul 27, 2026 (summer; Canvas text says "set on Canvas")

Brief: [`09-reallocation-engine-audited.md`](../../../assignments/fall-2026/09-reallocation-engine-audited.md) · Master plan: [`../PLAN.md`](../PLAN.md)

## Executive summary

**What it is.** Build a reallocation tool (anything that moves a scarce resource) and audit it on seven components: the working tool, data validation and a GIGO gate, a bias audit, an explainability critique, Pearl's three rungs, adversarial fragility, and a delegation map with a hard-stop gate. Plus a 5 to 8 minute video, Frictional Journal, and AI Use Disclosure.

**Where it stands.** Not started as this assignment. Lectern already contains pieces that resemble several components, but the mapping below is a hypothesis, not a finding: a trusted-run rule (at least 90% of the reported total and 70% of the previous run), reject and title audits, matched words stored per kept record, the Boondoggle Score's handoffs, and a no-push-without-word rule. None of this was built against this brief.

**Next move.** Only if used. The first step is to test the mapping honestly against each of the seven components.

---

## What the brief requires, and where each piece stands

✅ done · 🟡 partly · ⬜ not started · ➖ not an instructor deliverable

| Requirement | Status | Note | Evidence |
|---|---|---|---|
| Working tool (12) | 🟡 | Lectern runs; whether it is a "reallocation" tool in the brief's sense is a judgment call. | `lectern/` |
| Data validation and GIGO gate (10) | 🟡 | Candidate: the monitor's trusted-run rule; rejects by reason. | `lectern/collectors/monitor.py` |
| Bias audit (10) | 🟡 | Candidate: reject audit and title audit; the unreadable-companies selection effect. | `lectern/audit_rejects.py`, `audit_titles.py` |
| Explainability and its critique (10) | ⬜ | - | - |
| Causal and counterfactual reasoning, Pearl's rungs (15) | ⬜ | - | - |
| Adversarial robustness and fragility (8) | ⬜ | - | - |
| Delegation map and hard-stop gate (10) | 🟡 | Candidate: the Boondoggle Score handoffs; the push rule. | 03 report |
| Video 5 to 8 minutes, Frictional, AI Use Disclosure | ⬜ | - | - |

## What exists

- Lectern and its audits; the Week 2 Boondoggle Score; six Liam films on this assignment's method.

## What is still to do

- All seven components tested against the brief, the video, the disclosure.

## Plan of attack to a rough draft

| # | Who | Step | Size |
|---|---|---|---|
| 1 | Professor Bear | Decide whether to use this assignment. | Decision. |
| 2 | Claude Code | Test the mapping: for each component, show the file that does it or say there is none. | Read-only. Short. |
| 3 | Professor Bear | Decide what to build for the gaps (explainability, causal rungs, fragility). | Decision. |

## Decisions only Professor Bear can make

- Use or not.

## Honest limits

- Largest of the unpublished ones short of the capstone.

---

*Written 2026-10-18 from the Canvas export, the folder's `FRICTIONAL.md`, and the files named above. Nothing here records an approval, a prediction or an understanding that Professor Bear did not state.*
