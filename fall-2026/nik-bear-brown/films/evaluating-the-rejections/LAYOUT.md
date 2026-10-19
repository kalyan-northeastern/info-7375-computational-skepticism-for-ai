# Film layout: a hundred clean reads are weak evidence

Drafted 2026-10-18. A layout, not a build: nothing is narrated, drawn or rendered. Items in [brackets] are Professor Bear's to confirm.

## Executive summary

**What this is.** A layout for a film in the series *Professor Bear Does His Assignments*, about one question: Professor Bear read a hundred random rejected job postings and found no misses. Does that mean the filter misses nothing? The film answers with arithmetic he asked for, computed by a script and shown from its output.

**Why read it.** The answer is no, and the numbers say how strongly. By his own count about five postings in the run would fit him: five in 3,446 is 0.145%, about one in 690 (he rounds it to one in 500). At that rate a hundred random reads expect 0.15 hits, and the chance of finding none is **86%** (82% at one in 500). So a clean sample is what a filter with five misses would usually produce. Zero in a hundred rules out only a miss rate above about **3%**, which is up to about 99 missed postings among 3,349 rejects. To say the rate is below one in 500 would take about **1,500** random reads, 45% of all the rejects.

**What the film recommends instead** (all from the real runs): read the risky postings in full, not a random hundred; read titles, not postings; and keep roles that own a big institutional relationship from being rejected early. The last is what Professor Bear added today and the filter now does (keywords 0.5.2).

**What it must be honest about.**
- "Five relevant" is his count, said in chat on 2026-10-18. It is an assumption in the arithmetic, not a measurement. The script takes it as a parameter.
- He says he read the file and found no misses. The file's own Verdict column is still blank, so for now that is his word and not a record. The film says so.
- The reject file's header quotes the earlier pass (3,358 rejects); the quality report says 3,349. The film uses the quality report's 3,349 and the script's output, and says the difference changes nothing at the precision shown.
- The new rule has no measured precision. Three postings is too few.

**What it does not do.** It does not claim the filter is accurate. It claims the check he ran could not have shown otherwise.

---

## The film in one line

*A test that cannot fail is not a test. A hundred random reads had an 86% chance of coming back clean even if the filter were missing postings at the base rate. Here is the arithmetic, and what to read instead.*

**Working title:** A Hundred Clean Reads Prove Less Than You Think. [Alternative: How Many Rejects Do You Have to Read?]
**Length:** about 4:00, no hard cap in the `show-tell` skill; cut beat B09 first, then merge B05 and B06.
**Form:** `show-tell`: one drawn isometric picture per beat, one to three words of label, the voice carries the idea. Liam, in for Bear; third person ("Professor Bear" throughout, as in the series); the standard greeting and the standard @NikBearBrown outro, as in the pitch film. Playlist: *Professor Bear Does His Assignments*.
**Where it will be built:** `youtube/claude-liam-show-tell-a-hundred-clean-reads/` in this course repository (the `youtube/` folder is not tracked by git). `sampling_math.py` in this folder is the numbers' source.

## The central picture

One drawing runs through the whole film.
- A bin holds the rejected cards, with a lid that opens, the same bin as the pitch film. A tray beside it holds a hundred of them.
- A handful of cards in the bin are marked in terracotta: the misses nobody has found. Five, to match the example. The number is a label, not a claim.
- A hand draws a hundred at random. The tray fills. No terracotta card lands in it. The eye wants to read that as "none in the bin". The film's job is to show why that conclusion does not follow.
- The next pictures change one thing at a time: the number of hidden cards, then the number drawn.

Every count carries a small tag naming where it came from: `quality-report-2026-09-26`, `reject-audit-2026-09-26`, `sampling_math.py` output.

## Beats (drawn from `sampling_math.py`'s own output; every spoken number is in the table below)

