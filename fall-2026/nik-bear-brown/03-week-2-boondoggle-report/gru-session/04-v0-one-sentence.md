# Gru turn 04-v0-one-sentence

## Professor Bear typed

```
greenhouse-watch is a Claude Code skill inserted at the front of the Reallocation Engine, reading one company's public job board and the student's résumé JSON and remembering which job ids it saw last run, that produces a notice, not a verdict: a Markdown report and a JSON log listing only the postings new since the last run that match the résumé under a written string-match scheme, each with the résumé field and posting field behind every match.
```

## Gru replied (verbatim, unedited)

That sentence works. It names the thing (a Claude Code skill), what it reads (one public board, the résumé JSON, and its own record of the job ids it saw last run), and what it produces (a Markdown report and a JSON log of new matching postings, with the evidence behind each match). "A notice, not a verdict" answers the scorer question directly. You can now test the output: a reviewer could hold a report and say whether it's right or wrong.

I'm not confirming it yet. Two phrases in it contradict what you told me earlier, and one term needs to be logged.

**1. The name doesn't match the scope.** You told me the student names a board on **Greenhouse, Ashby, or SmartRecruiters**. The skill is called **greenhouse-watch**. Either it supports only Greenhouse, and the other two are out of scope, or it supports all three and the name will mislead every student who reads the skill list. I'm not being fussy about naming here. A student with an Ashby company will read the name, assume it won't work for them, and never run it. Which is it?

**2. "At the front of the Reallocation Engine" contradicts "runs beside."** "The front" suggests a pipeline where the watcher's output flows into the next stage, which is `role-scorer.mjs`. Two answers ago you said the watcher doesn't feed the scorer and runs beside it. If "front" means the first thing a student runs, the entry point to the engine, say that. If it means an upstream stage, then you've quietly decided to feed the scorer, and that needs to be a decision you made on purpose. Pick the words that match what's true today.

**3. "A written string-match scheme" is a promise I'm logging, not a blocker.** The sentence says the scheme will be written down. It doesn't say what it is: which résumé fields, which posting fields, exact or case-folded matching, whole words or substrings, and what counts as a match. That gets settled in /v1 and /d1. I'm adding it now as the first item in the Open Questions Log so nobody takes "string match" as already decided.

(One more for later, not a blocker. On the first run there are no saved ids, so by your own definition every posting is "new." That goes in /s4.)

Here's the draft summary with your sentence exactly as written:

---
**V0 SUMMARY (DRAFT, not confirmed)**

**Ecosystem:** The Reallocation Engine is a course repo of skills that students run themselves from Claude Code on their own laptops. It already has sponsorship (DOL/H-1B) and funding (SEC Form D) layers that feed a composite role scorer.

**Existing components touched:** Public job boards on Greenhouse, Ashby, and SmartRecruiters (read-only, one slug per run). `search/resume.json` (gitignored and shared; committed examples in `search/examples/`). The student's own scheduler. The watcher deliberately does **not** touch `data/80-days-to-stay/`, `data/sec/form-d/`, or `scripts/score/role-scorer.mjs`.

**Proposal:** "greenhouse-watch is a Claude Code skill inserted at the front of the Reallocation Engine, reading one company's public job board and the student's résumé JSON and remembering which job ids it saw last run, that produces a notice, not a verdict: a Markdown report and a JSON log listing only the postings new since the last run that match the résumé under a written string-match scheme, each with the résumé field and posting field behind every match."

**Open item carried forward:** OQ-1. Define the string-match scheme (fields, normalization, match rule). Owner: you. Due: before /d1.

---

Fix items 1 and 2 in the sentence yourself, or tell me why the current wording is correct. Then confirm, and we move to /v1.
