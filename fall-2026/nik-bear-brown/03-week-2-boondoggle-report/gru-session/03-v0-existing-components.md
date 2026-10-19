# Gru turn 03-v0-existing-components

## Professor Bear typed

```
Here's what exists today:
- Sponsorship and funding: sponsorship history comes from DOL/H-1B records in data/80-days-to-stay/ (a 30,370-row company table); company funding comes from SEC Form D filings in data/sec/form-d/. They feed a composite scorer, scripts/score/role-scorer.mjs, that gives each role Apply / Consider / Skip with an audit trace. The watcher does NOT read any of them right now. It runs beside them.
- Company list: the student names one board per run (the company's slug on Greenhouse, Ashby, or SmartRecruiters). Nothing supplies the list.
- Résumé: structured JSON, the student's real one at search/resume.json (gitignored, never committed); three persona examples under search/examples/ are the shape and what anything committed must use. Other skills read the same file.
- Scheduler: none. Scheduling is the student's own launchd, cron, or GitHub Action.
```

## Gru replied (verbatim, unedited)

That's specific enough to work with. Here's the list of existing components:

> **Existing components touched:**
> - **Job boards on Greenhouse, Ashby, and SmartRecruiters**, which the watcher reads from outside the repo. The student names one company slug per run.
> - **`search/resume.json`**, the student's structured résumé. It's gitignored and shared with other skills. The persona files in `search/examples/` are the committed stand-ins.
> - **The student's own scheduler** (launchd, cron, or a GitHub Action). The engine doesn't supply one.
> - **Not touched:** `data/80-days-to-stay/`, `data/sec/form-d/`, and `scripts/score/role-scorer.mjs`. The watcher runs beside them on purpose.

Before Question 3, I need to flag one thing, and it's the most important thing you've told me so far.

**The engine already has a fit verdict.** `role-scorer.mjs` gives every role Apply, Consider, or Skip, with an audit trace. Your watcher is about to decide that a posting "fits the résumé" on its own. That means one student, one posting, and two judgments that can disagree. Picture the watcher saying "strong fit, go look" about a role the scorer marks Skip. The student now has to referee two parts of the same course tool. That's the refresh-and-wonder loop you're trying to remove, just moved somewhere else.

I'm not telling you to wire them together. Running beside the scorer can be the right call for a first version. But your sentence has to make clear what the watcher's output *is* next to the scorer's. Is it a **pre-filter** ("this posting is new and plausibly relevant, so score it")? Is it a **verdict** ("apply")? Or is it a **notice** ("these postings appeared since yesterday, ranked by résumé overlap")? Those are three different things to build.

One more thing the sentence needs. "New posting" means the watcher remembers what it saw on the last run. That memory is part of the thing, so the sentence should name it, not assume it.

**3. In one sentence, not a paragraph and not a list: what are you proposing to ADD?**

Format: **"[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]."**

It has to name:
- **The thing**, not the problem it solves. Leave out networking and saved time. That's the *why*, and it goes in /v1.
- **Where it sits.** Where it enters the engine and what it reads.
- **What it produces.** An actual file, message, or list, with enough detail that someone could tell whether they got it.

Write it yourself. I'll push back on it, but I won't write it for you.
