# Gru turn 05-v0-confirmed-v1-start

## Professor Bear typed

```
Both fair.
1. It supports all three. It started Greenhouse-only and was extended to Ashby and SmartRecruiters; the name is historical. I'm not renaming it inside this document, but log the misleading name as an open question and I'll name the platforms in the sentence.
2. "Front" was wrong. It's the entry point a student runs first, and it feeds nothing downstream today.

Revised: greenhouse-watch is a Claude Code skill that a student runs as an entry point to the Reallocation Engine, beside the role scorer and feeding nothing into it, reading one company's public job board on Greenhouse, Ashby, or SmartRecruiters plus the student's résumé JSON and remembering which job ids it saw last run, that produces a notice, not a verdict: a Markdown report and a JSON log listing only the postings new since the last run that match the résumé under a written string-match scheme, each with the résumé field and posting field behind every match.

Confirmed. Go to /v1.
```

## Gru replied (verbatim, unedited)

Confirmed. Handling the name that way is fine: the document keeps the real name and records that it's misleading, rather than hiding it.

---
**V0 SUMMARY (CONFIRMED)**

**Ecosystem:** The Reallocation Engine is a course repo of skills that students run themselves from Claude Code on their own laptops. It already has sponsorship (DOL/H-1B) and funding (SEC Form D) layers that feed a composite role scorer.

**Existing components touched:** Public job boards on Greenhouse, Ashby, and SmartRecruiters (read-only, one slug per run). `search/resume.json` (gitignored and shared; committed examples in `search/examples/`). The student's own scheduler. The watcher deliberately does **not** touch `data/80-days-to-stay/`, `data/sec/form-d/`, or `scripts/score/role-scorer.mjs`.

**Proposal:** "greenhouse-watch is a Claude Code skill that a student runs as an entry point to the Reallocation Engine, beside the role scorer and feeding nothing into it, reading one company's public job board on Greenhouse, Ashby, or SmartRecruiters plus the student's résumé JSON and remembering which job ids it saw last run, that produces a notice, not a verdict: a Markdown report and a JSON log listing only the postings new since the last run that match the résumé under a written string-match scheme, each with the résumé field and posting field behind every match."

**Open Questions Log (started):**
- **OQ-1: String-match scheme is undefined** (fields, normalization, match rule). **Stakes:** without it, "match" means whatever the implementer assumes. Owner: you. Due: before /d1. Status: Open.
- **OQ-2: The name "greenhouse-watch" misleads** because the skill also covers Ashby and SmartRecruiters. **Stakes:** students on Ashby or SmartRecruiters won't realize the skill covers their company's board. Options: rename it, add an alias, or explain it in the skill description. Owner: you. Due: before release. Status: Open.
- **Deferred to /s4: First-run behavior.** With no saved ids, every posting counts as "new."
---

## /v1: Problem Intake

/v0 already answered part of intake. Here's what I'm carrying forward so we don't cover it twice:

- **Name:** greenhouse-watch (see OQ-2)
- **Category:** a local CLI skill that polls and notifies
- **Deployment target:** the student's own laptop, through Claude Code, scheduled optionally with the student's own launchd, cron, or GitHub Action

I'll still ask you *why* this deployment target when we get to question 6. What I have so far is what it is, not why.

We start with the question /v0 kept out on purpose.

**2. In one sentence, not a paragraph: what problem does this system solve?** Not the technology or the features. The problem.

A warning before you answer. You gave me the purpose at the very start: "so they stop refreshing career pages and spend their time networking." That tells me what goes wrong *for the student*. I want the problem in terms of what breaks. What does refreshing career pages cost an international grad student that it doesn't cost anyone else? If you can't name that difference, this tool is a generic job alert, and generic job alerts already exist.
