# This folder is a copy

## Executive summary

This is the n8n form of Lectern, kept inside the Lectern folder (`lectern/forms/n8n/`), beside the Python form so the two can be read, run and compared side by side: same pipeline, two ways of building it, one tested against the other. It is a copy of the folder published on its own as `lectern-job-search` in the `nikbearbrown/N8N` repository. If the two differ, check `git log` in each; neither is refreshed automatically. A CrewAI form is planned and would sit beside it as `lectern/forms/crewai-flow/` and `crewai-crew/`.

Because it sits inside `lectern/`, the tools in `tools/` find the Python by default:

```bash
python3 tools/test_headless.py                       # all five workflows, in a disposable n8n profile; nothing sent
python3 tools/parity_delta.py --earlier ../../runs/2026-10-08 --later ../../runs/2026-10-18
```

The real-data parity tests need saved board payloads, which are not tracked (full copies of companies' ads); see `README.md`.
