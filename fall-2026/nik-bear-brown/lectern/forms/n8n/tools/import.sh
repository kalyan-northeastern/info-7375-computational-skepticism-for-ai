#!/bin/sh
# Import the five workflows into the n8n profile this shell uses, keeping their ids so that 05 · Daily finds 01-04.
# Importing a workflow whose id already exists OVERWRITES it. Inactive on import; nothing runs.
# Before the first live run: set the paths in 05 · Daily > Settings, and create a Discord webhook credential for 04.
set -e
cd "$(dirname "$0")/.."
for d in 01-collect 02-filter 03-delta 04-post-to-discord 05-daily; do
  n8n import:workflow --input="$d/workflow.json"
done
