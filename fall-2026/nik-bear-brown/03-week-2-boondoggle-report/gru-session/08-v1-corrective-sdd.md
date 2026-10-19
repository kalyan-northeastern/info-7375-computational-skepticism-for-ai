# Gru turn 08-v1-corrective-sdd

## Professor Bear typed

```
(b), a corrective SDD. The skill exists and has run on real boards; today's version is the baseline and its failures are the evidence. And Priya's current solution for question 4 is her bookmarks, with today's greenhouse-watch as the thing being corrected.

Priya's calendar: you're right, the numbers don't fit a running clock. For this document she's in a stopgap job and protecting her buffer. The persona file in the engine repo still has the inconsistency; log it as an open question there rather than me editing it here.

On OQ-3, a fact you don't have yet: the current scheme file already has a location rule. location_mode is "soft" by default, which subtracts 1 point for a location miss instead of excluding the posting; it can be set to "hard" to make location a gate. So the watcher does own location today. The London match got through because the default is soft and the skill score outweighed the penalty. The real question is whether soft should be the default.
```

## Gru replied (verbatim, unedited)

Understood: this is a **corrective SDD**. Today's greenhouse-watch is the baseline, and its failures are the evidence. That framing is now fixed for every section after this one.

Your fact about OQ-3 changes it, and it also changes OQ-1. So I'm correcting my own log before we continue.

**Correction to OQ-1.** I've been treating the match scheme as undefined. It isn't. A scheme file already exists and has at least one real rule (`location_mode`). So the question isn't "define the scheme." It's "fix the scheme where it's wrong." Also, the scheme scores postings and subtracts points, so "match" really means **the score meets a threshold**, not a yes/no string match. Your /v0 sentence ("match the résumé under a written string-match scheme") is still accurate at that level of detail, so I'm not reopening /v0. But from here on, "match" in this document means *meets the threshold under the scheme*, and /d1 has to define the threshold.

**On OQ-3, a push before I rewrite it.** You've framed it as "should soft be the default?" That's the right question, but you can't answer it with soft versus hard alone. It depends on what each kind of error costs Priya:

- **Soft default, when it's wrong:** a London role gets through. Cost: about two minutes of Priya's attention, plus some loss of trust in the tool. The Writer run showed that once trust is gone, she's back to checking bookmarks.
- **Hard default, when it's wrong:** a role that's actually open to her gets dropped without her knowing. For example, a posting listed as "New York, NY" whose description says remote is fine, or a posting that lists five cities with Boston fifth. Cost: a missed application, which she never finds out about. Silent misses are worse than visible noise, because she can't catch them.

So whether a hard gate is safe depends on **how reliable the location field is on each of the three platforms**. That's a data question, not a preference. I'm writing it into the log that way.

**Open Questions Log (revised):**
- **Document type:** Corrective SDD. Baseline = today's greenhouse-watch. Evidence = real runs.
- **OQ-1 (revised): Fields the scheme matches on.** The scheme file exists. The gap is which posting fields count. It must exclude repeated company text. **Evidence:** Writer run on 2026-09-19, 51/51. It must also define the match threshold. Owner: you. Due: before /d1. Status: Open.
- **OQ-2: The name misleads.** Unchanged.
- **OQ-3 (reframed): Should `location_mode` default to soft or hard?** **Evidence:** the Figma run. Soft let a London role through for a student in Boston because the skill score outweighed the −1 penalty. **Blocking data:** how reliable the posting location field is on Greenhouse, Ashby, and SmartRecruiters (multi-city listings, "remote" written only in the description). Options: hard by default; soft with a larger penalty; hard, with remote detected from the description; or the student sets it on first run. Owner: you. Due: before /v2. Status: Open.
- **OQ-4 (new, in the engine repo): The `priya-nair` persona file is inconsistent.** It says 34 of 90 days used with an OPT start of 1 Feb 2026, which doesn't match a running clock. The decision for this document: she's in a stopgap job and protecting her buffer. Fix it in the repo, not here. Owner: you. Status: Open.

**4. What does this give Priya that her current solution doesn't?** Her current solution is 12 bookmarks, opened most mornings and scanned by eye, with a spreadsheet.

Answer at two levels:
- **Next to the bookmarks:** what she gets from the corrected watcher that she can't get from checking by hand. If your answer is "it combines X and Y," name what's actually new in the combination. "It's automatic" isn't enough, because a cron job and `curl` are automatic too.
- **Next to today's greenhouse-watch:** what the corrected version gives her that the current version doesn't. That's this document's reason to exist, and it should be one or two concrete things, not a list of fixes.
