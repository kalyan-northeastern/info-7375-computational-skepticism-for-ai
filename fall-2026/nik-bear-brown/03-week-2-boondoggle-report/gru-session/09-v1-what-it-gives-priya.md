# Gru turn 09-v1-what-it-gives-priya

## Professor Bear typed

```
Next to the bookmarks: memory plus cited reasons. Scanning 12 pages by eye, she can't reliably tell a posting that went up last night from one she dismissed three weeks ago; the watcher diffs by job id against what it saw last run, so "new" is a fact, not an impression. And each match carries the résumé field and posting field behind it, so she can check the claim in seconds instead of rereading the ad. A cron job and curl give her neither.

Next to today's greenhouse-watch, two things:
1. A match count she can trust, because matching runs only on the job's own text, not the company description repeated on every posting. Today a board like Writer's says everything fits.
2. No quiet location surprises. Location is handled as a stated rule the report shows, whatever we decide in OQ-3, instead of a soft penalty a strong skill score can bury.
```

## Gru replied (verbatim, unedited)

Accepted at both levels. "Memory plus cited reasons" is specific, and a cron job with `curl` really does give her neither. The two corrective claims are the document's reason to exist. I'm writing them into the Problem Summary almost as you wrote them. Three plausibility notes first, because each claim is a little stronger than what the build can guarantee right now.

**1. "New is a fact" is a fact about job ids, not about jobs.** Diffing ids tells you an *id* is new. Two ordinary cases break the connection between ids and jobs:
- **Reposts.** A company takes down a posting and puts it back up with a fresh id. The watcher reports it as new, and Priya sees again a role she already dismissed. That's the three-weeks-ago problem you just said the tool solves.
- **Memory of only the last run.** Your /v0 sentence says the watcher remembers the ids it saw *last run*. A posting that disappears for one run and comes back looks new again. And if Priya skips a week, "new since last run" and "new since she last looked" are no longer the same thing.

Neither case undermines the claim. They set its limits. Both are logged for /s4, and the report's wording should say "new since last run," not "new."

**2. "Only the job's own text" assumes the boards separate that text for you. On many of them, they don't.** On a lot of boards, the company's "About us" paragraph is inside the same description as the job, not in a separate field. If that's true on Greenhouse, Ashby, or SmartRecruiters, then fixing Writer isn't a matter of *choosing the right field*. It's a matter of *splitting the text into sections*, which means heuristics, and heuristics fail differently on each board. That's the difference between a config change and a design problem, and it's the biggest risk to your first corrective claim. You need to check it on real payloads from all three platforms before /d1. I'm logging it as its own open question, because it decides how big OQ-1 is.

**3. "A match count she can trust" isn't testable yet.** Writer at 51/51 is clearly broken. But what does "trustworthy" look like as a number? You don't have to answer now. In /v4 this becomes a Need, and a Need needs a pass/fail condition. For example: on a board with a known set of relevant roles, precision is at or above some level you name, and no false positive comes from company boilerplate. Start thinking about which board and which labeled set you'd test against.

The second claim, **"location as a stated rule the report shows,"** holds no matter how OQ-3 is decided. I'm accepting it as written. It's the stronger of the two, because it doesn't depend on any heuristic working.

**Open Questions Log (additions):**
- **OQ-5 (new): Do the three platforms separate job text from company text?** For each of Greenhouse, Ashby, and SmartRecruiters: is the company description a separate field, or is it inside the job description? **Stakes:** if it's inside, corrective claim 1 needs text segmentation, which turns a config fix into a design problem. **Blocks:** OQ-1. Owner: you. Due: before /d1. Status: Open.
- **Deferred to /s4:** reposts with new ids; ids that disappear and come back; skipped runs, where "new since last run" differs from "new since she last looked"; first run (already logged).

**5. Category.** I'm carrying this forward from /v0 as *a local CLI skill that polls and notifies*. With the corrective framing it's more precise to call it *a local, scheduled change-detector with a scored, explainable filter*. Correct me if that's wrong. Otherwise it stands and we go on.

**6. What is the deployment target, and why?** I know the target: the student's own laptop, run through Claude Code, scheduled optionally with launchd, cron, or a GitHub Action. What I don't know is **why**. Specifically:
- **Why local and not hosted?** A hosted service could run daily with nothing on Priya's end. What does running on her own machine protect? Her résumé JSON is gitignored for a reason, so is privacy the reason, or cost, or course pedagogy?
- **Why through Claude Code?** Does the Claude part of the skill do any work at runtime, or is Claude Code only how it gets launched? If matching is a deterministic scheme and diffing is deterministic, then every scheduled run may not need Claude at all. That affects cost, reliability, and what happens when a GitHub Action runs it headless.
