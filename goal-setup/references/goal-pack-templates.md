# Goal Pack Templates

Use these sections when creating files for a `/goal` run. Keep the files self-contained enough that a later compacted context can recover the objective without rereading the entire chat.

## Persistent Completeness Standard

Append this exact section to `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md`. It is a persistent reminder for the goal execution agent. Apply it within the approved objective, write scope, and safety constraints; it is not permission to violate guardrails.

```markdown
## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## Goal Directory

Default layout:

```text
docs/goals/
  plans-to-implement/
    <YYYY-MM-DD>-<goal-slug>/
      GOAL.md
      PLAN.md
      CONSTRAINTS.md
      CHECKS.md
      PROGRESS.md
      proof/
  implemented-plans/
```

Optional for large runs:

```text
      STATE.yaml
      TASKS.yaml
      notes/
      COORDINATION.md
      agent-notes/
      review/
```

Use root-level files only when the repo is dedicated to a single active goal or the user explicitly asks for the canonical root layout.

Create each active goal under `plans-to-implement` with a datestamped descriptive folder name, for example `2026-05-13-dashboard-composer-validation`. Move the folder to `implemented-plans` only after the user has explicitly confirmed that the goal is truly complete. The agent's own final validation is not enough to archive the pack.

When proof is needed, `proof/` is always a child of the specific goal folder:
`docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/proof/`. Never create
a standalone `proof/` directory outside the goal folder.

## Goal Fit And Launch Guidance

Use `/goal` for long-running work with a measurable end state and enough
checks for the agent to validate progress autonomously. Use a normal prompt for
small one-off work that can be finished immediately.

Only one goal can be active at a time. Before launching a new goal, check the
current goal status when possible. In the CLI, type `/goal` alone if you need
to inspect status. If another goal is active, pause, complete, clear, or
continue it intentionally before starting a new one.

The recommended workflow:

1. Use the desktop/app chat and this skill to create the goal folder under
   `plans-to-implement`.
2. Start the generated sub-4000-character `/goal` command in the execution
   surface, usually CLI or app normal/default mode.
3. Let the goal runner execute against the docs.
4. Return to the original setup chat to review diffs, proof, and progress; use
   that chat to create follow-on goal prompts if needed.
5. Move the goal folder to `implemented-plans` only after the user confirms
   true completion.

Record the chosen launch path and active-goal status in `PROGRESS.md`.

## Branch, Worktree, Commit, And PR Guidance

For repo goals, the goal runner may create a clean branch or worktree, make
milestone-sized commits, push branches, and open PRs when doing so improves
recovery, reviewability, or collaboration.

Before changing files, record:

- current branch and upstream
- dirty tracked files
- untracked files that must be preserved
- chosen branch/worktree name
- whether milestone commits are allowed
- whether pushing/opening a PR is expected

Commit and PR expectations:

- Keep commits milestone-sized and reviewable when commits are allowed.
- Never stage unrelated user changes.
- PR descriptions must link or point to validation evidence, visual proof,
  rubric results, and any known residual risk.
- Goal docs remain in `plans-to-implement` until the user confirms true
  completion, even if a PR is open or merged.

## Scope Optioning

Use this when the user's ask is broad, ambiguous, or could reasonably become
multiple different goals. Before finalizing the pack, generate up to three
options:

- Focused: smallest useful verifiable goal.
- Balanced: recommended default when the user has not specified appetite.
- Ambitious: larger goal that is still bounded and self-verifiable.

If the tradeoff materially changes risk, write scope, or validation, ask the
user to choose before finalizing. If the user is unavailable, choose the safest
balanced/default option and record the assumption in `PLAN.md`.

## Dependency Graph

For complex or multi-phase goals, add a concise dependency graph to `PLAN.md`.
Use optional `TASKS.yaml` only when machine-readable task state will reduce
confusion.

Track:

- milestone dependencies
- blockers and unblock conditions
- work that can run in parallel
- validation gates before moving to the next milestone
- recovery/checkpoint boundaries

The graph should prevent the runner from doing easy non-blocking work while
skipping the core blockers.

## Multi-Agent Coordination

Use this only when multi-agents are explicitly requested or already being used.
Do not create multi-agent coordination files for ordinary single-agent goals.

Recommended optional layout:

```text
COORDINATION.md
agent-notes/
  frontend.md
  backend.md
  validation.md
