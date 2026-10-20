# Targets: every company, school and research group Lectern watches, and where its data comes from

## Executive summary

**What this is.** The list of everything the job search and the research search are pointed at: companies, business schools, research institutes, hospitals, think tanks, a biotech, and the public databases behind them. Each is classified by what it is, with the direct link to where its data lives, the script that reads it (or a plain "none"), and what is still missing. **Why read it.** A target is only real if there is a way to read it. The project had grown a watch list in one file, a school list in another and a research-places list in a third, and nobody could see at a glance which targets are actually being read and which are only intentions. **What it found.** Of the targets with a reader: 14 company job boards are read and one (HubSpot) has gone dark; Google is collected but not filtered; Microsoft has never been read (it throttled), Amazon and Meta have never run here; 21 business schools are covered only through two shared job-feed searches, because most schools' own job systems cannot be read by script. Of the research places, **only one early reader exists** (`collect/collectors/biolabs.py`, built 2026-10-20 from the Biojobs repository, run on four directory pages): it finds lab links and scores each lab page for data-heavy biology, but no lab has yet been read for fit. Two targets turned out to have readable job feeds that Lectern has no reader for (Moderna on Workday, Hugging Face on Workable).

Links were checked with a plain request on 2026-10-20 (HTTP status shown in the notes where it was not 200). A page that answers a script is not the same as a page a script may read: check the site's robots file before adding a reader.

## How targets are classified

| Type | Meaning | Examples |
|---|---|---|
| **AI lab with an education product** | Builds AI and sells or runs an education product | Anthropic, OpenAI |
| **Tool company with an education program** | A product company with a real education arm (an academy, a university, an education edition) | Canva, Figma, Notion, HubSpot, Webflow, Vercel |
| **Developer-advocacy employer** | Known for paying people to teach developers | GitLab, Twilio, Netlify, Supabase |
| **Tool company, no education program yet** | Watched cheaply; the education push may come | Miro, Airtable, Jasper AI |
| **Big technology company with an education footprint** | Large incumbents with education businesses | Google, Microsoft, Amazon, Meta, Adobe, Salesforce, GitHub, Shopify |
| **University business school** | Where faculty listings about AI appear | the 21 schools below |
| **University research unit** | A department, center or lab inside a university | Harvard Medical School's Division of Nutrition, Northeastern's AI hub |
| **Research institute or think tank** | Professor Bear's broad sense: smart people on hard problems, whatever the kind (science institute, economics center, policy shop) | the Broad, the Whitehead, NBER |
| **Hospital research** | Research arms of hospitals | Boston Children's, Mass General |
| **Biotech company** | A company that does biology research for profit | Moderna |
| **Data source (not a target)** | A database the targets are read through | NIH RePORTER, NSF Award Search |

"Why it is a target" is taken from the reason recorded in the watch list or from Professor Bear's own words; where the repository gives none, the table says so. The classification is a reading, not a fact about the target.

## A. Companies read by `collect.py` (15 job boards)

The script is `lectern/collect/collect.py` with the watch list `lectern/config/sources.json`. The n8n form (`lectern/n8n/01-collect`) reads the Greenhouse and Ashby ones live and Canva not at all.

