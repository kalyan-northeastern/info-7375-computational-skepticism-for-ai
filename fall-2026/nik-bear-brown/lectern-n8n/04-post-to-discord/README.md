# 04 · Post to Discord

**What it does.** Builds the Discord messages for the new listings: only companies still on the watch list, most-wanted employers first, newly watched companies marked, nothing already posted, at most about 1,300 characters a message, ending with the line "A person decides; the machine only ranks words." A message containing a local path, an email address or a webhook URL is **refused**. The Discord node runs only if `send` is true; the default is false.

**Input:** `{new, watched, first_time_companies, already, send, date}`. **Output (one item):** `{rows, messages, sent_count, refused, posted_ids}`. An id is reported as posted only if every message went out.

**Python counterpart:** `build_messages()` and `post()` in `notify.py`. **Logic:** `shared/lib/messages.js`.

**Setup for real sending.** Create an n8n credential of type Discord Webhook with the channel's webhook URL (nothing secret is in this file), select it on the Discord node, and set `send` to true in `05 · Daily > Settings`. With no readable state, a send-on first run is refused unless `allow_first_run_post` is true, so a first run cannot post every kept listing at once.

**Tested.** Headless: rows and messages identical to the Python's; nothing sent. Real data: for 42 new listings, 30 watched rows and 5 messages, **byte-identical** to the Python's. **Not tested: the Discord node sending.** The n8n node posts plain text with link previews suppressed; the Python posts an embed with a title and colour, so the posts will look slightly different.