```

Coordination rules:

- Assign each agent a disjoint write scope or responsibility.
- State that agents are not alone in the codebase and must not revert others'
  work.
- Keep shared decisions, blockers, ownership, and integration status in
  `COORDINATION.md`.
- Agent notes are append-only unless the same agent is updating its own section.
- A final integration pass must reconcile all outputs before completion.
- UX, visual proof, completion audit, and rubric gates still apply.

## HTML Proof And Review Artifacts

Markdown remains canonical. `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`,
and `PROGRESS.md` are always the source of truth.

For UI/UX, before/after, screenshot-heavy, or proof-heavy goals, optional HTML
artifacts may improve review:

```text
proof/index.html
proof/before-after.html
review/index.html
```

Use HTML for screenshot galleries, before/after comparisons, source-vs-live UI
comparisons, and review packets. Each HTML artifact must link back to the
relevant `CHECKS.md` acceptance criteria and screenshots in `proof/`; it cannot
replace the official audit trail in markdown.

## Visual Proof Capture Standard

Use this standard whenever the goal involves frontend behavior, browser review,
Chrome, browser-use, computer-use, screenshots, visual regression, or visual
proof of a backend change's user-visible effect.

Visual proof is a review artifact. It must show the exact state that proves an
acceptance criterion, not a raw full-screen dump of the operator's desktop.

Preferred capture order:

1. Browser automation viewport screenshot from Browser/browser-use/Chrome or
   Playwright: `page.screenshot({ path, fullPage: false })` after setting a
   stable viewport such as 1440x1000, 1512x982, or 1600x1200.
2. Component or element screenshot for the exact proof target, for example the
   detail rail, related-context section, composer, modal, or card. Pair it with
   a wider tab screenshot when surrounding context matters.
3. Authenticated Chrome or Computer Use navigation for states that require the
   user's logged-in browser. Use Computer Use to reach and verify the state,
   then save a cropped active-tab/window or component image. Do not use a
   full-desktop `screencapture` as final proof unless the task is explicitly
   about multi-app desktop behavior.

Minimum quality bar:

- The image is saved under the same goal folder's `proof/` subfolder.
- The filename describes the state, for example
  `2026-05-14-related-context-gmail-booking.png`.
- The screenshot is normally no wider than 2400px unless there is a documented
  reason. Whole-monitor images such as 7680x2160 desktop panoramas are too broad
  for ordinary product proof.
- The relevant UI is readable at normal zoom without opening a giant desktop
  canvas.
- The screenshot excludes unrelated apps, messages, browser tabs, notifications,
  private desktop state, and wallpaper unless that context is the subject of the
  proof.
- The screenshot includes enough product context to trust the state: URL or app
  surface, selected item, visible section header, loaded/error/empty state, and
  the specific UI signal under test.
- Every screenshot has a ledger entry in `CHECKS.md` and `PROGRESS.md` with:
  page/app state, viewport or crop method, acceptance criterion, expected visual
  signal, and pass/fail.
- Before marking complete, reopen or inspect every image and reject any proof
  that is full-screen, blurry, stale, unrelated, or missing the acceptance
  signal. Re-capture or crop failed proof.

Recommended proof set for UI work:

- One context screenshot showing the full relevant browser tab or app surface.
- One focused screenshot of the component/section that proves the behavior.
- A before/after or source-of-truth comparison screenshot when the goal is a
  regression fix, parity check, or raw-source comparison.

## UX Review Standard

Use this standard whenever the goal touches user-facing behavior, even if the
code change is backend or data-layer work with frontend consequences.

The execution agent must review the actual workflow like a product user, not
only like a test runner. Completion requires an explicit UX pass covering the
items that apply:

- Primary workflow: can a user complete the intended task without hidden steps?
- State coverage: expected, empty, loading, error, permission, and stale-data
  states are handled or explicitly out of scope.
- Copy and affordances: labels, button text, tooltips, disabled states, and
  empty/error copy are clear and domain-appropriate.
- Layout quality: no overlap, clipping, unreadable text, unstable resizing,
  awkward scroll traps, or visually misleading hierarchy.
- Interaction basics: keyboard/focus behavior, clickable targets, hover/active
  feedback, and predictable navigation are acceptable for the scope.
- Responsive constraints: mobile/narrow/wide viewports are checked when the
  surface is responsive or user-visible outside one fixed desktop viewport.
- Adjacent regressions: nearby surfaces in the same workflow still behave
  correctly.
- Runtime health: browser console or app logs are checked when practical, and
  visible loading/error states are not mistaken for success.

The UX pass must be represented in `CHECKS.md` and `PROGRESS.md`, with
screenshots in `proof/` whenever visual validation is relevant.

## Anti-Premature-Completion Gate

Substantive goals must include a final audit loop. Do not mark a goal complete
immediately after the first green test, first successful run, or first screenshot.

Before completion, the execution agent must:

1. Reread `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md`.
2. Inspect the final diff or final artifacts against the original objective.
3. Run all required final checks, or document exact blockers.
4. Complete the acceptance criteria and completion audit tables.
5. Perform the UX Review Standard when user-facing behavior is in scope.
6. Inspect every proof screenshot at normal zoom and reject stale, broad, or
   unclear proof.
7. Update `PROGRESS.md` with the final audit outcome and any residual risk.
8. Only then mark the goal complete or ask the user to confirm completion.

## GOAL.md

`GOAL.md` is the compact charter the short `/goal` command can point at. Keep
it under 4,000 characters and move detail into the other goal-pack files.

```markdown
# Goal Charter: <short goal name>