| Beat | Picture | Narration draft (Liam, third person) |
|---|---|---|
| BIDEA | The hesitant-writer opener; corrected question | Greeting. "Professor Bear read a hundred random rejected job postings and found no misses. Does that mean the filter misses nothing?" |
| B01 | The bin with its lid; three counters | "On September twenty-sixth the filter read three thousand four hundred and forty-six postings, kept ninety-seven and rejected three thousand three hundred and forty-nine. Every reject is saved, with its reason." |
| B02 | A hand draws a hundred cards into a tray | "So the tool drew a hundred rejects at random, a number a person can read. He says he found no misses. The Verdict column in the file is still blank, so for now that is his word, not a record." |
| B03 | Five terracotta cards among thousands | "Is none surprising? Start with the base rate. By his own count about five postings in the run would fit him. Five in three thousand four hundred and forty-six is about one in six hundred and ninety. He rounds it to one in five hundred." |
| B04 | The tray of a hundred with a sliver of a card lit | "At that rate a hundred random reads expect about a seventh of a hit. The chance of finding none is eighty-six percent. At one in five hundred it is eighty-two." |
| B05 | The same tray, five hidden cards, tray clean | "So a clean sample is the likely result even when the filter does miss at that rate. Five hidden misses, and a hundred random reads still come back clean about eighty-six times in a hundred." |
| B06 | A row of bars that shrinks as misses grow | "Here is how it changes with the real number of misses. One: you see none ninety-seven percent of the time. Five: eighty-six. Ten: seventy-four. Thirty-three: thirty-seven. A hundred: five." |
| B07 | The terminal, showing the script's real output | "So what does zero in a hundred rule out? Only a high miss rate. With ninety-five percent confidence, below about three percent. That is still up to ninety-nine missed postings. It cannot tell zero from five." |
| B08 | A number line with a point at zero and a long bracket | "The file's own estimate is the misses you find times thirty-four. Zero times thirty-four is zero. That is a point. The honest part is the bracket around it." |
| B09 | A stack of cards the height of the whole bin | "To say the rate is below one in five hundred, you would need about fifteen hundred random reads. That is nearly half the rejects. Reading postings at random is the wrong tool for a rare thing." |
| B10 | The bin sorted by a lamp: a small pile lit | "So read the right ones, not random ones. Misses are not spread evenly. Of today's three thousand two hundred and forty-three postings, fifty-seven name a university or higher education in the body. Those can all be read." |
| B11 | Titles as a short strip next to postings as a tall stack | "And read titles, not postings. There are fewer titles than postings, and a person can sort them into kinds of job in minutes." |
| B12 | A shelf of near-identical "Enterprise Account Executive" cards, all in the bin, lid open | "When he looked, thirty-eight enterprise account executive postings were rejected, for banks, retailers, carmakers. All correct. 'Educate them about our services' is a sales line, not a teaching job." |
| B13 | One card set apart: an account role reaching a university | "But there is a role worth keeping. Someone who owns a big relationship with a university, the way a partner manager owns one with a consulting firm. Not teaching. A connector." |
| B14 | The rule as a two-key gate: a title key and a body key | "So the filter now keeps a posting when the title says account, partnership, marketing or adoption, and the body names a university. Both keys. Measured first: nine hundred and ninety-two such titles, thirteen name a university, twelve were already kept." |
| B15 | The new gate with a small question mark | "It is a bet, not a result. The rule's precision is not measured, because the posting count is too small to say. A person reads what it keeps." |
| B16 | A reviewer's two columns: can conclude / cannot | "What can a reviewer conclude? That he reads his rejects, and says how strong the check was. They cannot conclude the filter misses nothing." |
| BHTF | Your Turn in the composer | "Think of a check you ran that found nothing. If the thing had been there, how likely was the check to find it?" |
| BOUT | The standard outro | Title read aloud, "At Nik Bear Brown." |

## The numbers, and where each comes from

| Spoken | Value | Source |
|---|---|---|
| Postings, kept, rejected (the sample's run) | 3,446 / 97 / 3,349 | `build-your-data-pipeline/quality-report-2026-09-26.md` (Branding repository) |
| Sample size, method | 100 uniform random, seed 20260926 | `reject-audit-2026-09-26.md` |
| "Times thirty-four" | 3,358 / 100 = 33.6 | same file, Part 1 |
| Relevant postings | about 5 | Professor Bear, chat, 2026-10-18 (an assumption) |
| Base rate | 0.145%, about 1 in 690; 1 in 500 = 0.2% | `sampling_math.py`, output 1 |
| P(no hit in 100) | 86.5% at 5 in 3,446; 81.9% at 1 in 500 | output 1 |
| P(no miss) with 1, 5, 10, 33, 100 misses | 97.0%, 85.9%, 73.8%, 36.6%, 4.6% | output 2 (exact, hypergeometric) |
| What zero rules out | below 2.95% (about 99 postings) | output 3 |
| Reads needed to bound below 1 in 500 | 1,497 (45% of rejects) | output 4 |
| Simulation check | 85.9% (200,000 samples) | output 5 |
| Postings naming a university or higher education in the body | 57 | run 2026-10-18, counted with `collect.py`'s own word matching |
| Enterprise Account Executive postings, all rejected | 38 (28 at Anthropic) | same run |
| Account/partner/marketing/sales titles; naming a university; already kept | 992; 13; 12 | same run (`keywords.json`, `connector_rule`) |

## What is cut or left out

- No claim of a filter "recall". With no known total of relevant postings there is none to quote.
- The Bayesian version (a prior on the miss rate) is left out: it adds a second assumption to explain.
- No numbers from the 2026-10-18 run for the sample itself: the sample was drawn from the 2026-09-26 run.

## Decisions for Professor Bear before a build

1. **The five.** Is "about five postings that fit me" the right count to say on screen? It drives the 86%. If the count is different, change one number in `sampling_math.py` and the film follows.
2. **One in 500 or one in 690.** The film says both. Keep both or only his rounding?
3. **His result.** The film says he found no misses and that the file's Verdict column is blank. If he fills the column in first, that line changes to the record.
4. **The close.** The Your Turn question is a draft.
5. **Whether this is the second diary film in the series** or stands alone, and whether it publishes before or after the pitch film's sample is formally filled in.

*Written from `sampling_math.py`'s real output, the 2026-09-26 reject file and quality report, and the 2026-10-18 run. Nothing here records a decision, approval or understanding that Professor Bear did not state.*
