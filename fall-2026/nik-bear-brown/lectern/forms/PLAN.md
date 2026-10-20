# Lectern in other forms: which parallel versions to build

## Executive summary

**What this is.** Professor Bear's plan (2026-10-20) for building Lectern more than once: the plain Python stays the reference, and eight other versions each change one thing (where the control flow is written, who makes the judgment, where the state lives, who can change the rules, whether it can find new companies). **Why it exists.** The point is not to prove the job can be done another way; it is to find out what each framework or agent does that nobody thought of, and what it costs, with the Python as the oracle. **What it decides.** Which versions to build and in what order, how to compare them (the same columns for every version), and how to audit agents that write their own logs. The architecture rule that goes with it, one list of targets that every form reads and none copies, is in `README.md` in this folder.

*Edits to the text below, made when it was filed: "seven" boards became "six" (the watch list changed on 2026-10-20), and the product claims in the Rung 5 table (launch dates, tiers, the free-tier token figure) are Professor Bear's and have not been checked by the person filing this; the plan itself says to check the free tier against a real account first.*

## Why build it more than once

Lectern works in plain Python, and the Python stays the reference. The point of building parallel versions isn't to prove the job can be done another way. It's to find out what each framework or agent does that you didn't think of, and what that costs.

Two facts shape the choice. First, no model makes any decision in Lectern today: every judgment is a rule in `keywords.json` or an if-statement in `publish_delta.py`. That makes Python vs n8n a workflow comparison, not an agentic one. Second, the Python is closed-world. It can only watch the boards listed in `sources.json`. Agents with a browser can be open-world, and finding companies that belong on the list is the job you currently do by hand. That's the most likely place for a useful surprise.

So pick each parallel version to move one thing:

| What moves | The question it answers |
| --- | --- |
| Where control flow is written | Code, canvas, graph, prompt, or a vendor's agent? |
| Who makes the judgment | A rule, one model call, a team of models, or an always-on agent? |
| Where state lives | Files, a database, framework checkpoints, or a vendor's VM? |
| Who can change the rules | Can a keyword change without touching code? |
| Open or closed world | Does it only watch the list, or can it find new companies? |

## The build list

| # | Version | Folder | Status | Who runs it | What it's there to show | Oracle |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Plain Python | (this `lectern/` folder) | Built | Instructor | The reference | — |
| 2 | n8n | `n8n/` | Built | Instructor | The same workflow on a canvas | Identical output |
| 3 | One-call judge (Pydantic AI) | `judge-pydantic-ai/` | Build | Instructor, then students | What a model does in place of the keyword filter | Agreement with the keyword filter |
| 4 | CrewAI Flow | `crewai-flow/` | Build | Students | CrewAI used deterministically | Identical output |
| 5 | CrewAI Crew | `crewai-crew/` | Build | Students | Role-based agents deciding the flow | Agreement, plus the broken-source test |
| 6 | LangGraph | `langgraph/` | Build | Students | An explicit graph with model nodes, n8n's sibling in code | Agreement, plus path traces |
| 7 | Muse (Meta) | `muse/` | Running | Students | An always-on agent on the free tier | Agreement, the discovery log, Discord precision |
| 8 | Grok Bot (SpaceXAI) | `grok-bot/` | Running | Instructor | An always-on agent on a paid tier | Same as Muse |
| 9 | Dots (OpenAI) | `dots/` | Run | Instructor | An always-on agent on a paid tier | Same as Muse |
| — | GitHub Actions | `.github/workflows/` at the repository root (not yet written) | Build | Instructor | The scheduler and the heartbeat check, not a separate version | — |