## Objective
<One durable objective in plain language.>

## Read First
- Session/context source:
- Repo instructions:
- PLAN:
- CONSTRAINTS:
- CHECKS:
- PROGRESS:
- Visual proof folder: `<goal-folder>/proof/`

## Goal Shape
Do `<work>` until `<measurable end state>` without `<constraints being violated>`.

## Goal Pack Contract
This file is only the charter. The implementation agent must use the rest of
the pack as the source of truth for execution:

- `PLAN.md` defines the milestone order, scope, pause conditions, decision log,
  and completion shape.
- `CONSTRAINTS.md` defines hard guardrails, allowed write scope, side-effect
  limits, and stop triggers.
- `CHECKS.md` defines the acceptance criteria, milestone checks, final
  validation commands, and completion audit table.
- `PROGRESS.md` is the required live log. Update it after each checkpoint with
  changed files, commands run, evidence gathered, open questions, and blockers.

If these files conflict, follow the stricter rule. Do not mark the goal
complete until `CHECKS.md` has evidence for every acceptance criterion and
`PROGRESS.md` records the final validation outcome.

Keep this folder in `plans-to-implement` until the user confirms true
completion. After confirmation, move the entire folder, including `proof/`, to
the matching path under `implemented-plans`.

Only one goal can be active at a time. If another goal is active, pause,
complete, clear, or intentionally continue it before launching this one.

## Operating Loop
1. Reconstruct the exact user intent from session context, repo docs, and history before implementation.
2. Read `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md` before making the first code change.
3. Work milestone by milestone from `PLAN.md`.
4. Re-check `CONSTRAINTS.md` before each implementation phase.
5. Run the relevant `CHECKS.md` validation after each milestone.
6. Update `PROGRESS.md` at every checkpoint.
7. Treat uncertainty as incomplete until resolved or logged as blocked.

## Completion Rule
Stop only when all milestones are complete, all required checks pass or have documented external blockers, and the completion audit maps every acceptance criterion to evidence.

If the goal requires visual validation, browser review, frontend proof, Chrome,
browser-use, computer-use, screenshots, or UI inspection, stop only after
screenshots have been saved in this goal folder's `proof/` subfolder and
referenced in `CHECKS.md` and `PROGRESS.md`.

