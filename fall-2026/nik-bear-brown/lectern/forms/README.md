# forms/: Lectern built more than once

## Executive summary

**What this is.** One folder per parallel version of Lectern, beside the plain Python that stays the reference (the rest of `lectern/`). **Why.** To find out what each framework or agent does that nobody thought of, and what it costs, with the Python as the oracle; the full plan is in [`PLAN.md`](PLAN.md). **The rule that keeps it honest.** The project's point, which companies, schools and research groups are looked at and what counts as a match, has one source of truth that every form reads and none copies; each form owns only what is specific to it: how it collects, how it judges, where its state lives and how it is scheduled. **Where it stands.** The n8n form is built and tested against the Python; the other seven folders are placeholders with a README each, and nothing in them has been built.

## The single source of truth

| Read by every form, never copied | Owned by each form |
|---|---|
| `../config/targets.json`: every target, its type, its data links, whether it is removed and why | How it collects data (it may collect its own, to see whether it reads boards differently) |
| `../config/keywords.json`: the rules (the strict spec) | How it judges: a rule, one model call, a crew, an agent |
| the profile (the loose spec) | Where its state lives; how it is scheduled |
| the run format: what the Python writes to `runs/DATE/` | its own `logs/<tool>/` and `proposed-targets.jsonl` |

A form that finds a company writes a proposal with an evidence link; it never edits `targets.json`. Removed targets stay in that file with their reasons, so a discovery agent is shown what has already been ruled out.

## The folders

| Folder | Version | Status |
|---|---|---|
| (the parent folder) | Plain Python, the reference | built |
| [`n8n/`](n8n/) | Five n8n workflows | built, tested against the Python |
| [`judge-pydantic-ai/`](judge-pydantic-ai/) | One model call replaces the keyword filter | not started |
| [`crewai-flow/`](crewai-flow/) | CrewAI used deterministically | not started |
| [`crewai-crew/`](crewai-crew/) | CrewAI with role-based agents | not started |
| [`langgraph/`](langgraph/) | An explicit graph with model nodes | not started |
| [`muse/`](muse/) | Meta's always-on agent | running per the plan; nothing recorded here |
| [`grok-bot/`](grok-bot/) | SpaceXAI's always-on agent | running per the plan; nothing recorded here |
| [`dots/`](dots/) | OpenAI's always-on agent | to run |

The shared plumbing is in `../compare/` (the run-format check, the run comparison, the heartbeat) and `../logs/` (one append-only folder per tool). The heartbeat Action, when it is written, has to live at the repository root in `.github/workflows/`, the one place a Lectern file cannot be inside `lectern/`; it is not written yet (`compare/heartbeat.py` is the check it would run).
