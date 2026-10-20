# 01 · Collect

**What it does.** Reads each watched board and turns the three providers' different record formats (Greenhouse, Ashby, SmartRecruiters) into one shape. **Fixture mode** (default) replays three made-up payloads; **live mode** calls the public job-board APIs. A board that fails becomes a status row (`unavailable` with the reason), never a stop; if every board fails the workflow errors, as the Python does.

**Output (one item):** `{date, mode, sources: [{company, provider, status, postings | reason}], watched: [companies], views: [normalised postings]}`. The source's own raw record is not carried forward.

**Python counterpart:** `fetch_board()` and `normalise()` in `collect.py`. **Logic:** `shared/lib/normalise.js`.

**Tested.** Headless on the synthetic payloads: every normalised posting identical to the Python's. Live: Netlify, Airtable (Greenhouse) and Jasper AI (Ashby), run in n8n and in the Python seconds apart, identical on every field. A made-up board that returns 404 becomes an `unavailable` row.

**Limits.** SmartRecruiters is not read live (it needs one call per posting for the ad text); it is reported as unavailable instead of being judged on empty text. The HTML-entity decoder covers the common named entities and all numeric ones, not all of HTML5; on 2,465 real postings that made no difference.

**Run on its own:** import `workflow.json`, press Manual. Change the Fixture input node to `{mode: 'live', only: ['Netlify']}` to read a real board.
