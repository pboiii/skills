# <Goal Title>

Created: <YYYY-MM-DD>
Lifecycle location: `docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/`
Target runner: Codex
Packet size: <Lean / Standard / Full>

## Objective

Complete `<approved work>` until `<measurable end state>` is proven without violating `<key constraints>`.

## Read First

1. `STATE.md`
2. `PLAN.md` if present
3. `CONSTRAINTS.md` if present
4. `CHECKS.md`
5. `PROGRESS.md`
6. Relevant repo instructions and source files listed below

## Goal Pack Contract

- `GOAL.md` is the compact charter.
- `PLAN.md` is the milestone and sequencing source of truth.
- `CONSTRAINTS.md` is the write-scope, decision, safety, and stop-condition contract.
- `CHECKS.md` is the validation and completion-audit contract.
- `STATE.md` is the current resume capsule and must stay short.
- `PROGRESS.md` is the append-only evidence and decision log.

## Acceptance Criteria

| ID | Criterion | Evidence Required |
| --- | --- | --- |
| AC-001 | `<observable result>` | `<command/log/screenshot/artifact>` |
| AC-002 | `<observable result>` | `<command/log/screenshot/artifact>` |

## Required Final Proof

The goal is complete only when every acceptance criterion maps to fresh post-change evidence in `CHECKS.md`, `STATE.md` reflects final status, and `PROGRESS.md` records the final validation outcome.

## Stop / Report Conditions

Stop and report instead of guessing when any of these occur:

- Required credentials, approvals, or external access are unavailable.
- A decision would change product behavior, security, data deletion, public API contracts, billing, notifications, or external sends.
- Required validation fails twice for the same unresolved reason.
- The run reaches `<N turns / time budget / token budget>`.
- Work would exceed the allowed write scope or safety boundaries.

## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
