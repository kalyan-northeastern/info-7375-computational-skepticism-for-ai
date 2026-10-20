# CrewAI Flow

## Executive summary

**What this is.** A parallel version of Lectern, built to find out what CrewAI Flow does that the plain Python does not, and what it costs. CrewAI used deterministically: an event-driven flow that runs in a guaranteed order. It should match the Python exactly; if it does not, that is a bug. **Why it is here.** Each version moves one thing (see `../PLAN.md`); this one's job is rung 2 of the ladder. **Where it stands.** Not started. Nothing in this folder has been built or run.

## What it reads (one source of truth)

- **The targets:** `../../config/targets.json`, read directly and never copied. Which companies, schools and research groups to look at, and which have been removed and why, are decided there and only there.
- **The rules:** `../../config/keywords.json` for the strict run; `../../../06-setup-exercise-personal-layer/search/profile.yml` for a loose run (what an honest educational AI advocate would fit).
- **Never edits** either file. A company this version finds is written to `proposed-targets.jsonl` here, each with a link to a public page that backs the claim; a person promotes it.

## What it owns

How it collects (it may collect its own data, so the way it reads a board can be compared with the Python's), how it judges, where its state lives, and how it is scheduled: the flow definition and its steps.

## What it writes

The standard run format (`runs/DATE/all-jobs-DATE.json` and `jobs-of-interest-DATE.json`, checked by `../../compare/check_run_format.py`) and an append-only log in `../../logs/crewai-flow/`. It is compared with the reference run by `../../compare/compare_runs.py`.

## How it is judged

Oracle: Identical output. The same columns as every version are in `../PLAN.md`: broken-source test, what it found, Discord precision, log against outside evidence, heartbeat, where the rules live, unattended completion, cost and time, time to first working version.

## To do

Everything. First: make it write the standard run format on one day's boards, then run `../../compare/compare_runs.py` against that day's Python run.
