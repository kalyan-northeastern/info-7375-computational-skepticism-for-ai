#!/usr/bin/env bash
# sync.sh — propagate the shared files from this canonical folder to the other two classes.
# Canonical master: info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/
# See SYNC.md. --check reports drift and changes nothing. Never deletes, never commits.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"   # .../nik-bear-brown (this file is lectern/ops/sync.sh)
BOOKS="$(cd "$HERE/../../.." && pwd)"                        # .../books
CHECK=0
ONLY=""      # --only <text>: sync just the class whose repo name contains <text> (e.g. --only prompt)
while [[ $# -gt 0 ]]; do
  case "$1" in
    --check) CHECK=1 ;;
    --only) ONLY="${2:?--only needs a word from the repo name}"; shift ;;
    *) echo "usage: sync.sh [--check] [--only <word in repo name>]" >&2; exit 2 ;;
  esac
  shift
done

# Shared paths, relative to the nik-bear-brown folder. Everything else is class-specific.
SHARED=(
  "lectern/lectern_paths.py"
  "lectern/collect/collect.py" "lectern/collect/faculty_feed.py" "lectern/collect/collectors"
  "lectern/publish/publish_delta.py"
  "lectern/audit/audit_rejects.py" "lectern/audit/audit_titles.py" "lectern/audit/demand_report.py"
  "lectern/config/title_families.json" "lectern/config/sources.json" "lectern/config/keywords.json" "lectern/config/faculty_config.json"
  "lectern/notes/ATS.md"
  "facts/professor-bear-cv.json"
  "SDD-job-search-project.md"
  "figma" "greenhouse-watch-demo"
)
# The master keeps these in folders (config/, collect/, publish/, audit/, notes/); the other two classes keep one flat
# folder, so each file lands there by its base name. lectern_paths.py finds config and sibling scripts in either layout.
# Where each target class keeps its copy of the collector. Branding's is its graded submission.
# (A case statement, not an associative array — macOS still ships bash 3.2.)
lectern_dir() {
  case "$1" in
    info-7375-branding-and-ai) echo "build-your-data-pipeline" ;;
    *) echo "lectern" ;;
  esac
}

drift=0
for repo in info-7375-branding-and-ai info-7375-prompt-engineering-for-generative-ai; do
  [[ -z "$ONLY" || "$repo" == *"$ONLY"* ]] || continue
  dst="$BOOKS/$repo/fall-2026/nik-bear-brown"
  [[ -d "$dst" ]] || { echo "  SKIP $repo — no nik-bear-brown folder"; continue; }
  echo "== $repo"
  for path in "${SHARED[@]}"; do
    src="$HERE/$path"
    [[ -e "$src" ]] || { echo "  MISSING IN MASTER  $path"; drift=1; continue; }
    # the collector's four files land in that class's own directory for them
    if [[ "$path" == lectern/* ]]; then
      target="$dst/$(lectern_dir "$repo")/$(basename "$path")"
    else
      target="$dst/$path"
    fi
    if [[ -d "$src" ]]; then
      if diff -rq -x '__pycache__' -x '*.pyc' "$src" "$target" >/dev/null 2>&1; then echo "  same   $path/"
      else echo "  DIFFERS $path/"; drift=1
        (( CHECK )) || { mkdir -p "$(dirname "$target")"; rsync -a --exclude='__pycache__' "$src/" "$target/"; echo "         copied"; }
      fi
    else
      if diff -q "$src" "$target" >/dev/null 2>&1; then echo "  same   $path"
      else echo "  DIFFERS $path  ->  ${target#$BOOKS/}"; drift=1
        (( CHECK )) || { mkdir -p "$(dirname "$target")"; cp "$src" "$target"; echo "         copied"; }
      fi
    fi
  done
done
echo
if (( CHECK )); then
  (( drift )) && echo "Drift found. Run without --check to copy from the master." || echo "All three in sync."
else
  echo "Done. Commit each repo by hand, with its own FRICTIONAL.md entry."
fi
