# 06 — Setup Exercise: Your search's personal layer

25 points · **not published in Canvas** · exported due date Thu Jun 25, 2026 (summer)

Brief: [`06-setup-exercise-personal-layer.md`](../../../assignments/fall-2026/06-setup-exercise-personal-layer.md) · Master plan: [`../PLAN.md`](../PLAN.md)

## Executive summary

**What it is.** Add a `search/` folder to a Reallocation Engine fork with three files: `resume.json` (an attested record), `profile.yml` (target role and constraints), and `gaps.md` (the delta between evidence and target). The agent extracts and formats; the person attests, corrects and signs.

**Where it stands.** Not started as this assignment, and not assigned this term. Related material exists: `facts/professor-bear-cv.json` is the CV as structured facts (attested, with two sections added 2026-09-27 that are not), and the engine working copy has its own `search/resume.json`.

**Next move.** Only if Professor Bear decides to use this assignment. If so, the CV facts are the starting point and the attesting is his.

---

## What the brief requires, and where each piece stands

✅ done · 🟡 partly · ⬜ not started · ➖ not an instructor deliverable

| Requirement | Status | Note | Evidence |
|---|---|---|---|
| `search/resume.json` extracted and errors caught | ➖ | Not generated, at Professor Bear's word (2026-10-18): the résumé is already JSON. The attested CV facts file and the derived résumé in `greenhouse-watch-demo/` stand; the 2026-09-27 sections of the facts file are still unread by him, and his 2026-09-23 read found no errors (the exercise expects at least three). | `facts/professor-bear-cv.json` |
| `search/profile.yml` | ✅ | Written from his own answers on 2026-10-18, with a dated `revisions` block; committed locally, not pushed (it names his citizenship; he decides). | `search/profile.yml` |
| `search/gaps.md` | ⬜ | **Waits for data, on purpose.** The gap between his record and the target roles is measured against real postings, not guessed. Needs the Google and Microsoft collectors (running 2026-10-18, hours, none finished) and the existing 3,243-posting run. Writing it earlier would be a guess presented as a finding. | - |
| Verification check and log | ⬜ | - | - |
| Privacy: `search/private-notes.md` kept out of git | ⬜ | This repo is public; personal notes must stay out. | - |

## What exists

- The CV facts file and the figma-role iteration under `figma/` (shared).

## What is still to do

- Everything, if the assignment is used.

## Plan of attack to a rough draft

| # | Who | Step | Size |
|---|---|---|---|
| 1 | Professor Bear | Decide whether this assignment is used this term. It carries a summer due date and is unpublished. | Decision. |
| 2 | Claude Code | If used: map the CV facts into the exercise's three files and mark each field attested or not. | Draft. |
| 3 | Professor Bear | Attest or correct every field; write `profile.yml` and `gaps.md` choices himself. | His judgment. |

## Decisions only Professor Bear can make

- Use this term or not.

## Honest limits

- A résumé in a public repo is a privacy decision; nothing goes in until he says what may be public.

---

*Written 2026-10-18 from the Canvas export, the folder's `FRICTIONAL.md`, and the files named above. Nothing here records an approval, a prediction or an understanding that Professor Bear did not state.*
