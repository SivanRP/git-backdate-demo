#!/usr/bin/env bash
# Make a commit with a fake date.
# Usage: ./backdate.sh "2026-10-15T14:00:00" "commit message"
set -euo pipefail
DATE="$1"; MSG="$2"
GIT_AUTHOR_DATE="$DATE" GIT_COMMITTER_DATE="$DATE" git commit -m "$MSG"
# Both timestamps are set by the client. Git never checks them against a clock.
