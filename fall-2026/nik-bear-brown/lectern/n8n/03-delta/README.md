# 03 · Delta

**What it does.** Compares today's kept postings with the published state and sorts them into new, changed (title, link, place, department, matched words, or ad text) and gone. **A gone posting is only called gone if its source was readable today**: a board that was down gives "unknown", and the row stays in the state. Closed is not hired.

**Input:** `{state | null, run}` where `run` is workflow 02's output. **Output (one item):** `{new, changed, gone (each with a reason), first_time_companies, unavailable, filter_note, counts, next_state, watched, refused}`. With no state, everything is new. If the state is not older than the run it says so and `05 · Daily` stops.

**Python counterpart:** `diff()` and `write_state()` in `publish_delta.py`. **Logic:** `shared/lib/delta.js`.

**Tested.** Headless: new, changed and gone identical to the Python's on a fixture that has one of each, including a posting still on the board but no longer kept, a posting gone from the board, and a source that was down. Real data: the 2026-10-08 and 2026-10-18 runs give 42 new, 7 changed, 9 gone, identical to the Python including every reason.

**Limits.** The state uses a small non-cryptographic hash (the Code node has no crypto module by default), so it is not interchangeable with the Python's `published-state.json`. The Python's rule that a run's board counts only if it is trusted (about 30% of the last count, and two absences before closing) lives in the big-four collectors and is not ported.
