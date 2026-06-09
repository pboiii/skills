#!/usr/bin/env bash
# goal-check.sh
# Runnable validation harness for a generated goal packet.
# Usage:
#   bash ./goal-check.sh baseline
#   bash ./goal-check.sh milestone-M1
#   bash ./goal-check.sh final
#
# Command config:
#   ./checks/commands.txt
# Format per non-comment line:
#   id|required|command
#   id|optional|command
# Example:
#   lint|required|npm run lint
#   test|required|npm test
#   build|optional|npm run build

set -uo pipefail

PHASE="${1:-manual}"
SCRIPT_PATH="${BASH_SOURCE[0]}"
GOAL_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
CHECK_DIR="$GOAL_DIR/checks"
PROOF_DIR="$GOAL_DIR/proof"
LOG_DIR="$PROOF_DIR/logs"
COMMANDS_FILE="${GOAL_COMMANDS_FILE:-$CHECK_DIR/commands.txt}"
STAMP="$(date +"%Y%m%d-%H%M%S")"
SUMMARY="$LOG_DIR/${STAMP}-${PHASE}-summary.md"
LATEST="$LOG_DIR/latest-summary.md"
FAILURES=0
REQUIRED_FAILURES=0
RUN_COUNT=0

mkdir -p "$LOG_DIR"

safe_name() {
  printf '%s' "$1" | tr -cs 'A-Za-z0-9._-' '-'
}

append() {
  printf '%s\n' "$*" | tee -a "$SUMMARY" >/dev/null
}

rel_path() {
  local path="$1"
  case "$path" in
    "$GOAL_DIR"/*) printf '%s\n' "${path#"$GOAL_DIR"/}" ;;
    "$GOAL_DIR") printf '%s\n' "." ;;
    *) printf '%s\n' "$path" ;;
  esac
}

print_header() {
  append "# Goal Check Summary"
  append ""
  append "- Phase: $PHASE"
  append "- Started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  append "- Goal dir: ."
  append "- Commands file: $(rel_path "$COMMANDS_FILE")"
  append ""
}

run_one() {
  local id="$1"
  local requiredness="$2"
  local command="$3"
  local slug
  slug="$(safe_name "$id")"
  local log_file="$LOG_DIR/${STAMP}-${PHASE}-${slug}.log"
  local start_time end_time status exit_code
  start_time="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

  RUN_COUNT=$((RUN_COUNT + 1))

  append "## $id"
  append ""
  append "- Requiredness: $requiredness"
  append "- Started: $start_time"
  append "- Log: $(rel_path "$log_file")"
  append ""
  append '```bash'
  append "$command"
  append '```'
  append ""

  (
    if repo_root="$(git -C "$GOAL_DIR" rev-parse --show-toplevel 2>/dev/null)"; then
      cd "$repo_root"
    else
      cd "$GOAL_DIR"
    fi
    bash -lc "$command"
  ) >"$log_file" 2>&1
  exit_code=$?
  end_time="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

  if [[ "$exit_code" -eq 0 ]]; then
    status="PASS"
  else
    status="FAIL"
    FAILURES=$((FAILURES + 1))
    if [[ "$requiredness" == "required" ]]; then
      REQUIRED_FAILURES=$((REQUIRED_FAILURES + 1))
    fi
  fi

  append "- Finished: $end_time"
  append "- Exit code: $exit_code"
  append "- Status: $status"

  if [[ "$exit_code" -ne 0 ]]; then
    append ""
    append "Last 80 log lines:"
    append ""
    append '```text'
    tail -80 "$log_file" | tee -a "$SUMMARY" >/dev/null
    append '```'
  fi

  append ""
}

validate_config() {
  if [[ ! -f "$COMMANDS_FILE" ]]; then
    print_header
    append "No commands file found. Create $COMMANDS_FILE with lines like:"
    append ""
    append '```text'
    append "lint|required|npm run lint"
    append "test|required|npm test"
    append "build|optional|npm run build"
    append '```'
    cp "$SUMMARY" "$LATEST"
    return 2
  fi
}

main() {
  validate_config || exit $?
  print_header

  while IFS= read -r raw_line || [[ -n "$raw_line" ]]; do
    line="${raw_line#"${raw_line%%[![:space:]]*}"}"
    line="${line%"${line##*[![:space:]]}"}"

    [[ -z "$line" ]] && continue
    [[ "$line" == \#* ]] && continue

    IFS='|' read -r id requiredness command <<<"$line"

    id="${id:-unnamed}"
    requiredness="${requiredness:-required}"
    command="${command:-}"

    if [[ -z "$command" ]]; then
      append "Skipping malformed command line: $raw_line"
      continue
    fi

    if [[ "$requiredness" != "required" && "$requiredness" != "optional" ]]; then
      requiredness="required"
    fi

    run_one "$id" "$requiredness" "$command"
  done <"$COMMANDS_FILE"

  append "# Final Summary"
  append ""
  append "- Phase: $PHASE"
  append "- Commands run: $RUN_COUNT"
  append "- Total failures: $FAILURES"
  append "- Required failures: $REQUIRED_FAILURES"
  append "- Summary: $(rel_path "$SUMMARY")"

  cp "$SUMMARY" "$LATEST"

  if [[ "$REQUIRED_FAILURES" -ne 0 ]]; then
    exit 1
  fi

  exit 0
}

main "$@"
