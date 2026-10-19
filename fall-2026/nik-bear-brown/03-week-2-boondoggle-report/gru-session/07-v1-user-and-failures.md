# Gru turn 07-v1-user-and-failures

## Professor Bear typed

```
One persona, and a caveat: the personas are fictional composites, not real students, so treat the workflow part as illustrative.

Priya Nair (search/examples/priya-nair): MS Information Systems, finished December 2025. On post-completion OPT since 1 Feb 2026, STEM-eligible, 34 of 90 unemployment days used, and she wants a 20-day buffer, so about 36 usable days. Targets AI/ML engineer roles first, data engineer second; Boston or remote; needs sponsorship. Say she watches about 12 companies.

Workflow today (illustrative): bookmarks of 12 careers pages, opened most mornings, scrolled by eye, anything promising pasted into a spreadsheet. No alerts, because the board sites don't offer per-company alerts she trusts.

What goes wrong, from real runs of the tool itself rather than from Priya: on 2026-09-19 the skill was pointed at Writer's board and 51 of 51 postings came back "relevant," because words like "generative AI" appear in the company blurb on every posting, not in the job. And on a Figma run the one match for an F-1 student in Boston was a London role. So the failure I actually have evidence for is on the matching side: a checker that says everything fits is as useless as refreshing by hand.
```

## Gru replied (verbatim, unedited)

Priya works. A fictional composite is fine for this. What I need is a user specific enough to test against, and she is. I checked her numbers.

**Plausibility check on Priya's clock.** 90 − 34 = 56 days left, and with her 20-day buffer that's 36 usable days. The arithmetic is right. What doesn't add up is the calendar. She started OPT on 1 February 2026, and today is 24 September, about 235 days later. If she has used only 34 unemployment days, she has been in qualifying employment for about 200 of those days, which means her clock is probably **not running right now**. That can be true: someone in a stopgap job, still searching for the right role. But then she isn't racing a running clock. She's protecting a buffer in case the stopgap ends. It's a small detail in a fictional persona, but this document will be used for teaching, and a persona whose numbers contradict the stakes teaches the wrong urgency. Either give her a current stopgap job or make the count match the calendar. You decide which.

**Now the important part.** Your evidence changes the problem.

In /v1 question 2 you described the problem as *detection*: "no cheap way to know when a relevant posting has appeared." But detecting new postings is the easy half. Comparing today's job ids with yesterday's is simple and reliable. The real runs show the failure is in **precision**: the tool knows *that* something is new but can't tell *whether it fits*. As you said, a checker that says everything fits is as useless as refreshing by hand. Writer's 51 out of 51 isn't a weak signal. It's no signal at all.

And those are **two different failures with two different fixes**. They shouldn't be filed together:

1. **Writer, 51/51: matching on text that isn't about the job.** "Generative AI" was in the company description that repeats on every posting. That's a question of *which fields* get matched, and it makes OQ-1 more precise. The match scheme has to name which parts of a posting count (title, responsibilities, requirements) and which don't (company description, benefits, EEO statement).
2. **Figma, the London role: no concept of a hard constraint.** String matching can't catch this, because "London" isn't a skill mismatch. It's a disqualifier. You kept sponsorship out of the watcher because another layer owns it. Nobody has said who owns location.

**Open Questions Log (updated):**
- **OQ-1 (sharpened): Match scheme.** It must specify which posting fields are eligible for matching and explicitly exclude repeated company text. **Evidence:** Writer run on 2026-09-19, 51/51 false positives. Owner: you. Due: before /d1. Status: Open.
- **OQ-2: The name misleads.** Unchanged.
- **OQ-3 (new): Who owns hard constraints like location and remote-eligibility?** Options: the watcher filters on them before matching; the watcher passes them through and the scorer decides; or the student filters by hand. **Stakes:** without an owner, a student in Boston gets alerted to roles in London. **Evidence:** the Figma run. Owner: you. Due: before /v2, because it may become a principle. Status: Open.

**Before question 4, one conflict I can't absorb.** In /v0 you described this as something you're *proposing to add*. But you're citing real runs from 19 September, so the skill already exists and has produced output. That changes what this document is:

- **(a)** A retroactive SDD that describes the skill as built.
- **(b)** A corrective SDD: the design spec for fixing the skill, with today's version as the baseline and its failures as evidence.
- **(c)** A spec for a rebuild, treating the current version as a prototype to throw away.

This decides how we answer question 4 ("what does this give the user that their current solution doesn't?"). Priya's current solution might be her bookmarks, or it might be the current version of greenhouse-watch. Which is this document: a, b, or c?
