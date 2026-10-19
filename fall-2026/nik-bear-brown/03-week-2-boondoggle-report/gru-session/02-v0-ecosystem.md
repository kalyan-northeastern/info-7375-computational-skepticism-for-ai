# Gru turn 02-v0-ecosystem

## Professor Bear typed

```
It lives inside a course repo called the Reallocation Engine, as a skill the student runs themselves from Claude Code on their own laptop (one command, optionally scheduled daily). The engine already has separate layers for visa sponsorship history and company funding, so this piece doesn't have to decide sponsorship.
```

## Gru replied (verbatim, unedited)

Question 1 is answered. Here's the ecosystem as I understand it:

> **Ecosystem:** The Reallocation Engine is a course repo of skills that students run themselves from Claude Code on their own laptops. It already has separate layers for visa sponsorship history and company funding.

That also settles half of my first flag. Sponsorship is **out of scope** for this piece, because another layer owns that decision. That's a real boundary and a good one. It leaves an open question: now that sponsorship is excluded, "fits their résumé" means skill and role fit, and we still have to define it. We'll do that in Question 3.

It also raises a new question I won't let slide. If sponsorship and funding live in other layers, does your watcher **use their output**, or does it **run beside them without knowing they exist**? Say the watcher alerts a student about a strong-fit role at a company the sponsorship layer already marked as never sponsoring. The student just lost the time this tool was supposed to save. Whether you connect to those layers or deliberately stay independent, that's a decision, and we're writing it down.

**2. What already exists in the Reallocation Engine that this piece touches, depends on, or extends?** Name specific components, not "the engine." At minimum I need:

- **The sponsorship and funding layers:** what they're called and what they output (a file, a table, a score per company), and whether the watcher reads from them.
- **The company list:** where the list of companies to watch comes from. Does the student enter it by hand, does another layer supply it, or does it come from the sponsorship or funding output?
- **The résumé:** where it lives in the repo and in what format (PDF, Markdown, structured JSON). Is it shared with other skills, or does only this one use it?
- **The scheduler:** does the engine already have a scheduling setup that "optionally scheduled daily" plugs into, or does this skill bring its own?

If some of these don't exist yet, say so. That's useful information too.