| Company | Type | Provider | Board page (people) | API the script calls (data) | Status and to-do |
|---|---|---|---|---|---|
| Anthropic | AI lab with an education product | Greenhouse | [job-boards.greenhouse.io/anthropic](https://job-boards.greenhouse.io/anthropic) | `boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true` | Reads |
| Figma | tool company with an education program | Greenhouse | [job-boards.greenhouse.io/figma](https://job-boards.greenhouse.io/figma) | `boards-api.greenhouse.io/v1/boards/figma/jobs?content=true` | Reads (API 200); the board page redirects to the company's own careers page |
| HubSpot | tool company with an education program | Greenhouse | [job-boards.greenhouse.io/hubspotjobs](https://job-boards.greenhouse.io/hubspotjobs) | `boards-api.greenhouse.io/v1/boards/hubspotjobs/jobs?content=true` | **Board returns 404 (checked 2026-10-20); it also returned 404 in the 2026-10-18 run.** No data. |
| Vercel | tool company with an education program | Greenhouse | [job-boards.greenhouse.io/vercel](https://job-boards.greenhouse.io/vercel) | `boards-api.greenhouse.io/v1/boards/vercel/jobs?content=true` | Reads |
| Webflow | tool company with an education program | Greenhouse | [job-boards.greenhouse.io/webflow](https://job-boards.greenhouse.io/webflow) | `boards-api.greenhouse.io/v1/boards/webflow/jobs?content=true` | Reads |
| Miro | tool company, no education program yet | Greenhouse | [job-boards.greenhouse.io/realtimeboardglobal](https://job-boards.greenhouse.io/realtimeboardglobal) | `boards-api.greenhouse.io/v1/boards/realtimeboardglobal/jobs?content=true` | Reads (API 200); the board page redirects to the company's own careers page |
| Airtable | tool company, no education program yet | Greenhouse | [job-boards.greenhouse.io/airtable](https://job-boards.greenhouse.io/airtable) | `boards-api.greenhouse.io/v1/boards/airtable/jobs?content=true` | Reads |
| GitLab | developer-advocacy employer | Greenhouse | [job-boards.greenhouse.io/gitlab](https://job-boards.greenhouse.io/gitlab) | `boards-api.greenhouse.io/v1/boards/gitlab/jobs?content=true` | Reads |
| Twilio | developer-advocacy employer | Greenhouse | [job-boards.greenhouse.io/twilio](https://job-boards.greenhouse.io/twilio) | `boards-api.greenhouse.io/v1/boards/twilio/jobs?content=true` | Reads |
| Netlify | developer-advocacy employer | Greenhouse | [job-boards.greenhouse.io/netlify](https://job-boards.greenhouse.io/netlify) | `boards-api.greenhouse.io/v1/boards/netlify/jobs?content=true` | Reads |
| OpenAI | AI lab with an education product | Ashby | [jobs.ashbyhq.com/openai](https://jobs.ashbyhq.com/openai) | `api.ashbyhq.com/posting-api/job-board/openai?includeCompensation=true` | Reads |
| Notion | tool company with an education program | Ashby | [jobs.ashbyhq.com/notion](https://jobs.ashbyhq.com/notion) | `api.ashbyhq.com/posting-api/job-board/notion?includeCompensation=true` | Reads |
| Jasper AI | tool company, no education program yet | Ashby | [jobs.ashbyhq.com/Jasper%20AI](https://jobs.ashbyhq.com/Jasper%20AI) | `api.ashbyhq.com/posting-api/job-board/Jasper%20AI?includeCompensation=true` | Reads |
| Supabase | developer-advocacy employer | Ashby | [jobs.ashbyhq.com/supabase](https://jobs.ashbyhq.com/supabase) | `api.ashbyhq.com/posting-api/job-board/supabase?includeCompensation=true` | Reads |
| Canva | tool company with an education program | SmartRecruiters | [careers.smartrecruiters.com/Canva](https://careers.smartrecruiters.com/Canva) | `api.smartrecruiters.com/v1/companies/Canva/postings` | Reads, but the listing has no ad text: needs one call per posting (the n8n form does not do this yet) |

Removed on his word and kept in the `removed` block of the watch list: **Stripe** and **Writer** (2026-10-18; not directly applicable to improving education through AI, and not a judgment that they are bad) and **Replit** (2026-10-19; not educational AI, just AI).

## B. Companies read by the big-four collectors (no simple feed)

Script: `lectern/collect/collectors/` (`run_daily.py`, one module per company, `monitor.py`), writing to a local database. None of it passes through the keyword filter or the daily delta yet.

| Company | Type | Data (direct link) | Status and to-do |
|---|---|---|---|
| Google | Big technology company with an education footprint (Google for Education, Classroom, Gemini for Education, NotebookLM; on the most-wanted list) | [careers results pages](https://www.google.com/about/careers/applications/jobs/results/?page=1), read from a script block in the page | **Collected in two runs on 2026-10-19 (3,690 and 3,638 postings); 3,825 distinct postings** in the local database. Not filtered, not in the delta. The page is server-rendered HTML with no official feed: a page change will break it |
| Microsoft | Same type (on the most-wanted list) | [`apply.careers.microsoft.com/api/pcsx/search`](https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&start=0) (page size fixed at 10) | **Never read.** The first runs hit HTTP 429 (the site throttles hard). A single request answers 200 today. To-do: a slower, resumable run |
| Amazon | Same type (no reason recorded in the repository; part of the "big four") | [`amazon.jobs/en/search.json`](https://www.amazon.jobs/en/search.json?base_query=&country=USA&result_limit=1&offset=0) (answers 200) | **Never run here.** To-do: run it, and write down why Amazon is a target |
| Meta | Same type (no reason recorded) | [`metacareers.com/jobs`](https://www.metacareers.com/jobs) (redirects to `/jobsearch/`), read through a real browser | **Never run here.** Needs Playwright; not covered by any test. To-do: run it, and write down why Meta is a target |

## C. Companies with no data source yet

Watched, but the three job-board systems Lectern reads (Greenhouse, Ashby, SmartRecruiters) have no board for them. Their careers pages answer, but which system they use is not recorded.

| Company | Type | Careers page (checked 2026-10-20) | What is known | To-do |
|---|---|---|---|---|
| Adobe | Big technology company with an education footprint | [careers.adobe.com](https://careers.adobe.com/us/en) (200) | Education Exchange, Creative Cloud for Education | Find its job system and write a reader |
| Salesforce | same | [salesforce.com/company/careers](https://www.salesforce.com/company/careers/) (200, redirected) | Trailhead | same |
| GitHub | same (on the most-wanted list, "maybe") | [github.careers](https://www.github.careers/careers-home) (200, redirected) | GitHub Education, Student Developer Pack | same |
| Shopify | same | [shopify.com/careers](https://www.shopify.com/careers) (200) | Shopify Academy | same |
| Hugging Face | AI company (no education reason recorded) | [apply.workable.com/huggingface](https://apply.workable.com/huggingface/) (200) | **A Workable feed that works: 6 jobs listed on 2026-10-20** via `apply.workable.com/api/v1/widget/accounts/huggingface` | A Workable reader |
| Framer | Tool company | [framer.com/careers](https://www.framer.com/careers/) (200) | none | Find its job system |
| Sketch | Tool company | [sketch.com/careers](https://www.sketch.com/careers/) (200) | none | same |
| Retool | Tool company | [retool.com/careers](https://retool.com/careers) (200) | none | same |
| InVision | Tool company | not checked | the company's status is not established here | Check whether it still hires |

## D. Business schools: 21, read only through two shared feeds

Script: `lectern/collect/faculty_feed.py` with `lectern/config/faculty_config.json`. Data: the Chronicle of Higher Education's [job feed](https://jobs.chronicle.com/jobsrss/) and Inside Higher Ed's [job feed](https://careers.insidehighered.com/jobsrss/), searched with eight AI queries plus one query per school. The reader keeps a listing only if it looks like a faculty or institute-leadership role at a business school (or a watched school) with AI in the text, and stores the rule that fired. First run: 1,727 items read, 14 matched. Output: `faculty-runs/`.

The school's own page is the better source where it can be read; the table below says which can and cannot.

**Where each school publishes open faculty positions** (all 21 links answered 200 to my plain request on 2026-10-20; the columns on system, readability and robots are from a researcher agent's plain requests the same day, spot-checked by me only for the status code). Type for every row: university business school (Brown has none; its row is the university).

| School | Faculty-jobs page (direct link) | System | Titles readable by a script? | Robots file | Notes and to-do |
|---|---|---|---|---|---|
| Harvard Business School | [hbs.edu/faculty/positions](https://www.hbs.edu/faculty/positions) | own page; applications in Interfolio | yes | allowed (crawl delay 2 s) | 7 searches for a 2027 start listed; full ads in Interfolio |
| MIT Sloan | [faculty openings](https://mitsloan.mit.edu/work-mit-sloan/mit-sloan-faculty-openings) | own page; Interfolio | yes | allowed | 7 searches listed; two say "Link TBD" |
| Duke Fuqua | [Academic Jobs Online list](https://academicjobsonline.org/ajo?joblst---31), linked from [Fuqua](https://www.fuqua.duke.edu/faculty-recruiting) | Academic Jobs Online | yes | allowed (crawl delay 5 s) | The Marketing and Operations deadlines had already passed |
| Cornell Johnson | [Cornell HR academic careers](https://apps.hr.cornell.edu/recruiting/facultycareer.cfm) | Cornell HR app | **no** (loads by script) | no robots file | University-wide, not Johnson-only |
| Vanderbilt Owen | [Provost faculty jobs board](https://www.vanderbilt.edu/provost/jobs/) | provost widget | **no** | no robots file | Shows 0 results and one 2019 item; no Owen page found |
| UCLA Anderson | [UC Recruit](https://recruit.apo.ucla.edu/apply) (Anderson's [own page](https://www.anderson.ucla.edu/faculty-and-research/open-positions) only points there) | UC Recruit | yes | allowed | 2 Anderson listings |
| UT Austin McCombs | [Faculty Careers](https://faculty.utexas.edu/career) | UT app (per a search, fed from Interfolio) | **no** (JS shell) | none found | University-wide; no McCombs page |
| UT Dallas Jindal | [PeopleAdmin faculty search](https://jobs.utdallas.edu/postings/search?query=&query_position_type_id%5B%5D=2&commit=Search) | PeopleAdmin | yes | **disallowed for all crawlers** | Do not build a reader without permission |
| Boston College Carroll | [Carroll faculty jobs](https://www.bc.edu/bc-web/schools/carroll-school/faculty-research/jobs.html) | own page; Interfolio | yes | allowed, but the PDF folder is not | Finance searches open; business analytics and accounting items look stale |
| UC San Diego Rady | [Rady open positions](https://rady.ucsd.edu/faculty-research/open-positions/) | UC Recruit | yes | allowed | 3 titles, no tenure-track search |
| UNC Kenan-Flagler | [UNC HR employment](https://hr.unc.edu/work-at-carolina/employment-opportunities/) | PeopleAdmin | pointer page only | **the PeopleAdmin host disallows crawlers** | Did not read the listings; no Kenan-Flagler page found |
| Northeastern D'Amore-McKim | [university Workday](https://northeastern.wd1.myworkdayjobs.com/en-US/careers) | Workday | **no** (JS shell; earlier research found a Cloudflare block) | allowed for /careers/ | University-wide; no school page found |
| Brown (no business school) | [Dean of the Faculty: searches](https://dof.brown.edu/searches-hiring), which says vacancies are posted on the HERC board | HERC | **no: a "confirm you are not a robot" page** | allowed, but the page is a bot check | Not attempted past the check |
| Virginia Darden | [Jobs at Darden](https://www.darden.virginia.edu/about/jobs-at-darden) | UVA's Workday (staff); Interfolio for faculty, per a search | no (staff roles only) | allowed | No faculty page found |
| Dartmouth Tuck | [faculty recruiting](https://tuck.dartmouth.edu/faculty/faculty-recruiting) | own page; Interfolio | yes | allowed (crawl delay 3 s) | "No advertised positions" |
| Rice Jones | [faculty recruitment](https://business.rice.edu/faculty-research/faculty-recruitment) | own page; Interfolio | yes | allowed | 1 open: clinical professor of finance |
| emlyon | [emlyon Workday site](https://galileo.wd3.myworkdayjobs.com/en-US/emlyon_career_site) | Workday | **no** | allowed | General careers site; whether it carries professor ads is not verified |
| IESE | [an example department page](https://www.iese.edu/faculty-research/academic-departments/accounting-control/) | department pages; Interfolio | yes (that page) | allowed | No central list; the one posting seen had expired |
| London Business School | [faculty recruitment](https://www.london.edu/faculty-and-research/faculty-recruitment) | own pages | partial (index of 7 subject pages) | allowed | Read only the accounting page: one search |
| HEC Paris | [finance department openings](https://www.hec.edu/en/faculty-research/departments/finance/finance-department-job-openings) | department pages; EconJobMarket | yes, **but stale (2023)** | allowed | No central page; its Cornerstone careers site is a JS shell |
| ESADE | [ESADE faculty jobs](https://esadefaculty.teamtailor.com/jobs) | Teamtailor | yes | allowed | "No open positions right now" |

**What this says.** Only four schools run their own page that lists real titles (HBS, MIT Sloan, Rice, Boston College). Duke is on Academic Jobs Online and UCLA and UC San Diego on UC Recruit, which are readable; one reader for each of those two systems would cover three schools. Full ad text for HBS, MIT, Boston College, Rice, Tuck, Darden and IESE sits in Interfolio, a script-built page a plain request cannot read. Two systems (UT Dallas, UNC) forbid crawlers. Seven schools give only a university-wide system, and Brown's board sits behind a bot check. Search snippets disagreed with the live pages for Tuck, ESADE and Rady, so a listing seen in a search is not a listing that is open. **To-do:** readers for Academic Jobs Online and UC Recruit and for the four school-run pages; leave the other schools on the shared feeds; never build around a robots disallow or a bot check.

## E. Research places (the part-time research search)

There is **one early reader**, `collect/collectors/biolabs.py` (seeds and rules in `config/biolabs.json`, adapted from the Biojobs repository): it checks `robots.txt`, says what it is in its User-Agent, finds lab links on a directory page, scores each lab page for data-heavy biology words and writes a local record. Run on 2026-10-20 on four directory pages: Harvard Medical School's Division of Nutrition people page, the Chan School's biostatistics page and Boston Children's labs page produced candidate lab links (the Chan page first returned degree programmes, so the filter was tightened); **the Harvard Medical School labs page answers 200 to `curl` but 404 to the reader, unresolved**; and Broad, Dana-Farber, MIT Biology and Wyss directory pages are unreadable (403 or 404). Everything else was read by hand on 2026-10-19. The design for a reader is in `lab-outreach/LAB-RECORD.md`: three stages (a department directory gives the principal investigators, each person's profile gives the lab, the lab site gives what it does and who is in it). Funding is checked at the institution level with `check-awards.py` against NIH RePORTER and the NSF Award Search (it was run for six institutions on 2026-10-19; it lives in the Prompt Engineering repository's `mode-build-assignment/scripts/funding/`, not in the master folder). Records that name people stay local.

**Universities and their units**

| Target | Type | Why | Data (direct link) | Status and to-do |
|---|---|---|---|---|
| Harvard Medical School, Division of Nutrition | University research unit | Read to design the lab record (he named endocrinology and epidemiology at Harvard Medical School; the first pilot is not chosen) | [people page](https://nutrition.hms.harvard.edu/people) (126 cards, a directory of principal investigators, not of lab members) | Read once by hand. No reader |
| Harvard Medical School (other departments) | University research unit | Epidemiology, endocrinology | [hms.harvard.edu](https://hms.harvard.edu/) | Not read; departments to choose |
| Harvard T.H. Chan School of Public Health | University research unit | Longwood; named by him | [hsph.harvard.edu](https://hsph.harvard.edu/) | Not read |
| Massachusetts College of Pharmacy and Health Sciences | University research unit | Longwood; named by him | [mcphs.edu](https://www.mcphs.edu/) | Research programmes not found |
| Northeastern: DMSB AI Strategic Hub | University research unit | Easiest to contact; his MBA school | [DASH](https://damore-mckim.northeastern.edu/dash/) | Read by hand; a great fit, posted to Discord; no pay stated |
| Northeastern: Institute for Experiential AI (AI + Life Sciences, AI + Health, AI for Finance) | University research unit | His own affiliation | [ai.northeastern.edu](https://ai.northeastern.edu/) ([Life Sciences](https://ai.northeastern.edu/life-sciences), [Health](https://ai.northeastern.edu/ai-health), [Finance](https://ai.northeastern.edu/ai-for-finance)) | Read by hand; Life Sciences posted to Discord |
| Northeastern: Center for Workforce Analytics; research collaborations; Supply Chain and Information Management; Center for Health Policy and Healthcare Research | University research units | Business-school and health-policy groups | [Workforce Analytics](https://damore-mckim.northeastern.edu/workforce-analytics/) · [collaborations](https://damore-mckim.northeastern.edu/research-collaborations/) · [Supply Chain and IM](https://damore-mckim.northeastern.edu/supply-chain/) · [CHPHR](https://chphr.northeastern.edu/) | Read by hand or in a search summary only; rated pretty good |
| Harvard Business School AI Institute | University research unit | Business research on AI | [aiinstitute.hbs.edu](https://aiinstitute.hbs.edu/) | Read in a search; location is his |
| MIT Sloan: Initiative on the Digital Economy; MIT FutureTech | University research unit | Business and economics of AI | [IDE](https://ide.mit.edu/) · [FutureTech](https://futuretech.mit.edu/) | Read in a search |
| MIT Media Lab | University research unit | Named by him, next to the Broad | [media.mit.edu](https://www.media.mit.edu/) | What it researches was not looked at |
| Harvard Graduate School of Education; MIT Open Learning | University research unit | Education; **the author's own suggestion, never checked** | [HGSE](https://www.gse.harvard.edu/) · [Open Learning](https://openlearning.mit.edu/) | Unchecked |

**Research institutes and think tanks (his broad sense)**

| Target | Type | Data (direct link) | Status and to-do |
|---|---|---|---|
| Broad Institute | Research institute (biology) | [broadinstitute.org](https://www.broadinstitute.org/) (answers scripts with 403; opens in a browser) | His record lists a Broad collaboration. Not read |
| Whitehead Institute | Research institute (biology) | [wi.mit.edu](https://wi.mit.edu/) | Address beside the Broad; not read |
| Koch, McGovern, Picower, Ragon, Wyss, Kempner institutes | Research institutes (cancer; brain; learning and memory; immunology; bioengineering; natural and artificial intelligence) | [Koch](https://ki.mit.edu/) · [McGovern](https://mcgovern.mit.edu/) · [Picower](https://picower.mit.edu/) · [Ragon](https://ragoninstitute.org/) · [Wyss](https://wyss.harvard.edu/) · [Kempner](https://kempnerinstitute.harvard.edu/) | Listed from a pasted research snapshot; not read |
| Harvard Stem Cell Institute | Research institute (biology) | [hsci.harvard.edu](https://hsci.harvard.edu/) (403 to scripts) | From the snapshot, marked unchecked there |
| NBER; Federal Reserve Bank of Boston research (with the New England Public Policy Center) | Think tank (economics) | [nber.org](https://www.nber.org/) · [bostonfed.org](https://www.bostonfed.org/) | From the snapshot; not read |
| J-PAL; Harvard Kennedy School's Center for International Development and Mossavar-Rahmani Center | Think tank (economics, policy) | [J-PAL](https://www.povertyactionlab.org/) · [CID](https://www.hks.harvard.edu/centers/cid) · [Mossavar-Rahmani](https://www.hks.harvard.edu/centers/mrcbg) | From the snapshot; not read |
| Lincoln Institute of Land Policy; Pioneer Institute; MassBudget; Massachusetts Taxpayers Foundation; Boston Municipal Research Bureau | Think tanks (land and tax policy; state policy and education; state budget; city finance) | [Lincoln](https://www.lincolninst.edu/) · [Pioneer](https://pioneerinstitute.org/) · [MassBudget](https://massbudget.org/) · [Taxpayers](https://www.masstaxpayers.org/) · [BMRB](https://www.bmrb.org/) | From the snapshot; the last two marked unchecked there |
| Berkman Klein Center | Think tank (internet, law, AI) | [cyber.harvard.edu](https://cyber.harvard.edu/) | Kept for its AI work; fellowships; not one of his five interests |
| Boston University Global Development Policy Center; Northeastern Dukakis Center | Think tanks (policy) | [BU GDP](https://www.bu.edu/gdp/) · Dukakis Center: link not verified (its address did not answer) | From the snapshot, marked unchecked |

**Hospitals**

| Target | Type | Data (direct link) | Status and to-do |
|---|---|---|---|
| Boston Children's Hospital | Hospital research | [research.childrenshospital.org](https://research.childrenshospital.org/) | Named by him; no lab directory read |
| Mass General Brigham research (Brigham and Women's, Mass General, including its computational biology center) | Hospital research | [research.massgeneralbrigham.org](https://research.massgeneralbrigham.org/) | Mass General is the farthest he will go; not read |
| Beth Israel Deaconess; Dana-Farber; Joslin | Hospital research | [BIDMC](https://bidmc.org/research) · [Dana-Farber](https://www.dana-farber.org/research) · [Joslin](https://joslin.org/) | Confirmed in the Longwood area; not read |

**Biotech company**

| Target | Type | Why | Data (direct link) | Status and to-do |
|---|---|---|---|---|
| Moderna (Research and Early Development, Data Science and AI Research, Therapeutic Area Bioinformatics) | Biotech company | A great target for AI help (his words); a pitch for a collaboration, not a job | [careers](https://www.modernatx.com/careers/life-at-moderna) · jobs feed on Workday: [page](https://modernatx.wd1.myworkdayjobs.com/M_tx) and `modernatx.wd1.myworkdayjobs.com/wday/cxs/modernatx/M_tx/jobs` (a plain POST answers: **274 postings on 2026-10-20**) | Lectern has no Workday reader. The target is a research group's page, not a job: those pages have not been found. A need for outside help is not shown by the public record |

## F. Data sources that are not targets

| Source | Used for | Direct link | Script |
|---|---|---|---|
| NIH RePORTER | Which institutions hold active research awards, by topic | [reporter.nih.gov](https://reporter.nih.gov/) (API: `api.reporter.nih.gov/v2/projects/search`, a POST) | `check-awards.py` (Prompt Engineering repository) |
| NSF Award Search | Same, for NSF | [`api.nsf.gov/services/v1/awards.json`](https://api.nsf.gov/services/v1/awards.json?printFields=id&rpp=1) | same |
| Chronicle of Higher Education, Inside Higher Ed | Faculty listings | [Chronicle](https://jobs.chronicle.com/jobsrss/) · [Inside Higher Ed](https://careers.insidehighered.com/jobsrss/) | `faculty_feed.py` |
| Greenhouse, Ashby, SmartRecruiters | Company job boards | see section A | `collect.py` |
| BLS occupational wages (national) | Role quality, a wage floor | the Reallocation Engine's compact extract, in that repository | read by hand; the local-wage script cannot run (its data is not in the repository) |

## G. Scripts and what each covers

| Script | Reads | Covers | Not covered |
|---|---|---|---|
| `lectern/collect/collect.py` | Greenhouse, Ashby, SmartRecruiters | 14 working boards | HubSpot (404); Canva has no ad text in the n8n form |
| `lectern/collect/collectors/` | Google, Microsoft, Amazon, Meta | Google (collected, unfiltered) | Microsoft (429), Amazon and Meta (never run); none passes the filter or the delta |
| `lectern/collect/faculty_feed.py` | two job feeds | 21 schools by keyword | each school's own page |
| `lectern/n8n/` (five workflows) | Greenhouse, Ashby | the same as `collect.py` minus SmartRecruiters | everything above that is not a board |
| `check-awards.py` | NIH RePORTER, NSF | institution-level funding for 6 institutions | NSF names for four of them; lab level |
| `collect/collectors/biolabs.py` | four lab directory pages | candidate lab links and a data-signal score per lab page | HMS labs page (404 to the reader), Broad, Dana-Farber, MIT Biology, Wyss; fit judgment; people and funding at lab level |

## What we do not have (the to-do list)

1. **The lab reader is a start, not a reader.** `biolabs.py` covers directory pages and a keyword score; the people-page stage, funding at lab level, the HMS labs page, and every institute, think tank and department page are still unread by script.
2. **Moderna.** A Workday reader (the feed answers), and, more important, the research group pages the pitch needs.
3. **HubSpot.** The board returned 404 on 2026-10-18 and on 2026-10-20: find where its postings moved.
4. **Microsoft, Amazon, Meta.** Never read here; and Google is collected but not filtered or part of the delta.
5. **A Workable reader** (Hugging Face answers) and **a Workday reader** (Moderna answers).
6. **Adobe, Salesforce, GitHub, Shopify, Framer, Sketch, Retool, InVision.** No job system identified.
7. **Each business school's own page**, for the schools where it can be read; the rest stay on the shared feeds. Several disallow bots or sit behind a block.
8. **A reason on record for Amazon and Meta**, and a check that each target is still worth watching.
9. **The funding check in the master folder**, and an NSF organisation-name mapping so the NSF half stops undercounting.
10. **A single machine-readable list of targets.** Today the targets are in `sources.json` (companies), `faculty_config.json` (schools) and `lab-outreach/PLACES.md` (research places), and this file is written by hand from them. A file the scripts read, with this file generated from it, would stop the two drifting.
11. **The profile does not drive the targets.** Nothing reads `profile.yml`; the lists are edited by hand to match it.

*Written 2026-10-20 from the repository's own files and the link and feed checks named above. A classification is a reading by the author of this file, not a verdict by Professor Bear, who has not reviewed it.*
