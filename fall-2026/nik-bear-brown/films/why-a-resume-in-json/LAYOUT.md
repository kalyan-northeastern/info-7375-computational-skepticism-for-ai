# Film layout: why your résumé should be a file, not a document

Drafted 2026-10-18. A layout, not a build: nothing is narrated, drawn or rendered. Items in [brackets] are Professor Bear's to confirm.

## Executive summary

**What this is.** A short overview film in the series *Professor Bear Does His Assignments*: why the first file in a job search is the résumé as JSON, kept as one record, and everything else (a résumé for one company, a cover letter, a match against a posting) is made from it. It does not teach JSON syntax and it does not walk through the fields.

**Why read it.** The idea is one source of truth that its owner updates, and many disposable outputs made from it. The film also fixes a word. Professor Bear called the file "immutable" and also said it will be updated. Both cannot be true. What is true, and what the film says, is: **one record, changed only by its owner, with a date and a note on every change; everything derived from it can be thrown away and remade.**

**What the real work gives the film** (all from this folder):
- **The record exists and has a history.** `facts/professor-bear-cv.json` is his CV as fields, read and attested by him on 2026-09-23. Two sections were added on 2026-09-27 from his promotion dossier and are marked not yet read by him. The file says which parts are attested and which are not.
- **One output already comes from it.** The résumé the job-matching demo uses, `greenhouse-watch-demo/resumes/professor-bear.json`, is derived from the record, and says so, and says that its skills list (Claude's selection from the CV) has not been reviewed.
- **A match can point at the field behind it.** In the design for the job watcher, every match lists the résumé field and the posting field it rests on. That is only possible because the résumé is fields, not paragraphs.
- **The agent is not the source of truth.** The exercise's own line: extraction is fluent, you are the source of truth. The agent converted the CV; the owner read it.

**What it must be honest about.**
- **No cover letter and no company-specific résumé has been generated yet.** Those are what the file allows, not what exists. The film says "can be made", not "was made".
- **The file does not make the content true.** A wrong date in the record is wrong in every output. The film says the attestation is what stands between a typo and ten applications.
- **Personal data.** The public copy has contact details, links and other people's names removed; the film says a private copy is where those live.
- The exercise expects the owner to find at least three errors in the import. His read on 2026-09-23 found none. The film does not claim three.

---

## The film in one line

*Write your résumé once, as fields, and read it as the owner. Then every résumé and letter you send is just a view of it, and a view you can throw away.*

**Working title:** One Résumé, Many Views. [Alternative: Why a Résumé Is a File]
**Length:** about 2:30 to 3:00; brief overview, no detail on the fields.
**Form:** `show-tell`, Liam in for Bear, third person, standard greeting and @NikBearBrown outro; playlist *Professor Bear Does His Assignments*. [If you want the `lecture` skill's act structure instead, this layout carries over; it is shorter than that skill's usual film.]
**Where it will be built:** `youtube/claude-liam-show-tell-one-resume-many-views/` in this course repository (not tracked by git).

## The central picture

A single card, the record, at the centre. Arrows run out to many cards: a résumé for one company, a cover letter, a match report, a one-page version. Each outgoing card is slightly faded. Changing the central card changes all of them on the next pass, and the faded cards can be torn up without touching the middle.

## Beats

| Beat | Picture | Narration draft (Liam, third person) |
|---|---|---|
| BIDEA | Hesitant-writer opener | Greeting. "Why would a résumé be a JSON file?" |
| B01 | Five Word documents, slightly different | "Most people keep several résumés. One for each application, edited a little each time. Which is the real one?" |
| B02 | One card at the centre | "The fix is to have one. A single record of your work, written once as fields: jobs, dates, titles, degrees, skills." |
| B03 | Arrows out to faded cards | "Everything you send is made from it. A résumé for one company. A cover letter. A short version. They are views of the record, and they are disposable." |
| B04 | A tidy field next to a messy paragraph | "Why a file and not a document? Because fields can be checked. A missing date, a title in the wrong place: a program can find that. A paragraph cannot be checked at all." |
| B05 | A match line pointing to one field | "Because a match can point at its evidence. In Professor Bear's job watcher, every match lists the résumé field and the posting field it rests on." |
| B06 | A change log beside the card | "Because it has a history. The record is a file in a repository, so every change has a date and a reason." |
| B07 | The word "immutable" crossed out, replaced | "Professor Bear's first word for it was immutable. That is not quite right, because it gets updated. The right words: one record, changed only by its owner, with a date on every change." |
| B08 | An agent hand passing a card to the owner | "The agent can make the first version from your CV in minutes. That is the easy part. Extraction is fluent. You are the source of truth." |
| B09 | The owner reading with a pen; a stamp | "So the owner reads it. Professor Bear's CV file says: read on September twenty-third, accurate. Two sections added later say they have not been read yet. Attested and not attested, in the same file." |
| B10 | A derived card with a small "not reviewed" tag | "The résumé made from it for the job matcher says so too: the skills list is the agent's choice, not yet reviewed." |
| B11 | A typo travelling down every arrow | "What the file does not do is make the content true. A wrong date in the record is wrong in every output. The reading is what stops one typo from becoming ten applications." |
| B12 | A pale card: cover letter, labelled "can be made" | "What it allows, and has not yet been used for: a cover letter built from the record for one posting. Nothing here has been sent." |
| B13 | A locked private copy beside the public one | "One more thing. The public copy has no contact details, no links, no other people's names. The private copy is where those live." |
| BHTF | Your Turn in the composer | "Open your most recent résumé. List every job and date as separate lines. Which one would you not want to defend?" |
| BOUT | Standard outro | Title read aloud, "At Nik Bear Brown." |

## What is cut
- JSON syntax, field names and a tour of the record: the brief said no detail.
- Claims about ATS (applicant-tracking) parsing: not checked here.
- Any claim that a JSON résumé gets more interviews. Nothing in the project measures that.

## Decisions for Professor Bear before a build
1. **The word.** "One record, changed only by its owner" in place of "immutable": agreed?
2. **Lecture skill or show-tell**, for this film and for the profile-file film.
3. **Whether to make one cover letter or one company-specific résumé first**, so B12 can show a real output instead of saying "can be made".
4. **Order** of the two films in the series.

*Written from `facts/professor-bear-cv.json`, `greenhouse-watch-demo/resumes/professor-bear.json` and this folder's log. Nothing here records a decision or understanding Professor Bear did not state.*
