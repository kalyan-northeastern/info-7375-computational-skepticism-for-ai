# 05 · Daily

**What it does.** Runs 01, 02, 03 and 04 in order (Execute Workflow nodes), then saves the new published state and, if anything was posted, the posted ids. Two small JSON files are the memory. Trigger: manual, or a daily schedule (the workflow is inactive on import).

**Settings (one Code node).** `mode` (`fixture` or `live`), `only` (company names, empty for all), `date` (empty for today), `send` (default false), `allow_first_run_post` (default false), `state_path`, `posted_path`. Set the two paths before the first run; the committed file has placeholders.

**Behaviour, as tested.** First run: no state, every kept posting is new, state written. Same day again: refuses, because the state is not older than the run (the Python does the same). Next day with the same postings: nothing new, nothing changed, nothing gone, nothing to post, state advanced. The state is written only after the whole chain succeeded.

**Python counterpart:** `daily.sh` (collect, publish_delta, churn, faculty feed). Churn and the faculty feed are not ported yet.

**Import all five together** with `tools/import.sh`: the Execute Workflow nodes point at fixed workflow ids. Importing a workflow with an id that already exists overwrites it.

**Limits.** A state file that exists but cannot be parsed is treated like a missing one (a first run); with `send` on, that stops the run instead of posting everything. The live run was checked end to end on three small boards in dry-run mode only.