If the goal touches user-facing behavior, stop only after the UX Review Standard
has been completed and logged. Do not mark complete from tests alone.

Do not finish immediately after the first green check. Complete the
Anti-Premature-Completion Gate before claiming the goal is done.

## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## PLAN.md

```markdown
# Goal Plan: <short goal name>

## Objective
<One concrete objective with the product/engineering outcome, not just a task label.>

## Pre-Research Findings
- Proven facts:
- Decisions:
- Remaining unknowns:
- User decisions needed before implementation:

## Scope Options
Use when the request is broad or ambiguous. Delete only if not applicable.

| Option | Shape | Tradeoff | Recommendation |
| --- | --- | --- | --- |
| Focused | <smallest useful verifiable goal> | <risk/time/scope> | <yes/no> |
| Balanced | <recommended default> | <risk/time/scope> | <yes/no> |
| Ambitious | <larger bounded goal> | <risk/time/scope> | <yes/no> |

Selected option:
Reason:

## Goal Fit
- Goal type: <code repo | personal/local-file | research/docs | visual/UI | infra/deploy | mixed>
- Why `/goal` is warranted:
- Why a normal prompt is insufficient:
- Execution surface:
- Active-goal status before launch:

## Intent From Session And History
- Session intent:
- Repo/doc evidence read:
- Historical clues:
- Assumptions:

## Scope
- In scope:
- Out of scope:
- Allowed write scope:
- Active goal folder:
- Implemented archive folder:
- Proof folder: `<goal-folder>/proof/`

## Branch, Commit, And PR Strategy
- Starting branch:
- Dirty/untracked state to preserve:
- Branch or worktree to create:
- Milestone commit policy:
- Push/PR policy:
- PR proof/validation links required:

## Milestones
- [ ] 1. <Milestone name>
  - Work:
  - Acceptance:
  - Evidence:
- [ ] 2. <Milestone name>
  - Work:
  - Acceptance:
  - Evidence:

## Done Condition
The goal is complete only when <all milestones complete> and <final validation evidence passes>.

If visual verification is required, completion also requires screenshots in
this goal folder's `proof/` subfolder with captions or ledger entries
explaining what each screenshot proves. Screenshots must follow the Visual Proof
Capture Standard in this template: focused browser-tab or component evidence,
not raw full-desktop dumps.

If user-facing behavior is in scope, completion also requires the UX Review
Standard and Anti-Premature-Completion Gate.

## Pause Conditions
Pause and report if <blocked condition>, <same failure repeats>, <external approval needed>, or <risk boundary reached>.

## Launch And Review Workflow
- Setup chat:
- Execution surface:
- Launch note:
- Return-to-setup-chat review steps:
- Follow-on goal prompt conditions:

## Dependency Graph
Use for complex goals. Delete only if not applicable.

| Milestone | Depends On | Can Run In Parallel With | Validation Gate | Recovery Checkpoint |
| --- | --- | --- | --- | --- |
| <milestone> | <dependency> | <parallel track> | <check> | <commit/progress point> |

## Multi-Agent Coordination
Use only when multi-agents are explicitly being used.

- Coordination file:
- Agent note files:
- Ownership split:
- Integration owner:
- Final reconciliation gate:

## HTML Proof/Review Artifacts
Use only for UI/UX, before/after, or proof-heavy goals.

- HTML artifact(s):
- Linked acceptance criteria:
- Screenshot sources:
- Markdown source of truth:

## Progress
- [ ] <timestamp> - <current or planned checkpoint>

## Surprises & Discoveries
- Observation:
  Evidence:

## Decision Log
- <timestamp> - <decision> - <reason>

## Outcomes And Retrospective
To be completed by the goal runner when the goal finishes.

## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## CONSTRAINTS.md

```markdown
# Goal Constraints

