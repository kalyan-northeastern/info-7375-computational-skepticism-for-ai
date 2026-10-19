<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 25 points · NOT PUBLISHED in Canvas yet · exported due date Thu Jun 25, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

# Setup Exercise — Your Search's Personal Layer

**Course:** INFO 7375 — Computational Skepticism for AI **Type:** Standalone setup exercise (runs alongside the main assignment sequence) **Points:** 25 **Submission:** Your forked Reallocation Engine repo on GitHub; link submitted via Canvas

------------------------------------------------------------------------

## What You're Building

A `search/` folder in your Reallocation Engine fork containing three files:

- `search/resume.json` — your attested record: verified past experience, skills, credentials
- `search/profile.yml` — your target role, constraints, and search preferences
- `search/gaps.md` — the delta between your current evidence and your target role

These three files are the personal data layer that makes the engine *yours*. Without them, every score the engine produces is generic. With them, the sponsorship tier, the fit score, the timeline factor, and the Apply / Consider / Skip recommendation all operate on your actual situation. The engine's whole argument — that verified data beats fluent guessing — starts here, with your own record.

The principle this exercise runs on: **the agent does the extraction, drafting, and formatting; you do the attesting, correcting, and signing.** A file the agent built but you never questioned is not a verified record. It is fluency wearing the costume of evidence — the exact failure mode this course exists to catch.

------------------------------------------------------------------------

## Step 0 — Privacy First

Before anything else:

bash

``` code-block__code
mkdir -p search
echo "search/private-notes.md" >> .gitignore
```

Your `search/` folder will become part of your repo. One file stays out of git: `search/private-notes.md`, where honest self-assessments, raw gap admissions, and anything you would not want a recruiter to read can live safely. Everything else in `search/` is written knowing a stranger may read it.

------------------------------------------------------------------------

## Step 1 — `search/resume.json`: Extract, Then Catch the Errors

Point your agent (Cowork, Claude Code, or Claude chat) at your current resume — PDF, docx, or a LinkedIn export — and have it extract to `search/resume.json`. Each record should be structured: one entry per job, project, degree, skill, certification, or publication, with dates, titles, and verifiable details as fields rather than prose.

Then run the **attestation pass**. Your job is to find the three things the import got wrong. There will be at least three. A date that shifted. A title that got quietly promoted. A skill inferred from a course you barely passed. A project described as if you led it when you were one of five. Fix them. Then add an attestation field at the top of the file:

json

``` code-block__code
{
  "attested": true,
  "attested_date": "YYYY-MM-DD",
  "attestation_note": "Three errors corrected: [brief description]"
}
```

The attestation pass is not bureaucratic overhead. It is the course's central claim applied to your own data: **extraction is fluent; you are the source of truth.** An unattested `resume.json` is the agent's best guess about your past, dressed in JSON. An attested one is a record you can defend.

**Artifact:** `search/resume.json`, attested, with a one-line note of the three errors you caught.

------------------------------------------------------------------------

## Step 2 — `search/profile.yml`: What You Want and What Constrains You

Your agent will ask you intake questions. Answer them as facts, not aspirations:

``` code-block__code
Q1  TARGET ROLE. "In one sentence: what kind of role are you searching for?"
    Be specific enough that the engine's sponsorship scorer and fit score
    can use it. "Data scientist at a biotech startup" works.
    "Something in tech" does not.

Q2  VISA AND TIMELINE CONSTRAINTS.
    - Visa type (F-1 OPT / STEM OPT / H-1B / no constraint)
    - Authorization end date (if applicable)
    - Unemployment days already used (if on OPT)
    - STEM-eligible? (flag as uncertain if you are not sure — do not assert
      eligibility the engine will treat as a gate; confirm with your DSO)
    - Buffer target (the book recommends 80 days below the 90-day ceiling)

Q3  TARGET GEOGRAPHY. Cities or metros you can realistically work in.
    Be honest about constraints — remote preference, visa office location,
    partner or family situation. The engine filters on this.

Q4  INDUSTRY AND COMPANY PREFERENCES.
    - Sectors you are targeting (biotech, fintech, defense, etc.)
    - Company size range (seed-stage, Series A–C, public)
    - Any hard exclusions (industries you will not work in, for any reason)

Q5  SPONSORSHIP REQUIREMENT.
    Do you require employer visa sponsorship? If yes, this becomes a gate
    in the scorer — a company with no sponsorship history is skip-regardless,
    regardless of fit. State this explicitly.
```

