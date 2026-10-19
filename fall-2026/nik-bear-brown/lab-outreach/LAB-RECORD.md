# The lab record: what a scrape of a lab's pages should produce

Proposed 2026-10-19 after reading one real department people page and one real lab site. A design, not a scraper: nothing here has been built or run beyond those two reads. The example uses placeholders, not real people: records that name people stay on Professor Bear's machine (`lectern/.gitignore` ignores `labs/` and `lab-records/`).

## Executive summary

**What this is.** The data structure a lab scrape should end in, so that each lab answers the questions Professor Bear asked: what does the lab do, does it match what he does, who is the principal investigator, who should get the email, is there a lab manager and who.

**What the two real reads showed, and why it shapes the record.**
- **A department people page is a directory of principal investigators, not of lab members.** The Division of Nutrition at Harvard Medical School lists 126 people in one list: 121 faculty, 2 fellows, 2 staff, 1 student. No postdocs and no lab managers. Each card has a name, one to three title lines (role, department, hospital or centre), sometimes a bio snippet, a mailto and a phone link, a profile page, a Harvard Catalyst profile, and sometimes a link to the lab's own website.
- **The lab's website is a different site.** The one followed from that list redirected to the hospital's research site, built on a content system, with a "Lab Members" page one click further in, a contact page, a publications page, and no join or openings page.
- **So the scrape has three stages, and each hop changes site, robots rules and layout:** (A) the department directory gives the list of principal investigators; (B) each principal investigator's profile or lab site gives what the lab does, the publications and the contact page; (C) the lab's own people page gives the lab manager and members, when there is one.
- **Absence is a result.** The lab read had no join page, no lab manager on the front page and no funding statement. The record says "not found", it does not leave a blank, because "nobody was listed on this page" and "we did not look" are different findings.

**What it must not do.** Guess an email address from a naming pattern. Invent a lab manager. Let a model's summary pass as the lab's own words. Each of those has its own field below so the difference stays visible.

## The record (one per lab)

```json
{
  "lab_id": "hms-nutrition-<pi-surname>-<pi-firstname>",
  "kind": "lab | company_team",
  "read_at": "YYYY-MM-DD",
  "status": "read | partial | blocked | not_a_lab",

  "directory": {
    "name": "Division of Nutrition, Harvard Medical School",
    "people_page_url": "https://…/people",
    "listed_as": "Faculty | Fellow | Staff | Student",
    "titles_raw": ["Assistant Professor, Department of Medicine", "Beth Israel Deaconess Medical Center"],
    "robots_checked": true
  },

  "institution": { "school": "", "hospital_or_centre": "", "department": "" },
  "site": { "address_or_building": null, "area": "Longwood | Mass General | Cambridge (Kendall) | Allston | other", "in_range": "yes | far_end | no | unknown", "source_url": null },

  "pi": {
    "name": "",
    "title": "",
    "profile_url": "",
    "catalyst_or_external_profile_url": "",
    "lab_site_url": "",
    "email": { "value": null, "source_url": null },
    "phone": { "value": null, "source_url": null }
  },

  "what_the_lab_does": {
    "verbatim": "one sentence copied from the lab's own page, 300 characters at most",
    "source_url": "",
    "publications_url": null,
    "model_summary": null
  },

  "size_and_funding": {
    "people_listed": null,
    "pis_listed": null,
    "funding_stated": [],
    "grants_or_sponsors_named": [],
    "signal": "single_person | small | established | unknown",
    "basis": ""
  },

  "fit": {
    "basis": [
      { "my_record": "experience[11]: …", "lab_text": "…words from the lab's page…",
        "kind": "genomics | high_throughput | large_data | database_need | wants_ai_without_technical_capacity" }
    ],
    "track": "biology | business | none",
    "tier": null,
    "suggested": null,
    "verdict": null,
    "note": null
  },

  "target": {
    "is_target": null,
    "why": "has a lab website | no lab website: recorded, not a target | single person, probably unfunded | no data signal"
  },

  "people": {
    "people_page_url": null,
    "lab_manager": { "name": null, "title": null, "email": null, "source_url": null },
    "research_staff": [],
    "postdocs": [],
    "students": [],
    "counts_stated_on_page": null
  },

  "who_to_email": {
    "role": "pi | lab_manager | other",
    "name": null,
    "email": null,
    "how_chosen": "stated | inferred",
    "reason": ""
  },

  "openings": { "join_page_url": null, "says_it_is_hiring": null, "excerpt": null },
  "contact_page_url": null,

  "not_found": ["lab manager", "join or openings page", "funding statement"],

  "provenance": {
    "urls_read": [ { "url": "", "status": 200, "read_at": "" } ],
    "robots_ok": true,
    "reader": "scrape | by hand"
  },

  "outreach": { "state": "not_contacted | drafted | sent | replied | declined", "sent_on": null, "note": null,
                "page_posted_to_discord_on": null, "looked_at_by_professor_bear_on": null }
}
```

## Why each part is there