**Optional, if time allows:** Dagster or Temporal (same rules, different orchestrator; Dagster if the lesson is lineage, Temporal if it's failure), DSPy (optimizes the judge against your audited rejects), and an explicit operator agent built with the Claude Agent SDK or the OpenAI Agents SDK that runs the existing scripts.

## A ladder, by how much decision goes to a model

| Rung | Form | Versions on the list | Oracle |
| --- | --- | --- | --- |
| 0 | Same rules, different orchestrator | n8n; optionally Dagster or Temporal | Identical output |
| 1 | One model call replaces the filter | Pydantic AI judge; optionally DSPy | Agreement with the keyword filter |
| 2 | Explicit graph with model nodes | LangGraph, CrewAI Flow | Agreement, plus path traces |
| 3 | Agents decide the flow | CrewAI Crew | Agreement, plus invariant tests |
| 4 | An agent operates the existing scripts | Optional operator agent | Python output unchanged; you judge the operator |
| 5 | No code: an English spec on the vendor's computer | Muse, Grok Bot, Dots | Agreement, the discovery log, Discord precision |

### Rung 1: the one-call judge

This gives the most lesson for the least work, and it isn't a full translation. Replace the keyword filter with one structured model call that returns a typed `{keep, family, reason}`. Run it over the same thousands of postings the keyword filter already judged and compare. The false-friend words that tripped the first filter make a ready-made adversarial set: does the model fall for the same words, or make new mistakes of its own? One table of agreements and disagreements makes the core Computational Skepticism point.

### Rungs 2 and 3: CrewAI twice, and LangGraph

CrewAI has two modes: Crews, where role-based agents collaborate, and Flows, which are event-driven and run in a guaranteed order. Its own docs point to Flows when you need deterministic, auditable results. Build both. The Flow version should match the Python exactly, and if it doesn't, that's a bug. The Crew version (a Scout that reads the boards, a Judge that keeps or rejects, an Editor that writes the Discord post) won't match, and how far it misses is the lesson. Building both inside one framework removes the "different tools give different results" excuse, and it shows students that a crew doing deterministic work is mostly function calls with personas attached.

LangGraph has the same shape as n8n but lives in code, with model calls as nodes, checkpointing, and an interrupt before anything posts. Because the structure matches n8n, the comparison isolates what a model node changes. Microsoft Agent Framework (the successor to AutoGen and Semantic Kernel) covers the same ground. Pick one of the two, and pick Microsoft only if your students are headed for Microsoft or .NET shops.

### Rung 5: the always-on agents

Grok Bot, Muse, and Dots launched within seven weeks of each other in August and September 2026. Each runs on its own cloud computer, connects to outside apps, and keeps working after the user logs off. Recurring watch jobs like Lectern are what they were built for.

|  | Grok Bot | Muse | Dots |
| --- | --- | --- | --- |
| Maker | SpaceXAI | Meta | OpenAI |
| Launched | August 11, 2026 (early beta) | September 8, 2026 | September 29, 2026 |
| Access | SuperGrok Heavy, Cursor Ultra, Cursor Teams Premium | Free for most everyday use; US rollout | ChatGPT Pro and Business Premium; Enterprise and Edu if an admin enables the beta |
| Scheduling | Routines (works much like cron) | Background work after the app closes | Continuing work toward user-set goals |
| Safety layer | A review agent that can allow, block, or escalate actions | A Sentinel agent that must approve anything sent to the internet | Admin controls; Microsoft Agent 365 integration announced for business Dots |
| Who runs it here | Instructor | Students | Instructor |

**Run each of them two ways.**

- **The strict spec** is written from `keywords.json` and this README. It should agree with the Python, so it serves the oracle comparison. It also inherits the filter's blind spots, false friends included.
- **The loose spec** is written from the intent in `profile.yml` (the file nothing reads today): find companies and roles where an honest educational AI advocate would fit. This is the discovery run. It's where you find out whether the agents spot something the keyword filter can't.

**Split the watch list in two.** The API half is the six Greenhouse, Ashby, and SmartRecruiters boards. These publish JSON, the Python already gets them right for almost nothing, and an agent that clicks through them like a person is slower, more expensive, and less exact. The big-four half is Google, Amazon, Microsoft, and Meta. These have no simple public feed and your collectors take hours on them. That half is where a browsing agent might actually earn its cost. Without the split, the cost question can only come out one way.

**Compare products, not models.** Each tool bundles a different model, browser, set of connectors, and safety layer. That's fine, since it's what a buyer pays for, but say so in the writeup. The safety layers also decide whether a scheduled run finishes unattended. Whether the daily Discord post goes out on its own or waits for approval is a result.

## Audit design

### The repo is the audit trail

- **Logs go straight in.** Each tool gets an append-only `logs/<tool>/` folder it writes to freely, because a log you have to approve stops being a log.
- **Outputs that change state wait for review.** Anything that changes `published-state.json` or the delta is written to the tool's own folder or branch and not acted on without review.
- **Every tool uses one output format:** the same fields the Python writes to `runs/DATE/`, whether a run lands in GitHub or Drive. Otherwise each agent invents its own format and nothing can be compared.
- **Protect the branch the logs land on.** Block force-pushes and branch deletion, so no agent can rewrite its own history. Otherwise the audit trail is only as trustworthy as the thing it audits.

### Logs are self-reports

Each agent writes its own trace, so its log can describe a fetch that never happened, leave out a failed one, or turn a messy run into a clean story. Check each log against evidence the agent didn't write: commit timestamps, the Discord message history, the Python's snapshot of the same boards on the same day, and the vendor's own activity records where they exist (Grok Bot has its agents check their work with screen recordings). Where the self-report and the outside evidence disagree, that's a finding about the agent.

### The heartbeat lives outside the agents

An agent that didn't run can't report that it didn't run. A small scheduled GitHub Action checks for each tool's log commit by its expected time and raises an alert if one is missing. The alert goes to an ops channel or email, never to the channel for human review.

### Differences between tools are the audit, but only for errors they don't share

Several tools doing the same job independently means every disagreement points to a mistake somewhere. Agreement is weaker evidence than it looks, because these tools read the same boards and may work from the same spec, so their errors can line up. Knight and Leveson found exactly this with independently written software versions in 1986. Three cheap fixes:

- Run the loose spec as well as the strict one, so not every tool inherits `keywords.json`.
- Keep sampling the postings every tool agreed to reject, because nobody looks at those.
- Give the independent auditor a model family none of the collectors run on, and hand it the raw board data rather than the agents' outputs, so it judges postings fresh instead of grading the other agents' homework.

### Discovered companies need evidence

Every company a tool proposes for the watch list comes with a link to a public page that backs the claim, and students check a sample. Agents can confidently describe an education program that doesn't exist, or one that turns out to be product training (HubSpot Academy, for example, teaches HubSpot rather than AI in education).

## Discord: the human-judgment channel

The channel exists to narrow tens of thousands of postings to the few dozen a person can actually read. Human attention is the scarce resource, so the channel is also where each tool gets measured.

- **Every post is tagged with the tool that made it.**
- **The reader reacts with a thumbs up or down.** Those reactions are labeled data at almost no cost: each tool's precision measured against human judgment.
- **Watch for the pattern you're hoping for.** If a tool keeps surfacing posts people mark useful that the Python filter rejected, that's the discovery you wanted, with evidence behind it.

No logs or activity updates go to this channel.

## Student setup

Students run Muse on its VM, post to the class Discord, and write to the class GitHub. Muse is built as a personal agent that wants access to email, calendars, and payments, and Lectern needs none of that. Students should connect only what the task needs (the public boards, the class Discord, the repo), ideally from a throwaway account rather than their personal one. One report puts the free tier at 100 million tokens a week; check that against an actual account before planning around it.

## The same columns for every version

| Column | What to record |
| --- | --- |
| Oracle | Identical output, or the agreement rate with the disagreements read by hand |
| Broken-source test | Given a board that returns an error, did the tool close its postings? |
| Found | What it did that the Python can't: read the whole posting, explained a fit, caught a duplicate, proposed a company (with its evidence link) |
| Discord precision | The share of its posts that got a thumbs up |
| Log vs evidence | Where its self-report disagreed with commits, Discord, or the Python snapshot |
| Heartbeat | Missed runs |
| Where the rules live | JSON, code, prompt, or a vendor settings page |
| Unattended completion | Did a scheduled run finish without waiting for approval? |
| Cost and time per run | Tokens or subscription share, and wall-clock time, on each half of the watch list |
| Time to first working version | Hours |
| Fits `sync.sh` | Whether the version survives being flattened into the other classes' single folder (code-based versions only) |

## Build order

1. **The shared plumbing comes first,** because every comparison depends on it: one output format, the `logs/` layout, branch protection, and the heartbeat Action. Muse and Grok Bot are already running, so their output needs to fit the format before it piles up.
2. **The one-call judge.**
3. **A week of Muse, Grok Bot, and Dots** running the strict and loose specs on both halves of the watch list, scored against the Python.
4. **CrewAI, built as both a Flow and a Crew.**
5. **LangGraph.**
6. **The optional versions,** if the comparisons so far leave a question only one of them can answer.

## Skip these

**Zapier and Make** repeat n8n's lesson with less visibility into what ran. **Langflow, Flowise, and Dify** are visual model builders that duplicate n8n and LangGraph together. **Mastra** and the other TypeScript frameworks change the language, not the idea. **Airflow** is heavier than Dagster and adds no lesson for a pipeline this size. **Microsoft Agent Framework** duplicates LangGraph unless your students are headed for .NET.

## Further reading

- Knight, J. C., and Leveson, N. G. (1986). An experimental evaluation of the assumption of independence in multiversion programming. *IEEE Transactions on Software Engineering*, SE-12(1).
- CrewAI documentation on Crews vs Flows: https://docs.crewai.com
- Microsoft Agent Framework overview: https://learn.microsoft.com/agent-framework/overview/
