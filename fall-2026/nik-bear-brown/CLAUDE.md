# CLAUDE.md — nik-bear-brown/ (Professor Bear's example folder)

This folder is the instructor's public example work for INFO 7375 Computational Skepticism for AI, Fall 2026. It keeps the same process record students keep. **Every substantive change here is logged in `FRICTIONAL.md`, and every push adds a line to it.** The repo-root `AGENTS.md` still governs everything else.

## Rule 0 — this folder is the canonical master for three classes

The same job-search tool is live-coded in Computational Skepticism, Branding and AI, and Prompt Engineering. **The shared files live here and are copied out.** Read [`SYNC.md`](SYNC.md) before editing anything in `lectern/`, `facts/`, `figma/`, or `greenhouse-watch-demo/`.

- **Edit a shared file here, never downstream.** After editing, run `./lectern/sync.sh --check`, then `./lectern/sync.sh`.
- **Never copy** `FRICTIONAL.md`, `README.md`, `CLAUDE.md`, an `assignment-*/` folder, or a dated run output between classes. A log overwritten by another class's log is a destroyed record.
- **`sync.sh` does not commit.** Each repo is committed by hand with its own message and its own `FRICTIONAL.md` entry.
- If a shared file was edited in the wrong repo during a class, follow the recovery steps in `SYNC.md` — and log the drift, because it is a finding about the workflow.

## Rule 1 — log every substantive change in FRICTIONAL.md

Before you report a task in this folder as done, update `FRICTIONAL.md` in the same change set.

**Substantive** means anything a reader of the log would need in order to understand the work:
- a new or deleted file or folder;
- a change to what a result says (a new Gru turn, a changed verdict, a new section of the design document);
- a decision, a reversal, or something that went wrong.

**Not substantive:** typo, wording, or formatting fixes that don't change meaning. Leave those out rather than padding the log.

**How to log it:**
- **Same day, same work:** extend that day's entry. Don't start a second entry for the same session.
- **New day or new piece of work:** add a new entry under `## Entries`, newest last, headed `### YYYY-MM-DD — <what it was>`, using the course's seven fields, verbatim and in order:
  - Date and what I was working on
  - I tried / expected
  - What happened
  - What I did
  - What Claude or another person contributed
  - What I understand now / still do not understand
  - Evidence and next step
- **Write what happened, not what was hoped.** Include what failed. Name the files that serve as evidence. Never invent a prediction, a result, an approval, or an understanding Professor Bear didn't state.
- **Credit honestly.** Say what Claude Code did and what Professor Bear decided. If he hasn't reviewed something, say so.
- Keep the executive summary at the top current.

## Rule 2 — Gru's words are never edited

Files in `03-week-2-boondoggle-report/gru-session/` and `03-week-2-boondoggle-report/gru-session-downloadable-gru/` (renamed from `boondoggle-report/` on 2026-10-18) hold Gru's replies verbatim. So do the blocks under "Gru's section outputs" in `FRICTIONAL.md`, which are sliced from those files by script. They are copied from the conversation transcript by script, never retyped or cleaned up. The brief says Gru's errors and pushback are part of the submission.

## Rule 3 — one line per GitHub push

Every push that touches this folder adds a row to the `## GitHub pushes` table, **in the same commit being pushed**:

```
| YYYY-MM-DD | <commit subject, exactly as committed> |
```

- The note is the commit subject, copied exactly. The repo uses conventional subjects (`feat(fall-2026): …`, `docs(fall-2026): …`).
- No commit ID in the row: a commit can't contain its own ID, and `git log` holds it.

## Rule 4 — new possible listings are posted to Discord automatically

**Standing rule (Professor Bear, 2026-10-19):** every time a run finds new possible listings, post them to the public `#professor-bear` channel of the SEIS AI Lab Discord server without being asked, so he can see them whenever he looks. This is not a question to ask each time.

- **How:** `lectern/daily.sh` does it (`publish_delta.py --write --post`, then `faculty_feed.py --send`). A run you start by hand uses `publish_delta.py --post`, or `--post-only` for a run already collected. Both go through `lectern/notify.py`.
- **What goes in a post:** only listings from companies still on the watch list, most-wanted employers first, each with its link and the words that matched, newly watched companies marked, and the line "A person decides; the machine only ranks words." Posted ids are remembered, so nothing is posted twice.
- **What never does:** a local path, an email address, a webhook URL, or an unlisted YouTube link. The webhook stays in the home folder.
- **Posting is not pushing.** Posting a run's listings to Discord needs no word; pushing its delta to GitHub still does.

## Rule 5 — great-fit labs are posted to Discord, and nothing is approached before Professor Bear has looked

**Standing rule (Professor Bear, 2026-10-19):** when a lab or research group looks like a great fit, post its page to the public `#professor-bear` channel so he can look at it. For a company such as Moderna that is a research group's page, not a job posting. Then he, as a person, reads the page and decides. No lab is approached, drafted to or written to before he has looked, and the emails are his to write and send.

- **Tiers:** `great` fits first. `pretty_good` fits are posted only when he says so, after great fits have come to nothing. Do not widen on your own.
- **How:** `lectern/notify.py` `post_labs()` (tested with made-up labs in `lectern/test_notify.py`). It reads only the lab's public name, institution, page link, tier, kind and the lab's own words (300 characters at most).
- **What never goes in a post:** the principal investigator, a lab manager or any other person; an email address or phone number; a local path; a webhook URL. A lab named for a person is shown as "A lab at <institution>" with its link. The lab records themselves name people and stay local (`lectern/labs/`, `lectern/lab-records/`, gitignored).
- **Not built yet:** the reader that turns lab pages into candidates (see `lab-outreach/LAB-RECORD.md`). Until it exists there is nothing to post.
- **Posting is not pushing**, as in Rule 4.

## Rule 6 — `lectern/HISTORY.md` is the daily log of the code

**Standing instruction (Professor Bear, 2026-10-20):** keep `lectern/HISTORY.md` as a daily log of what was added to `lectern/` and when, and how the tool is being built up, alongside `FRICTIONAL.md`. Whenever a file in `lectern/` is added, removed or changed in what it does, add a dated entry (date, what, why) **in the same change**, and keep the tables in `lectern/README.md` true. Write what happened, including what failed; never a result nobody ran. The same goes for `lectern-n8n/` (the n8n form, kept beside the Python form): its README says what is tested. **Also keep `TARGETS.md` true:** when a target is added, removed or reclassified, or a reader for one is built or fails, change its row in the same change.

## Pushing from this folder

- **Each push needs Professor Bear's word.** He approved the first push on 2026-09-24. There is no standing approval for this folder yet.
- Git on his machine is already authenticated. Never ask for, accept, or write down a GitHub token.
- Stage **only** `fall-2026/nik-bear-brown/` (and the one `.gitignore` line that tracks it). The repo often has other uncommitted instructor edits; never sweep them in.
- Run `python3 scripts/validate_course.py` from the repo root before committing.

## Privacy

This repo is public. The person here is **"Professor Bear."** No contact details, profile links, or other people's names. No absolute local paths (`/Users/…`) in anything committed. The personas named in the report (Priya Nair, Aarav Patel) are fictional, from the Reallocation Engine's `search/examples/`.
