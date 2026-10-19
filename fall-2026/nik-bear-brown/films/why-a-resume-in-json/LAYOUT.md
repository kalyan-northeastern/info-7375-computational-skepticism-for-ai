# Film layout: why a résumé should be a file (ai-explainer, Liam in for Bear)

Drafted 2026-10-19, rewritten from the 2026-10-18 show-tell layout after Professor Bear asked for an **ai-explainer** (the tighter single-idea film on the Claude skin), not a deep explainer. A layout, not a build: nothing is narrated, drawn or rendered. Items in [brackets] are his to confirm.

## Executive summary

**What this is.** A short ai-explainer in the series *Professor Bear Does His Assignments*: why the first file in a job search is the résumé kept as one JSON record, with every résumé and cover letter made from it. The new spine, from Professor Bear: **a résumé you keep editing in Word or Google Docs collects mistakes you never see, and AI makes that worse.** He has known students who had to defend skills they do not have, because those skills crept into their résumé without their knowing.

**The second half of the argument is flexibility.** His record is long: 20 roles and about 18,000 characters, because he has done a lot. A one-page résumé has room for a handful. With a record, the page for each opportunity, whether a job or a piece of work, is a **selection** from it: the roles and projects that matter to that opportunity, chosen without editing a document. Two different opportunities give two different pages from the same record.

