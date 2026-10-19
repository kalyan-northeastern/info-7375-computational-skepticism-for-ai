# 04 — The Reallocation Engine: Mode Design

25 points · due Sat Oct 10, 2026, 11:59 PM ET · published in Canvas · **past due**

Brief: [`04-reallocation-engine-mode-design.md`](../../../assignments/fall-2026/04-reallocation-engine-mode-design.md) · Master plan: [`../PLAN.md`](../PLAN.md)

## Executive summary

**What it is.** Design a new **mode** for the Reallocation Engine for your own domain: a mode file in the style of the repo's existing modes, a one-page domain justification, and a worked example run or simulated against real or realistic input. The mode does not have to be implemented, but it has to be honest about what does not exist yet.

**Where it stands.** Closest existing work is a drafted **case recipe** for this very search (`nikbearbrown-advocate-education-search` and its card), drafted before 2026-10-07 in the Reallocation Engine working copy, where it is still uncommitted (per the 2026-10-07 status report). The Canvas brief says "mode"; the working copy's equivalent artifacts are called "recipes". No mode file in the brief's format exists. The job-search tool itself (Lectern) is the natural subject, and a real run happened today.

**Next move.** Convert the case recipe into a mode file, using Lectern's real outputs as the worked example.

---

## What the brief requires, and where each piece stands

✅ done · 🟡 partly · ⬜ not started · ➖ not an instructor deliverable

| Requirement | Status | Note | Evidence |
|---|---|---|---|
| Mode file (what and when, sources and exact commands, proposed new sources, can and cannot verify, output format, RUN_LOG template) | 🟡 | A case recipe and card exist but not in the brief's mode format. | Reallocation Engine working copy, `recipes/cases/2026fa/` |
| Domain justification, one page or less | ⬜ | Information asymmetry, which engine layer it connects to, domain-specific failure modes. | - |
| Worked example with verified-versus-inferred commentary | 🟡 | A real collection run exists (2026-10-18: 3,243 postings fetched, 88 kept). Commentary not written. | `lectern/runs/2026-10-18/` |
| In-class presentation (5 points) | ➖ | A student task; optional for the instructor example. | - |
| GitHub folder link and final commit hash | ⬜ | At submission time. | - |

## What exists

- The case recipe and its card for the education and advocate job search (uncommitted in the engine working copy).
- Lectern: `collect.py` (18 boards on three applicant-tracking systems), the big-four collectors, the monitor, the faculty-listings reader, and the audit scripts.
- Run outputs: 2026-09-26 (3,446 postings, 97 kept, in Branding's graded folder), 2026-10-08 (six companies), 2026-10-18 (3,243 fetched, 88 kept).

## What is still to do

- Read two existing modes in the canonical engine repo for the file format.
- Draft the mode file and the justification.
- Write the worked-example commentary against the 2026-10-18 run: what was verified (counts are records) and what was inferred (a keyword match is a guess).

## Plan of attack to a rough draft

| # | Who | Step | Size |
|---|---|---|---|
| 1 | Claude Code | Read two existing mode files in the canonical engine repo and note the required sections and the `RUN_LOG.md` entry format. | Read-only. Short. |
| 2 | Claude Code | Draft the mode file from the case recipe: exact commands (`collect.py --out`, the daily runner, the audits), what each verifies, what it cannot, and the output table. | Draft. |
| 3 | Claude Code | Draft the worked example from the 2026-10-18 run with a verified-versus-inferred table and a "what I would change" list. | Draft. |
| 4 | Professor Bear | Write or rewrite the domain justification: who uses the mode, the asymmetry, and the failure mode hardest to catch (candidate from the log: a company that cannot be read looks like a company with no demand). | His judgment. |
| 5 | Professor Bear | Decide whether the mode proposes new commands (candidate: the push-only-what-changed publisher). | Decision. |
| 6 | Claude Code | Assemble the folder and log the work in `FRICTIONAL.md`. | Assembly. |

## Decisions only Professor Bear can make

- Which mode to design (job search for education and advocate roles is the obvious one).
- Whether the recipe in the engine working copy is committed, and where.

## Honest limits

- The engine working copy and the canonical repo may differ in layout. The mode format is taken from the canonical repo, not assumed.
- The worked example is a run of Lectern, a collector. The brief asks for a mode run or simulation; the commentary must say which it is.

---

*Written 2026-10-18 from the Canvas export, the folder's `FRICTIONAL.md`, and the files named above. Nothing here records an approval, a prediction or an understanding that Professor Bear did not state.*