The agent drafts `search/profile.yml` from your answers. You review it and correct anything that drifts from your actual constraints toward what sounds good. A profile that claims flexibility you do not have will produce Apply recommendations for roles you cannot take.

**Artifact:** `search/profile.yml` — target role, visa constraints with dates, geography, industry preferences, sponsorship requirement.

------------------------------------------------------------------------

## Step 3 — `search/gaps.md`: The Delta Between Your Record and Your Target

Now the agent compares your attested `resume.json` against what your target role (from `profile.yml`) actually requires, and drafts `search/gaps.md` as a table:

| Gap | Evidence the target demands it | What I have | Plan to close it |
|-----|--------------------------------|-------------|------------------|

The **evidence column** is the discipline. Every gap must be grounded in something checkable — a job posting, a BLS/O\*NET skill requirement for the SOC code, a pattern across three postings in your target sector. A gap with no evidence is a feeling, not a finding. Feelings go in `private-notes.md`.

The **plan column** is where this exercise earns its keep in this course. For each gap, the question is: what would you build, demonstrate, or publish that would close it — and how would you verify that it is closed? A gap closes only when new evidence exists: a shipped project, a published piece, a completed credential. When it closes, a new entry goes into `resume.json` and the gap row is deleted. Your `gaps.md` is a place things leave.

Your agent will draft this table. Your job is to do two edits before submitting:

1.  **Kill one wrong row.** Find one gap the agent identified that does not actually apply to your situation, and delete it. Write one sentence explaining why it was wrong.
2.  **Rewrite one row in your own words.** Take the gap that matters most to you and restate it — the evidence, what you have, the plan — in language that reflects your actual understanding of your situation, not the agent's extraction of it.

**Artifact:** `search/gaps.md`, agent-drafted, with one killed row (explained) and one row rewritten in your own words.

------------------------------------------------------------------------

## Step 4 — The Verification Check

Before submitting, run this check against your three files. Answer each question honestly in your `RUN_LOG.md` entry (Step 5):

``` code-block__code
□ resume.json: Is every job entry traceable to something verifiable
  (a LinkedIn post, a reference, an offer letter)?
  Or did the agent promote a title, extend a date, or add a skill
  you cannot defend in an interview?

□ profile.yml: Does the visa constraint section reflect your actual
  documents — or your hope for how the timeline might work out?
  If STEM eligibility is marked "yes" but you have not confirmed
  with your DSO, change it to "uncertain."

□ gaps.md: Does every gap in the evidence column cite something
  real — a posting, an O*NET requirement, a pattern you observed?
  Or did the agent invent the demand signal from its training data?
  An invented demand signal is the verified-data contract violation
  applied to your own career.
```

This check is the course's methodology applied to personal data. The same skepticism you will apply to AI systems in the research project applies here. Your own record is not exempt.

------------------------------------------------------------------------

## Step 5 — Log It

One entry in your fork's `logs/RUN_LOG.md`:

- What was built (the three files)
- The three attestation errors you caught in `resume.json`
- The top gap from `gaps.md`
- The row you killed and why
- Which field in `profile.yml` you had to correct from the agent's first draft

No contents from `search/private-notes.md` in the log.

------------------------------------------------------------------------

## Grading — 25 Points

### Mechanics — 20 Points

Each line is independently checkable. Partial completion earns partial credit.