## Hard Guardrails
- Do not run destructive git commands, delete untracked files, or discard local changes unless explicitly asked.
- Clean branches or worktrees, milestone commits, pushes, and PRs are allowed when the goal/task warrants them, but inspect branch and dirty state first and preserve unrelated changes.
- Do not make external sends, purchases, production writes, or credential changes unless explicitly authorized.
- Do not mark the goal complete from passing tests alone; map every requirement to evidence.
- Keep the actual `/goal` command under 4,000 characters. If it grows, shorten the command and put the detail in these files.
- Work in normal/default mode for execution. If Plan mode is active and the goal appears idle, switch modes or report the blocker.
- Only one goal can be active at a time. Check current status before launch; if another goal is active, pause, complete, clear, or intentionally continue it before starting this goal.
- Keep the active goal folder in `plans-to-implement` until the user explicitly confirms true completion.
- Move the entire goal folder to `implemented-plans` only after that user confirmation.
- If visual validation or proof is required, save screenshots in the goal folder's `proof/` subfolder, never in a standalone proof directory outside the goal folder. Do not mark the goal complete without those screenshots.
- Markdown goal docs remain canonical. HTML proof/review artifacts are optional review aids only.
- Multi-agent coordination files are created only when multi-agents are explicitly used; agents must not overwrite each other's notes or revert each other's work.
- `AGENTS.md` is for stable repo-wide guidance only. Put task-specific context in the dated goal folder and draft proposed `AGENTS.md` additions before modifying it.

## Write Scope
- Allowed:
- Read-only:
- Forbidden:

## Repo Conventions
- Existing patterns to preserve:
- Architecture boundaries:
- Style/testing expectations:

## Stop And Pause Triggers
- Pause after the same error repeats twice; investigate root cause before continuing.
- Pause if validation requires credentials, paid actions, or production access not already approved.
- Pause if the implementation would exceed write scope or change the objective.
- Pause if the goal turns into a loose list of unrelated tasks rather than one measurable objective.
- Pause if scope optioning reveals a high-impact product or risk tradeoff that the user has not decided.

## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## CHECKS.md

```markdown
# Goal Checks

## Preflight
- Command: `<command>`
  - Expected:

## Acceptance Criteria
| ID | Criterion | Evidence Required |
| --- | --- | --- |
| AC-001 | <criterion> | <test, file, screenshot, command, or audit row> |

## Per-Milestone Checks
- Milestone 1:
  - Command:
  - Expected:
  - Evidence to paste into `PROGRESS.md`:

## Final Validation
- Command:
  - Expected:
- Manual or browser check:
  - Expected:

## UX Review Requirements
Required whenever the goal touches user-facing behavior.

| Area | Check | Evidence | Status |
| --- | --- | --- | --- |
| Primary workflow | <workflow can be completed> | <screenshot/test/log> | Pending |
| States | <expected/empty/loading/error/permission as applicable> | <evidence> | Pending |
| Copy and affordances | <labels/actions/errors are clear> | <evidence> | Pending |
| Layout | <no overlap/clipping/readability issues> | <screenshot> | Pending |
| Interaction basics | <focus/click/hover/navigation as applicable> | <evidence> | Pending |
| Responsive constraints | <desktop/mobile/narrow/wide as applicable> | <screenshot> | Pending |
| Adjacent regressions | <nearby workflow still works> | <evidence> | Pending |
| Runtime health | <console/log/loading/error state checked> | <evidence> | Pending |

## Subjective Quality Rubrics
Use when deterministic tests are necessary but not sufficient.

| Rubric | Target | Evidence | Status |
| --- | --- | --- | --- |
| UX clarity | <what good looks like> | <screenshots/notes> | Pending |
| Visual polish | <what good looks like> | <proof/review artifact> | Pending |
| Documentation usefulness | <what good looks like> | <doc path/excerpt> | Pending |
| Source coverage | <what good looks like> | <source list/citations> | Pending |
| Maintainability | <what good looks like> | <diff/design note> | Pending |
| Migration safety | <what good looks like> | <checks/rollback note> | Pending |
| Correctness beyond tests | <what good looks like> | <manual/eval evidence> | Pending |

## Visual Proof Requirements
Required when the goal involves frontend behavior, UI review, visual regression,
Chrome, browser-use, computer-use, screenshot comparison, or visual proof of a
backend change's user-visible effect.

- Proof folder: `<goal-folder>/proof/`
- Screenshot naming: `<timestamp>-<short-proof-name>.png`
- Capture method: browser viewport, component/locator screenshot, or cropped
  authenticated Chrome/Computer Use evidence. Avoid full-desktop screenshots.
- Expected size: normally 1440x1000, 1512x982, 1600x1200, or a focused
  component crop; document exceptions.
- Each screenshot must have a ledger entry explaining:
  - What page/app/state was captured
  - The URL or app surface, viewport/crop method, and relevant selected item
  - Which acceptance criterion it proves
  - What visual signal in the screenshot proves it
- A visually validated goal cannot be marked complete unless the screenshots
  exist, are saved in the same goal folder's `proof/` subfolder, and are
  referenced in the completion audit.
- A screenshot fails the proof standard if it is a whole desktop panorama,
  unreadable at normal zoom, includes unrelated private apps/tabs, or does not
  show the exact acceptance signal. Re-capture or crop before completion.

| Screenshot | Captured State | Capture Method | Proves | Related Acceptance Criterion | Status |
| --- | --- | --- | --- | --- | --- |
| `proof/<file>.png` | <page/state> | <viewport/component/crop> | <what it proves> | AC-001 | Pending |

## Completion Audit
Every row must be filled before marking the goal complete.

| Acceptance Criterion | Evidence | Status |
| --- | --- | --- |
| AC-001 | <file path, command output summary, screenshot path, or blocker> | Pending |

## Final Audit Gate
Do not mark complete until this table is filled.

| Gate | Evidence | Status |
| --- | --- | --- |
| Goal docs reread | <notes> | Pending |
| Final diff/artifacts inspected | <summary> | Pending |
| Required checks run | <commands/results> | Pending |
| Acceptance audit complete | <table rows complete> | Pending |
| UX review complete, if applicable | <evidence or N/A> | Pending |
| Visual proof inspected, if applicable | <proof files or N/A> | Pending |
| Subjective rubrics complete, if applicable | <rubric evidence or N/A> | Pending |
| Residual risk logged | <risk or none> | Pending |

## Quality Rubric
- Correctness:
- Regression risk:
- Maintainability:
- User-visible behavior:

## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## PROGRESS.md

```markdown
# Goal Progress