| Part | Answers his question | Rule that keeps it honest |
|---|---|---|
| `pi` | Who is the principal investigator? | Every value carries the page it came from. Email and phone only if the page published them; never constructed. |
| `what_the_lab_does` | What does the lab do? | `verbatim` is the lab's own sentence. `model_summary` is separate and empty unless one is written, so a model's words never replace the lab's. |
| `size_and_funding` | Can this lab afford me? | People and PIs counted from the pages; funding only as the lab states it. A lab of one is `single_person`: he judged that probably means no funding. "Established" needs evidence on the page (several people, named grants or sponsors), not an impression. |
| `fit` | Is it a match for what I do? | The best fit is a lab with a lot of genomic or other biological data that needs a computational biologist or a database; on the business side, a group that wants to do AI research without the technical capacity. `basis` shows which words on the page produced the suggestion. `suggested` is the tool's guess; `verdict` is his. |
| `kind` | Is it a lab or a team inside a company? | A company such as Moderna has research teams that work like labs. For a `company_team` the funding test does not apply (the company pays); what has to be recorded instead is whether the team works with outside collaborators, which a public page rarely says. |
| `site` | Can I get there? | Where the lab sits, taken from its own page, and whether that is in his range: Longwood, Harvard and Cambridge near the Broad, Allston, and Mass General at the far end, about once a week. Tufts is out. The work is mostly remote, so this is a visit, not a commute. |
| `target` | Should I write to them? | False for a faculty member with no lab website (recorded only), false for a single-person lab, false with no data signal, false when the site is out of range and the lab is not offering remote work. These are his rules, applied by the tool as a suggestion; the verdict is his. |
| `people` | Is there a lab manager, and who? | `lab_manager` is null unless a page lists one with that title. "Not found on the pages read" is recorded in `not_found`. |
| `who_to_email` | Who would get an email? | `how_chosen` says "stated" (the page names a contact for enquiries) or "inferred" (the tool chose the principal investigator by default). |
| `openings` | Is it hiring? | Null means "no page found", not "no". |
| `not_found` | What did the scrape fail to find? | Explicit, per record. |
| `provenance` | Can I check it? | Every URL read, its status and date, and whether it was read by a script or by hand. |
| `outreach` | Where am I with this lab? | Filled in by Professor Bear only. |
| `fit.tier` | Is it worth his look? | `great`, `pretty_good` or `none`, suggested from the lab's own words; he decides. `great` pages are posted to Discord; `pretty_good` only when he says so. |

## From record to Discord (Professor Bear, 2026-10-19)

A lab record with `fit.tier` of `great` becomes a candidate for `lectern/notify.py` `post_labs()`: `lab_id`, a public display name, the institution, the lab's page, the tier, the kind and `what_the_lab_does.verbatim`. Nothing else from the record leaves the machine: not the principal investigator, not the lab manager, not an email or phone. He looks at the page; `outreach.looked_at_by_professor_bear_on` is filled in by him, and no email is drafted before it is. For a `company_team` (Moderna) the page is the research group's page, not a job posting. The Northeastern question, whether it could engage him as a consultant or joint faculty for this work, is his to settle by reading his agreements, and sits in the profile as a hypothesis.

## The directory stage, as its own small record

Stage A produces one card per person, to decide which cards become labs:

```json
{ "directory_url": "", "name": "", "listed_as": "", "titles_raw": [], "profile_url": null, "lab_site_url": null,
  "catalyst_url": null, "email_on_card": null, "phone_on_card": null, "bio_snippet": null, "read_at": "" }
```

On the page read, faculty were 121 of 126 cards. A faculty card without a lab website is still a principal investigator candidate: the profile page may carry the research description.

## Reading rules (from the pages read)
- Read `robots.txt` first, per host, and skip any path it disallows. The directory page read here is allowed; its `profiles/`, `browse/` and `search/` paths are not.
- One request at a time, a few seconds apart, a plain User-Agent that names the project. No logins, no forms.
- The department RSS feed holds only the 10 most recent entries; it is not a list of everyone. The directory itself, with its "Load more", is.
- A redirect to another host starts that host's robots check again.

## Open questions for Professor Bear
1. **Answered (2026-10-19): the unit is the lab.** A faculty member with no lab website is recorded and is not a target. A lab that looks like one person probably has no funding and is not a target. Fit: computational biology and any lab with a lot of genomic or biological data, or one that could use a database; on the business side, a group that wants to do AI research without the technical capacity. The places to read: Harvard Medical School departments, the big Boston hospitals (Massachusetts General Hospital and Boston Children's Hospital named so far, others to be named), Harvard Business School, MIT Sloan, the Broad and Whitehead Institutes, and think tanks. None of those hospital sites has been read yet, so how their lab listings are laid out is not known.
2. **Still to decide: how small is too small.** Single person is clear. Is two or three people too small, or does the funding signal (named grants, sponsors) decide?
3. **Which departments first.** The Nutrition directory is 126 cards and one read; a pilot there would show how hard stage B and C are.

*Written from two real reads on 2026-10-19: the Division of Nutrition people page and its robots file, and one lab's site. Nothing here records a decision Professor Bear did not state.*
