# Plan

## Intent Summary

<One paragraph explaining the user need and the intended outcome.>

## Claim / Evidence Ledger

| Claim | Evidence | Confidence | Used By |
| --- | --- | --- | --- |
| `<fact about code/user need>` | `<file, command, log, screenshot, source>` | High / Medium / Low | `<AC or milestone>` |

Rules:
- High-confidence claims may drive implementation.
- Medium-confidence claims require validation during the relevant milestone.
- Low-confidence claims must not become implementation assumptions unless recorded as a risk or stop condition.

## Decision Log

| Decision | Reason | Alternatives Rejected |
| --- | --- | --- |
| `<decision>` | `<why>` | `<other options>` |

## Remaining Unknowns

| Unknown | Why It Remains Unknown | Required Action |
| --- | --- | --- |
| `<unknown>` | `<blocked access or implementation-dependent>` | `<runner action or stop trigger>` |

## Core Path First

Complete the shortest path to the measurable done condition before polish, broad cleanup, refactors, or optional enhancements.

Core path:
1. `<minimum implementation step>`
2. `<minimum validation step>`
3. `<minimum proof step>`

Non-core work is allowed only after the core path passes validation, unless it is required to unblock the core path.

## Gated Milestones

### M1. `<Milestone name>`

Purpose:
`<why this matters>`

Allowed write scope:
- `<paths>`

Inputs to inspect first:
- `<files/docs/tests>`

Implementation target:
- `<specific change>`

Exit gate:
- `<command, artifact, screenshot, or manual proof required>`

Evidence to record:
- `<log path, screenshot path, diff summary>`

Rollback/checkpoint:
- `<commit, checkpoint, or revert strategy>`

Do not proceed to M2 until:
- `<condition>`

## Known Failure Modes

| Failure Mode | Why It Might Happen | How To Detect | Required Response |
| --- | --- | --- | --- |
| `<fixes happy path only>` | `<risk>` | `<test/manual check>` | `<add coverage or stop>` |
| `<visual proof shows wrong state>` | `<risk>` | `<screenshot review>` | `<recapture correct state>` |
| `<unrelated files changed>` | `<risk>` | `git diff --stat` | `<revert unrelated edits>` |

## Branch, Commit, and PR Strategy

- Current branch at setup: `<branch>`
- Dirty state at setup: `<clean / dirty with notes>`
- Branch/worktree strategy: `<strategy>`
- Commit policy: `<none / milestone commits / final commit only>`
- Push/PR policy: `<requires explicit approval unless repo policy says otherwise>`

## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