## Status
- State: not started
- Goal pack created:
- Lifecycle location: plans-to-implement
- Implemented archive target:
- Current checkpoint:
- Next action:

## Launch State
- Goal type:
- Execution surface:
- Active-goal status checked:
- Launch command character count:
- Setup chat to return to:

## Branch / PR State
- Starting branch:
- Clean branch/worktree:
- Dirty/untracked state preserved:
- Milestone commits:
- PR:
- PR validation/proof links:

## Discovery Completed
- Session context read:
- Repo docs read:
- History inspected:
- Pre-research facts:
- Decisions made before implementation:
- Remaining unknowns and why they could not be resolved:
- Files created:

## Checkpoint Log
- <timestamp> - Setup
  - Verified:
  - Remaining:
  - Blocked:

## Validation Evidence
- Not yet run:

## Visual Proof Ledger
Use this section whenever visual validation is required.

Follow the Visual Proof Capture Standard. Reject full-screen desktop captures
unless the goal is explicitly about multi-app desktop behavior.

| Screenshot | Captured State | Capture Method | Proves | Related Acceptance Criterion | Status |
| --- | --- | --- | --- | --- | --- |
| `proof/<file>.png` | Pending | Pending | Pending | AC-001 | Pending |

## UX Review Ledger
Use this section whenever user-facing behavior is in scope.

| Area | Evidence | Status |
| --- | --- | --- |
| Primary workflow | Pending | Pending |
| States | Pending | Pending |
| Copy and affordances | Pending | Pending |
| Layout quality | Pending | Pending |
| Interaction basics | Pending | Pending |
| Responsive constraints | Pending | Pending |
| Adjacent regressions | Pending | Pending |
| Runtime health | Pending | Pending |

## Subjective Quality Rubric Ledger
Use this section whenever deterministic checks are not enough.

