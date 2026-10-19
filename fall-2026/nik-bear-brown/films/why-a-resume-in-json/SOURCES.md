# Sources and fact-check: one résumé, many views

| Claim in the film | Source | Status |
|---|---|---|
| The record is attested 2026-09-23, with two sections unread | `facts/professor-bear-cv.json` (`attested`, `attested_date`, `pending_owner_review`) | Checked against the file |
| 15 skills on the derived résumé; 14 in the record; "course development" not | `skills_trace_check.py`, run 2026-10-19; output reproduced in the artifact page | Run |
| The record says he co-developed and filmed INFO 6205 as a full Coursera course; "curriculum" appears five times | `facts/professor-bear-cv.json`, experience entry for Northeastern; the script's count | Checked against the file |
| Language models can produce content their source does not support | Ji, Lee, Frieske, Yu, Su, Xu, Ishii, Bang, Dai, Madotto, Fung, "Survey of Hallucination in Natural Language Generation", arXiv:2202.03629 (https://arxiv.org/abs/2202.03629). The survey reviews measurement and mitigation of hallucination in natural language generation across several tasks; later versions add large language models. | Existence, authors and scope confirmed from search results on 2026-10-19; **not read in full**. The journal version (ACM Computing Surveys, 2023) is from memory and not confirmed: check the ACM Digital Library before showing a venue or year on screen. |
| Students have had to defend skills they do not have because the skills crept into their résumé | Professor Bear, in chat, 2026-10-19 (his own experience) | His statement. Told as his, no names, no details, not evidence about students in general. |
| An import can promote a title or infer a skill the person lacks | The exercise's own text (Setup Exercise, step 1) | Quoted from the brief |
| "Watermarking" | none | **No claim made.** Waiting on what Professor Bear means. |
| Cover letters and company-specific résumés can be made from the record | Design of the job-search project | Stated as "can be made". None has been made. |
| His record holds 20 roles (about 18,000 characters); a one-page view holds a handful | `facts/professor-bear-cv.json`; `select_view.py` output (`select_view_output.txt`), run 2026-10-19 | Run. The page size of six is a choice made in the script. |
| Two listings give two different selections, three roles in common | `select_view.py`, using keywords taken from the real Boston College listing (faculty reader, 2026-10-18) and the Anthropic developer-education listing (Lectern run 2026-10-18) | Run. Keyword overlap is a crude selector; some picks look wrong. |
