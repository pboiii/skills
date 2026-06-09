# Constraints

## Allowed Write Scope

- `<path or module>`

## Out of Scope

- `<explicit non-goal>`

## Banned or Approval-Gated Operations

The runner must not perform these without explicit user approval or documented repo policy:

- Push branches, open PRs, deploy, publish packages, or write to production.
- Delete user data, run destructive migrations, or mutate external services.
- Send emails, notifications, payments, messages, or other external effects.
- Add dependencies or change lockfiles unless required by the approved objective.
- Stage, commit, or revert unrelated user changes.

## Decision Budget

The runner may decide:

- implementation details that preserve documented behavior
- naming consistent with repo conventions
- test placement following existing patterns
- minor copy only when acceptance criteria define intent

The runner must stop/report for:

- product behavior tradeoffs
- data deletion or migration ambiguity
- permission or security model changes
- pricing, billing, email, notification, or external-send behavior
- public API contract changes
- scope expansion beyond the approved objective

## Privacy and Proof Safety

- Do not expose secrets, tokens, private docs, customer data, browser tabs, notifications, unrelated personal files, or internal-only content in logs or screenshots.
- Redact sensitive proof or keep it local and uncommitted.
- Do not paste credentials into `PROGRESS.md`, screenshots, issue comments, or PR descriptions.

## Budget and Stop Conditions

- Turn/time/token budget: `<budget>`
- Retry cap: stop/report after `<N>` repeated validation failures for the same unresolved cause.
- Credential/access blocker: stop/report.
- Product decision blocker: stop/report.
- Safety or permission ambiguity: stop/report.

## Partial Completion Protocol

If the full goal cannot be completed, leave the workspace in the most useful safe state.

- Revert or isolate unsafe partial changes.
- Preserve useful completed changes when safe.
- Record exactly what passed and failed.
- Leave reproduction steps for remaining blockers.
- Update `STATE.md` with the next best action.
- Do not claim completion.

## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