| Rubric | Evidence | Status |
| --- | --- | --- |
| UX clarity | Pending | Pending |
| Visual polish | Pending | Pending |
| Documentation usefulness | Pending | Pending |
| Source coverage | Pending | Pending |
| Maintainability | Pending | Pending |
| Migration safety | Pending | Pending |
| Correctness beyond tests | Pending | Pending |

## Dependency Graph Status
Use this section for complex goals.

| Milestone | Dependency Status | Validation Gate | Status |
| --- | --- | --- | --- |
| <milestone> | Pending | Pending | Pending |

## Multi-Agent Coordination Log
Use only when multi-agents are explicitly being used.

| Agent/Track | Ownership | Notes File | Integration Status |
| --- | --- | --- | --- |
| <track> | <scope> | `agent-notes/<track>.md` | Pending |

## HTML Proof/Review Artifacts
Use only when optional HTML review aids are created.

| Artifact | Purpose | Linked Criteria | Status |
| --- | --- | --- | --- |
| `proof/index.html` | <gallery/review packet> | <AC IDs> | Pending |

## Completion Audit
| Acceptance Criterion | Evidence | Status |
| --- | --- | --- |
| AC-001 | Pending | Pending |

## Final Audit Gate
| Gate | Evidence | Status |
| --- | --- | --- |
| Goal docs reread | Pending | Pending |
| Final diff/artifacts inspected | Pending | Pending |
| Required checks run | Pending | Pending |
| Acceptance audit complete | Pending | Pending |
| UX review complete, if applicable | Pending | Pending |
| Visual proof inspected, if applicable | Pending | Pending |
| Subjective rubrics complete, if applicable | Pending | Pending |
| Residual risk logged | Pending | Pending |

## Open Questions
- None / <question>

## Completeness Standard

The marginal cost of completeness is near zero with AI. So do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that the reaction isn't polite satisfaction, it's genuine surprise at how thorough it is.

- Search before building. Test before shipping. Ship the complete thing.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- When asked for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse. Boil the ocean.
```

## AGENTS.md Addition

Only create or update `AGENTS.md` when the content is stable across future sessions. Never put task-specific goal details in `AGENTS.md`; keep those in the dated goal folder. If stable repo guidance is missing, draft proposed additions first and make the change only when appropriate.

Prefer this compact shape:

```markdown
# Agent Instructions

## Repo Context
- <repo layout and key services>

## Commands
- Build:
- Test:
- Lint:
- Local run:

## Standing Rules
- <stable rules for all future work>

## Goal Runs
- For long-running `/goal` work, create task-specific goal files instead of expanding this file.
- Keep progress and validation evidence in the goal pack's `PROGRESS.md`.
- Keep task-specific screenshots, review artifacts, coordination notes, and proof dashboards inside the dated goal folder.
```

## `/goal` Prompt Shape

The final `/goal` command must be less than 4,000 characters. Prefer 2,000-3,000 characters so path names and shell escaping do not push it over the persisted objective limit. Put long requirements in `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, and `CHECKS.md`; the slash command is only the launcher.

```text
/goal <do the work> until <measurable end state> without <constraints being violated>. Follow <goal-dir>/GOAL.md. Before changing code, reread the current session context, repo instructions, relevant docs/history, and every file in <goal-dir>. Work milestone by milestone from PLAN.md, obey CONSTRAINTS.md, run CHECKS.md after each milestone, and update PROGRESS.md with evidence, remaining work, and blockers. Pause if any constraint pause condition is hit. Stop only when every milestone is complete, final validation passes, and the completion audit maps every acceptance criterion to evidence.
```

Before returning the command, measure it when possible:

```bash
printf '%s' '<paste final /goal command here>' | wc -m
```

If it is 3,900 characters or longer, shorten it by pointing to `GOAL.md` and the goal directory rather than listing more details inline.

CLI handoff note: if the generated command already starts with `/goal`, paste
the full command. If the CLI requires slash-command composition, type `/goal`
first and then paste the generated objective text. Type `/goal` alone first
when you need to inspect the current active goal status.