**The place of the résumé among three files** (Professor Bear's framing). The résumé is **history**: the factual things you have done. The profile is **your future**: where you want to go. The gaps file is an **analysis done with data**: once we know what you have done and where you want to go, we look at real job postings to find what separates the two. The résumé must be factual because the other two are built on it, and the gaps cannot be written from a guess. In his own search the gaps file does not exist yet, on purpose: it waits for the postings (the Google and Microsoft collectors, the business-school listings) so that it is measured, not guessed.

**Why read it.** The film argues for a record, not against a tool. Edits to a document leave no mark of what was added. An AI rewrite can add a plausible detail that was never in the source (the hallucination literature is the evidence). A record read once by its owner, with every view made from it and checkable against it, is the fix.

**What the real work gives the film, all of it run or read, not staged:**
- **A real check, with a real result.** A script compared every skill on the résumé derived for the job matcher against the attested CV record. 15 skills; 14 appear in the record; **1 does not: "course development"**. The record says he "co-developed and filmed" a full Coursera course and uses "curriculum" five times, so it is probably a fair restatement, but the script cannot judge that and he has not ruled. The film shows the check finding a line nobody wrote down, and a person deciding.
- **A real selection, run on his record.** A small script suggested the roles for a one-page view for two real listings (an AI institute director at Boston College, a developer-education lead at Anthropic). Of six roles per page, three are on both pages and three on only one; 11 of his 20 roles are on neither. The suggestion is rough (it matches words), and some picks look wrong, which is the point: it suggests, he chooses.
- **A record that says what is attested and what is not**, in the same file: attested 2026-09-23; two sections added later and marked unread.
- **An artifact page** of his record (readable view, raw JSON, and the check), made 2026-10-19.

**What it must be honest about.**
- The student stories are Professor Bear's own, told as his, with no names and no details. They are not data.
- No cover letter or company-specific résumé has been made yet. The film says "can be made", never "was made".
- The hallucination claim is limited to what the survey is: a review of how language models produce content their source does not support. Its venue and year are not confirmed here (see SOURCES.md).
- **"Watermarking"** was in his note. This layout makes no claim about it, because nothing is checked here and it is not clear what he means. See the questions at the end.
- The check is literal. It finds a skill the record does not say; it cannot say whether the record is true.
- The selection script matches words. It is a suggestion tool, and the film shows a pick that looks wrong. Choosing is the owner's job.

---

## The film in one line

*A résumé you keep editing drifts, and nobody can say when a line got there. Keep one record you have read, make every résumé from it, and check the views against it.*

**Working title:** One Résumé, Many Views. [Alternative: Why a Résumé Is a File]
**Form:** `ai-explainer`; channel `claude-liam` (Liam in for Bear, Kokoro `am_onyx`, free); Teardown register; the skill's bookends and laws apply. Playlist *Professor Bear Does His Assignments*. Length about 3:15, set by the measured audio.
**Where it will be built:** `youtube/claude-liam-why-a-resume-in-json/` in this course repository (not tracked by git). `BUILD-PROMPT.md` there is the handoff.

## The central picture

One card at the centre (the record) and a ring of faded cards around it (a résumé for one company, a cover letter, a match report). In the first half the same ring is made by hand-editing one card into the next, and a line quietly changes along the chain. In the second half every outer card is made from the centre and checked against it, and the line that does not trace back lights up.

## Beats

Every body beat's `show` events are authored with the beat sheet at build time; the order and the evidence on screen are fixed here. The screen carries the evidence; the voice judges it. The Claude interface appears only in the ask beats, the verdict page, the handoff and the outro.

| Beat | Lane | What the viewer watches | Narration draft |
|---|---|---|---|
| B00 cold open | `ClaudeComposerAsk`, greeting "Hej, Liam"; answered | Composer types "Why would a résumé be a JSON file?"; two result lines land | "Hej. This is Liam, in for Bear. Why would a résumé be a JSON file? Because a résumé you keep editing drifts, and a record you keep does not." |
| B01 BLUF | `BrutalistHesitantWriter`, `lead_silence_s: 0.8`, ≥ 9 s | Types "A résumé is a document you keep editing." then strikes it and types the correction: "a record you keep, and a document made from it" | Reads the final line; one breath of stakes: what creeps into a résumé is what you will be asked to defend. |
| B02 five years of edits | C3 illustration (constructed, captioned) | Five document cards, each a copy of the last; at each hop one line changes; a counter asks "which edit?" and cannot say | "Edit a document for years and it becomes a copy of a copy. Nothing marks which line was added, by whom, or when." |
| B03 the interview | C3 illustration (constructed, captioned) | An interviewer card: "Tell me about your work with ___"; the blank is a skill on the page; a student-shaped silence | "Professor Bear has known students who had to defend skills they do not have. The skills crept into the résumé without them knowing. That is the failure." |
| B04 how it creeps | C3 + a source card | Two arrows into the same document: a person tailoring for one more application, and a rewrite by a language model. A source card names the survey (see SOURCES.md) | "Two ways in. A person tailors the résumé again. Or a tool rewrites it, and language models can add a plausible detail the source never had. Researchers have surveyed that failure. Neither edit leaves a mark." |
| B05 ask | `ClaudeComposerAsk` micro-beat, runningText `running the check…` | The actual command typed: "Check every skill on my résumé against my CV record and list any the record does not say." | "So ask a different question. Not 'does it read well', but 'does every skill trace to the record'." |
| B06 result | Onda `code-block`, real output | The real printout of the check: 15 skills, 14 found, one line flagged in the terracotta accent | "Fifteen skills. Fourteen appear in the record. One does not: course development." |
| B07 a person decides | C3, two cards side by side held ≥ 2 s | The flagged string beside the record's own line ("co-developed and filmed … a full Coursera platform course") | "The check found a line nobody wrote down. It cannot say whether it is fair. The record does say he co-developed a full course. Whether that makes it course development is the owner's call, and he has not ruled yet." |
| B08 the header | Real file contents as a card | The record's own header lines: attested, date, and the two sections marked unread | "The record carries its own status. Attested on September twenty-third. Two sections added later, marked unread. A document cannot tell you that." |
| B09 one long record, one page | C2 pattern (a funnel) + the script's real output | The record drawn as 20 role cards; for listing A six cards lift into a one-page frame, then for listing B a different six lift into a second frame; three cards sit in both; the real printout is shown beside it | "His record is long: twenty roles, because he has done a lot. A one-page résumé holds six. So the page for each opportunity is a selection from the record. Two listings, two pages, three roles in common. The script only suggests. A person decides." |
| B10 three files | C3 illustration: three cards in a row, the third computed from the first two | The résumé card labelled "history", the profile card "future", and a third card "gaps" that fills only when a stack of real postings slides in under the first two; until then it shows blank, labelled "waits for the data" | "A search has three files. The résumé is your history: what you have done, as facts. The profile is your future: where you want to go. The gaps are neither. They are an analysis, made from data: take what you have done, take where you want to go, and read real job postings to see what separates them. Professor Bear's gaps file is not written yet, because the postings are not all collected." |
| B11 many views | C2 pattern / C3 | The centre card sends arrows to a company résumé and a cover letter, drawn faded and labelled "can be made" | "Everything you send is a view of the record. A company résumé. A cover letter. None made yet. Each can be thrown away and made again." |
| B12 verdict | Artifact page | Two columns: what a record does / what it does not | "What a file does: it makes an unread change visible. What it does not: make a line true. A wrong date in the record is wrong in every view." |
| B13 handoff | `ClaudeComposerAsk`, greeting "Your turn." | The prompt typed: "Here is my résumé. Make a JSON record with one entry per job, project, degree and skill. For every skill, name the job, project or course that shows it. Mark any skill you cannot point to as unsupported, and add nothing I did not write." | Reads the prompt aloud, then discusses it: it flips the usual task, so the model has to show evidence, and the viewer should look for the word "unsupported" in the answer. |
| B14 outro | `ClaudeTitleOutro`, locked | Title restated; `@NikBearBrown` | Liam re-reads the title, then "At Nik Bear Brown." |

## Laws this layout is built around
- **Executable evidence.** B06 and B08 are real output and real file contents. Nothing is mocked.
- **Constructed means captioned.** B02 and B03 are illustrations and say so on screen, once, small.
- **No source, no verdict.** B04's claim about language models is attributed to a named source and limited to what that source is.
- **Not a slideshow.** B02, B04, B07, B09, B10 and B11 each move; none is a headline over a paragraph.

## Open questions for Professor Bear
1. **"Watermarking."** What did you mean? If it is AI-text detection or watermarks on rewritten text, say what claim you want, and I will find a source for it. Until then the film says nothing about it.
2. **The selection.** The suggester is rough and puts a Harvard Medical School course role on the Anthropic page. Keep that on screen as the reason a person chooses, or tidy it first?
3. **The flagged skill.** Is "course development" a fair restatement of the Coursera course line? The film currently says you have not ruled.
4. **B03.** Your student stories are told in your voice and attributed to you. Fine as written?
5. **The artifact page** of the record (readable view, raw JSON, check): show it in the film as the real page, or leave it out?
6. **The greeting language** (Hej) and the series order against the profile-file film.

*Written from `facts/professor-bear-cv.json`, the derived résumé in `greenhouse-watch-demo/`, `skills_trace_check.py` and its output, and this folder's log. Nothing here records a decision or understanding Professor Bear did not state.*
