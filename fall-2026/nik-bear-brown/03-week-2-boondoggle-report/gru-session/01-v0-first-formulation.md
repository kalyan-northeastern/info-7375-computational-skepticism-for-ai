# Gru turn 01-v0-first-formulation

## Professor Bear typed

```
/v0 I want to build a job-board watcher for international grad students. It checks a company's job board every day and tells the student when a new posting fits their résumé, so they stop refreshing career pages and spend their time networking instead.
```

## Gru replied (verbatim, unedited)

That's a better start than most. You've named a thing, a "job-board watcher", and not just a goal. But this is still one sentence doing three jobs. Here's what I can pull out, and what's still missing.

**What's there**
- **The thing:** a watcher that checks job boards on a schedule.
- **The trigger:** a new posting.
- **The output:** some kind of alert to the student.
- **The purpose:** less time refreshing career pages, more time networking. This is the *why*. It stays out of the /v0 sentence, and we'll need it later in /v1.

**What's missing or unclear**
1. **"Fits their résumé" is carrying the whole design and has no definition yet.** Is it keyword overlap? Similarity score? Title and seniority match? For an international grad student, the fit that decides whether applying is worth it may not be skill match at all. It may be whether the company sponsors visas, or whether the role qualifies under OPT/STEM OPT. If you build a skill matcher when your user's real filter is sponsorship, you've built the wrong thing well. I'm not settling this now. I'm naming it so it doesn't get settled by accident.
2. **"A company's job board" is singular.** One company per student? A list the student picks? Every board on one platform like Greenhouse or Workday? Each answer is a different system.
3. **"Tells the student" doesn't say how.** Email, a text, a daily digest, a dashboard? That's the output, and the /v0 sentence has to name it.

We'll close these in order. First question:

**1. What ecosystem or platform does this live inside?** Two sentences at most. Is it a standalone tool a student runs themselves, something inside a university career-services system, a feature of an existing product, or a pipeline in a course repo? This is context, not the proposal.
