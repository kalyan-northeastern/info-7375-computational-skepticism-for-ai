#!/usr/bin/env bash
# sync.sh — propagate the shared files from this canonical folder to the other two classes.
# Canonical master: info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/
# See SYNC.md. --check reports drift and changes nothing. Never deletes, never commits.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"     # .../nik-bear-brown
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
  "lectern/collect.py" "lectern/audit_rejects.py" "lectern/audit_titles.py" "lectern/demand_report.py" "lectern/title_families.json" "lectern/sources.json" "lectern/keywords.json" "lectern/ATS.md" "lectern/faculty_feed.py" "lectern/faculty_config.json" "lectern/collectors" "lectern/publish_delta.py"
  "facts/professor-bear-cv.json"
  "SDD-job-search-project.md"
  "figma" "greenhouse-watch-demo"
)
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
