<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, published assignment text. Due date converted from the export's UTC. -->

> **Canvas assignment · 50 points · due Sun Oct 25, 2026, 11:59 PM ET**

# Final Project Pitch Film — Show What You Will Build

**Points: 50 · Due: five days from release (Canvas shows the date) · Submit: one .zip through Canvas, plus a matching GitHub folder**

> **About the syllabus.** The syllabus describes explainer videos as optional with no separate point category. **For this assignment, the film is required and graded, and this description governs.**

## What to do

Your final project is a **portfolio piece**: something a hiring manager can open and judge in a few minutes, that shows you can do the work you want to be hired for.

In five days, make a short film with [BrutalistLinks to an external site.](https://github.com/nikbearbrown/brutalist.art) that says clearly what you think that project will be.

This is a **pitch, not a build.** Nothing has to exist yet — but the film must be honest about what exists and what does not. You are not locked in: you may change your project later and log the change in `FRICTIONAL.md`.

**Length: 2–4 minutes.** Shorter is fine if the pitch is finished.

## The seven questions the film must answer

1.  **What is it?** One sentence. Then what exists when it is done — the artifact and its form (repository, app, report, dataset, agent, workflow, dashboard).
2.  **Why would anyone care — what makes it special?** This is your unique value proposition. What does it do for the person who uses it, and what makes it different from what already exists? Name one or two real alternatives you actually looked at (a tool, a template, a competitor, a manual process) and say what yours does that they do not. This project may outlive the course and become real work, so "it is an AI app" is not an answer; "it saves a \[specific person\] \[specific thing\] that \[the alternative\] does not" is.
3.  **Who opens it, and what do they do with it?** The target role and the reader (recruiter, hiring manager, engineer, or the end user). What do they do in the first sixty seconds?
4.  **What does it prove about you?** Which skills, tied to what this course teaches (prompt contracts, verification, agent loops, evaluation, source grounding). What could a reviewer fairly conclude, and what evidence will back it?
5.  **What is in, what is out, what comes first?** One thing it will deliberately not do. The first piece you will make run, and how someone would know it ran.
6.  **What could sink it?** One concrete risk specific to *this* project, and what you would do about it.
7.  **Why this project?** Why did you pick it? Is it something new you are learning, something you already know how to do and want to show off, or a mix? Say which skills are new to you and which you already have, and for the ones you already have, what you can point to as evidence. There is no wrong answer — learning and showing off are both good reasons — but be honest about which it is.

"I don't know yet, and here is how I will find out" is a complete, respectable answer. A confident answer you cannot defend is not.

## The honesty rule

Past tense only for things that exist and that you can show. Everything else is "will." Label what ran, label what is proposed, never present one as the other.

- No invented users, employers, metrics, testimonials, or results.
- Screenshots, repositories, and data samples you show are real — say when you made or got them.
- Mock-ups and sketches are labelled **constructed** on screen.
- Any Claude response you show is one you actually got, with the date.

A pitch that fabricates progress to sound ready has failed the assignment, however good it looks.

## Choosing a project

**The right size:** something a stranger can open and verify, that one person can finish, with a failure mode you can name. For example:

- a Claude Code workflow for a specific profession, with tests and an evaluation log
- a document-question-answering tool with a source-grounded test set and an honest failure analysis
- a prompt-contract library with a test harness for one domain, built on synthetic data
- a recipe for your own domain in the Reallocation Engine (you build exactly this in the next assignment, so it can be the start of your project)
- a small tool plus a write-up of where Claude's output was wrong and how you caught it

**The wrong size:** "an AI app" with no named reader · a clone with no evidence it works · anything needing private or restricted data · anything whose only value is "it is accurate" with no way to check.

**Your own data stays private.** No real résumé, contacts, application tracker, or conversation transcripts in the film or the repository. Use synthetic or public data.

Stack is your choice — name it. The course scaffolds are Python and Claude.

## Using Brutalist

git clone https://github.com/nikbearbrown/brutalist.art

Work from the toolkit's own README. **Free pipeline only** — narration and rendering run locally. No paid generation, no API keys, no media account, and no public upload is required. If your checkout includes the `show-tell` skill, it is the right format for a pitch: one simple drawn picture per beat, minimal on-screen text, narration carrying the explanation.

Run the toolkit's own quality gates and include their reports. Fix a film that fails its render-integrity check; do not submit over it.

Narrate as yourself. Do not use the instructor's name, persona, or credit line.

If Brutalist won't run on your machine, that is a legitimate `FRICTIONAL.md` entry, not an automatic loss of points. Record what you tried, what broke, and what you did instead.

## A five-day shape (a suggestion)

| Day | Do |
|----|----|
| 1 | Choose the project. Write the seven answers in `PROJECT-BRIEF.md` in plain sentences. |
| 2 | Turn the seven answers into a beat sheet: one picture, one idea per beat. |
| 3 | Build the film. |
| 4 | Run the gates. Check every claim against the honesty rule. Re-render what failed. |
| 5 | Write Frictional, assemble the folder, submit to Canvas and GitHub. |

## What to submit

Canvas file name: `LastName_FirstName_INFO7375_FinalProjectFilm.zip` GitHub folder: `fall-2026/first-name-last-initial/final-project-film/`

- `README.md` — your name, the project's working title, the target role, the runtime, and how to rebuild the film
- the rendered film (`.mp4`)
- `PROJECT-BRIEF.md` — one page answering the seven questions in text, ending with two lists: **exists today** and **will exist**
- `beat_sheet.json` — your narration and visual plan
- `BUILD-PROMPT.md` — the prompts and commands that rebuild it
- `SOURCES.md` — what you used, what you made, what Claude contributed, and any third-party asset with its licence
- the toolkit's gate reports, if it produced them
- `FRICTIONAL.md` — dated entries as you worked

Include the GitHub folder link and your final commit hash in the Canvas submission. Leave out caches, credentials, private data, and private conversation transcripts.

## Optional: share it for feedback

**Entirely optional. It earns no points and skipping it costs none.** Reviewers do not see or consider where a film was posted. Posting publicly is a separate decision from submitting. Don't post another person's private information, restricted course material, or work you don't have the right to share — and remember that once something is public it can be copied and indexed even if you delete it later.

## Grading — 50 points

| Component                              | Points |
|----------------------------------------|--------|
| The pitch                              | 30     |
| Frictional (honest log)                | 5      |
| GitHub version posting matching Canvas | 5      |
| Relative Quartile                      | 10     |
| **Total**                              | **50** |

**The pitch (30)** — what and who: one clear sentence, a named artifact, target role and reader (7) · unique value: why anyone would care, at least one real alternative named, a specific difference, no invented market or competitor claims (5) · what it proves: skills named, evidence planned, no overclaiming (5) · why this project: honest about new learning versus existing skill on show, new and existing skills separated, existing ones backed by something real (4) · scope and honest risk: in/out/first separated, a real limitation and a concrete risk, exists versus will-exist explicit (5) · shown, not asserted: pictures carry the idea, constructed material labelled, nothing presented as done that is not, the film passes its own quality checks (4)

**Relative Quartile (10)** — compares specificity, substantive improvement, demonstrated understanding, evidence, honesty about verification, usability, and professional communication across the whole comparison group. Meeting the stated requirements earns the 40 criterion-based points; it does not guarantee these 10. Top 25%: 8–10 · Second 25%: 5–7 · Third 25%: 2–4 · Bottom 25%: 0–1. The instructor and TAs review the full group before assigning it.

Production polish counts only as professional communication. **A plain, honest pitch for a modest project will outrank a beautiful one that overclaims.**

## AI use and responsibility

Read the [course AI policyLinks to an external site.](https://github.com/nikbearbrown/info-7375-prompt-engineering-for-generative-ai/blob/main/prerequisites/ai-policy.md) and watch [AI Policy for Professor Bear's Courses \| Using AI Responsibly in ClassLinks to an external site.](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz)[![](https://northeastern.instructure.com/images/play_overlay.png)](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz).

Use Claude throughout if you want — script, beat sheet, build. Name what it contributed in `SOURCES.md`.

You remain responsible for what you submit. The instructor or a TA may ask you to explain any part of the film, the brief, or the build. Not being able to explain your own submission reduces points under the relevant criteria, and misrepresenting what you verified is an academic integrity matter.
