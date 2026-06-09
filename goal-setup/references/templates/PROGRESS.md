# Progress Log

Keep this append-only below the current status block. Update `STATE.md` after each meaningful change, validation run, blocker, or context-compaction risk.

## Current Status Mirror

- Current verdict: `<mirror STATE.md in one line>`
- Next best action: `<mirror STATE.md in one line>`
- Latest evidence: `<path or summary>`

## Setup-Time Discovery

| Item | Result | Evidence |
| --- | --- | --- |
| Git status | `<clean/dirty>` | `<command output summary>` |
| Baseline checks | `<not run/pass/fail>` | `<log path>` |
| Relevant docs/code read | `<summary>` | `<paths>` |

## Progress Entries

### <timestamp> - Packet created

- Files created:
  - `GOAL.md`
  - `PLAN.md`
  - `CONSTRAINTS.md`
  - `CHECKS.md`
  - `STATE.md`
- Assumptions:
  - `<assumption>`
- Unchecked validation:
  - `<check>`

### <timestamp> - Baseline captured

- Command summary:
- Result:
- Evidence path:
- Pre-existing failures:

### <timestamp> - Milestone update

- Milestone:
- Changes made:
- Validation:
- Evidence:
- Blockers:
- Next action:

## Final Outcome

Do not complete this section until final validation is done.

- Final verdict:
- Fresh evidence summary:
- Residual risks:
- User-confirmed completion:
- Archive path if moved:

## Context Compression Rules

When context gets long, preserve these first:

1. Current `STATE.md`
2. Acceptance criteria and latest evidence
3. Active blockers
4. Files touched and why
5. Next best action

Append historical detail below the current status snapshot. Do not bury the next action inside old logs.

## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