| \# | Component | Pts |
|----|----|----|
| 1 | `search/` folder created; `private-notes.md` gitignored and confirmed | 1 |
| 2 | `resume.json` created or imported — structured records with typed fields, not pasted prose | 3 |
| 3 | Attestation pass complete: three import errors found, fixed, and noted; `attested: true` field present with date | 2 |
| 4 | `profile.yml`: target role stated specifically enough to drive the scorer; visa constraints present with actual dates or marked uncertain | 2 |
| 5 | `profile.yml`: sponsorship requirement explicitly stated as a gate or non-issue | 1 |
| 6 | `gaps.md`: drafted with evidence columns filled — every gap cites a posting, O\*NET requirement, or observed pattern | 2 |
| 7 | `gaps.md`: plan column answered for every gap with a verifiable closing condition | 2 |
| 8 | Required gap edits done: one row killed with a written reason; one row rewritten in the student's own words | 2 |
| 9 | Verification check answers present in `RUN_LOG.md` — honest responses to all three checklist items | 2 |
| 10 | `RUN_LOG.md` entry complete: three errors, top gap, killed row, corrected `profile.yml` field | 1 |
| 11 | AI Use Disclosure submitted with the assignment (see course policy) | 2 |
|  | **Mechanics total** | **20** |

### Depth — 5 Points

Graded by the TA on the quality of reasoning visible across the three files and the log. The five dimensions:

- **Specificity:** Are the target role, gap evidence, and plan concrete enough to be acted on — or are they vague enough to be comfortable?
- **Honesty:** Does the attestation note describe real errors, or does it describe trivial formatting fixes? Does the killed row have a real reason, or a diplomatic one?
- **Causal chain:** Does the gap → plan connection hold? Would the described plan actually produce evidence that closes the gap — or is it adjacent activity that feels productive?
- **Skepticism applied inward:** Did the student catch at least one place where the agent's output was fluent but wrong about their own situation?
- **Verification discipline:** Are the evidence columns in `gaps.md` grounded in something checkable, or sourced to the agent's confident inference?

| Band                                         | Pts |
|----------------------------------------------|-----|
| Top quartile of the cohort's reasoning depth | 4–5 |
| Second quartile                              | 3   |
| Third quartile                               | 2   |
| Bottom quartile                              | 0–1 |

The cap applies: if the whole cohort turns in shallow depth sections, everyone lands at 1–2. Being the least shallow in a shallow pool does not earn 4–5.

------------------------------------------------------------------------

## What Can Go Wrong

| Symptom | What it means | Fix |
|----|----|----|
| `resume.json` has no attestation errors | The agent's import was not challenged | Look harder — a title promoted by one level, a skill inferred from a course, a project date that's off by a year. They are there. |
| `profile.yml` visa section says STEM-eligible without a DSO confirmation | A gate is set on an assumption | Mark it uncertain and confirm before the engine runs on it; a wrong gate here produces Apply recommendations for roles you cannot legally take |
| Every gap in `gaps.md` lacks an evidence citation | Gaps written from feeling, not from findings | Go find three postings for your target role and mine them for skill and credential requirements; the O\*NET entry for your target SOC is also a source |
| The killed row explanation is "not relevant to me" | A reason, not a critique | Name what the agent got wrong about your situation that made it generate the gap — that is the skepticism this course is training |
| The plan column says "take a course" for every gap | Courses are inputs, not evidence | A gap closes when someone else can verify it closed — a shipped project, a published piece, a credential with an external issuer. Restate the plan as an output, not an activity |
| AI Use Disclosure says "AI drafted, I reviewed" | The disclosure describes a workflow, not a judgment | The "What the AI could not do" field requires a specific instance — one thing the agent got wrong about your situation that required your knowledge to catch |

------------------------------------------------------------------------

## A Note on Why This Exercise Exists in This Course

The Reallocation Engine is a validation pipeline for a job search. This exercise is the step that makes it personal rather than generic — and in doing so it is also the first application of the course's core methodology to a dataset you know better than any model ever will: your own record.

The attestation pass on `resume.json` is a bias audit. The evidence requirement in `gaps.md` is the verified-data contract. The profile.yml visa section is a gate definition. The killed row is a false positive you caught by applying domain knowledge the agent did not have.

These are not metaphors for the course material. They are the course material, applied to the problem of your own search. The same skepticism that catches a model's confident error on an external dataset catches the agent's confident error on your resume. The discipline is identical. The stakes, on a ninety-day OPT clock, are higher.
