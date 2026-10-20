# logs/: one append-only folder per tool

## Executive summary

Each tool that runs Lectern (Muse, Grok Bot, Dots and any other) writes its own log into `logs/<tool>/`, freely, because a log that needs approval stops being a log. A log is a **self-report**: it can describe a fetch that never happened or tidy a messy run, so it is always checked against evidence the tool did not write (commit times, the Discord history, the Python's own snapshot of the same boards that day, the vendor's activity records). `compare/heartbeat.py` looks for each tool's log for today, because a tool that did not run cannot say so. Name each file with the date (`run-2026-10-21.md`) so the heartbeat can find it. Nothing here goes to the channel Professor Bear reads for judgment.
