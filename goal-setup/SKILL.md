---
name: goal-setup
description: Create a verified Codex /goal setup from messy session and repo context. Use when the user asks to prepare, scaffold, write, or refine a /goal run, goal prompt, PLAN.md, CONSTRAINTS.md, CHECKS.md, PROGRESS.md, AGENTS.md, visual proof screenshots, ExecPlan, PLANS.md, or an "ubergoal" style markdown file pack for a long-running autonomous Codex task in a code repo, product workspace, personal/local-file workflow, research task, or documentation task.
---

# Goal Setup

Prepare a `/goal` run by turning the current conversation, repo history, and project docs into a durable markdown contract. Create the files first, then give the user the exact `/goal` prompt. Do not start the goal unless the user explicitly asks you to.

Core rule: the `/goal` command itself must be under 4,000 characters. Target 2,000-3,000 characters, hard-stop at 3,900, and move all detailed brief/context into files.

Fit rule: use `/goal` for long-running, self-verifiable work. For a small one-off that can be completed in the current turn, do the work normally instead of creating a goal pack.

Active-goal rule: only one `/goal` can be active in a thread/session at a time. Before launching a new goal, check current goal status where possible or instruct the user to type `/goal` alone first; if another goal is active, pause, complete, clear, or intentionally continue that goal before starting a new one.

Branch/PR rule: goal agents may create clean branches or worktrees, make milestone-sized commits, push branches, and open PRs when the repo/task warrants it. They must inspect current branch and dirty state first, preserve unrelated changes, and include validation/proof links in PR descriptions.

Lifecycle rule: goal packs start under `docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/` and move to `docs/goals/implemented-plans/<YYYY-MM-DD>-<goal-slug>/` only after the user has truly confirmed goal completion.

Completeness rule: within the approved objective, write scope, and safety constraints, optimize for the finished product rather than a plan, workaround, or partial handoff. The goal pack must carry the persistent Completeness Standard from [goal-pack-templates.md](references/goal-pack-templates.md) into `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md` so the execution agent sees it repeatedly.

Visual proof rule: screenshots are review artifacts, not raw monitor dumps. For UI, browser, frontend, or visual-regression goals, require evidence that a human can trust at normal zoom: focused browser tab or component screenshots, clear captions, and a ledger that ties each image to an acceptance criterion. Full-desktop screenshots are not acceptable proof unless the task is explicitly about multi-app desktop layout and the image is cropped or annotated so the relevant state is legible.

UX rule: any goal that touches user-facing behavior must include a UX review gate, not just code/tests. The execution agent must inspect the actual workflow from the user's point of view, cover expected/empty/loading/error states where relevant, check copy and affordances, and capture visual proof before completion.

Anti-premature-completion rule: a goal must not finish merely because the first implementation attempt and a narrow test passed. Substantive goals need a final audit loop: reread the goal docs, inspect the diff, run the required checks, complete the acceptance/evidence tables, perform UX/visual review when applicable, update `PROGRESS.md`, and only then mark done.

Decision-complete pre-research rule: before creating or finalizing a goal pack, answer every reasonably answerable factual, code, data, infra, and UX question yourself using available repo context, local history, read-only runtime checks, browser/app tools, logs, and connected sources. Do not hand an implementation agent a diagnosis task like "figure out whether X is true" when it can be resolved safely during goal setup. Separate proven facts, decisions, and remaining unknowns. Only leave unknowns for the goal runner when they require mutation, external approval, unavailable access, or are inseparable from implementation. If a remaining product/UX choice needs the end user's judgment, ask the user before finalizing the goal or record it as a pause trigger rather than burying it as implementation work.

## Workflow

1. Confirm the target workspace.
   - Use the current working directory or the repo/path the user named.
   - Find the git root when available.
   - Run a non-destructive status check before edits.
   - Never overwrite existing goal files without reading them and preserving useful content.
   - Classify the goal type: code repo task, personal/local-file task, research/documentation task, visual/UI task, deployment/infra task, or mixed.
   - Decide whether `/goal` is actually warranted. If the task is small, non-iterative, or not self-verifiable, explain that a normal prompt is better and ask before creating a pack.
   - Record the intended execution surface: Desktop/app for setup, CLI/app for goal execution, and the original setup chat for review/follow-on goals.
   - Record the branch/worktree strategy: current branch, dirty state, whether a clean branch or worktree should be created, whether milestone commits are allowed, and whether a PR should be opened.

2. Read deeply before drafting.
   - Read the current session context, the user's attached files, and any markdown strategy docs they provided.
   - Read repo instructions and docs: `AGENTS.md`, `README*`, `CONTRIBUTING*`, `docs/`, existing plans, issue docs, and relevant implementation files.
   - Inspect history when it clarifies intent: recent `git log`, related branches, existing plan/progress docs, PR notes, or local session summaries if the user points at them.
   - Search with `rg` for named features, issue keys, modules, failing commands, and acceptance criteria.
   - For reported bugs or ambiguous behavior, reproduce or trace the current behavior as far as safe read-only access allows before converting it into implementation scope.
   - Query safe read-only stores, logs, browser/app state, or connected tools when the user supplied concrete examples and access is available. Do not defer that evidence gathering to the goal runner by default.
   - Ask at most one concise blocking question if the goal cannot be made verifiable. Otherwise make a clear assumption and proceed.

3. Synthesize the real intent.
   - Identify the actual objective, why it matters, likely write scope, out-of-scope work, verification commands, risk boundaries, and pause triggers.
   - Express the objective in the shape: do `<work>` until `<measurable end state>` without `<constraints being violated>`.
   - If the ask is broad or ambiguous, generate focused, balanced, and ambitious goal options before finalizing; ask the user to choose when the tradeoff matters, or record the selected default and why.
   - Convert vague asks into observable outcomes. A proper goal must have artifacts or commands that prove completion.
   - Decide whether each observed issue actually requires a code change, a data repair, a deploy/reingestion, a product decision, or no action. Put that decision in the goal pack instead of making the runner rediscover it.
   - For complex goals, create a dependency graph that names blockers, parallelizable tracks, validation gates, and recovery/checkpoint boundaries.
   - Record pre-research as `Proven Facts`, `Decision Log`, and `Remaining Unknowns`; unresolved unknowns must include the exact blocked access or user decision needed.
   - If the context reveals competing interpretations, capture the chosen interpretation in `PLAN.md` and list unresolved ambiguity in `CONSTRAINTS.md` or `PROGRESS.md`.

4. Choose a file layout.
   - Default for reusable or multi-goal repos: `docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/`.
   - The folder name must include a datestamp and a descriptive goal slug, for example `2026-05-13-dashboard-composer-validation`.
   - Ensure the sibling archive path exists or is documented: `docs/goals/implemented-plans/`.
   - Create `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md` in that directory.
   - Create a `proof/` subfolder inside that exact goal folder whenever visual validation or visual proof may be required; do not create a standalone `proof/` directory beside or outside the goal folder.
   - Use root-level goal files only when the repo is dedicated to one active goal or the user asked for the canonical root layout.
   - Create or update `AGENTS.md` only for stable project-wide context. Keep it lean; move task-specific detail into the goal pack.
   - For complex multi-hour architecture work, add ExecPlan-style sections inside `PLAN.md`: `Progress`, `Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective`.
   - For very large shared-state runs, add an optional `STATE.yaml` or `TASKS.yaml` only if machine-readable state will reduce ambiguity.
   - For explicitly multi-agent runs, add optional `COORDINATION.md` and `agent-notes/` inside the goal folder with disjoint ownership and integration rules.
   - For visual, UI/UX, before/after, or proof-heavy runs, add optional `proof/index.html`, `proof/before-after.html`, or `review/index.html` as review dashboards. Markdown remains canonical.

5. Write the goal pack.
   - Create the required files: `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md`.
   - Create `AGENTS.md` only if missing or clearly incomplete for stable repo instructions.
   - Use [goal-pack-templates.md](references/goal-pack-templates.md) for the exact sections.
   - Keep `GOAL.md` under 4,000 characters. It is the compact charter, not the full brief; move detailed examples, scope, checks, and implementation notes into `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md`.
   - In `GOAL.md`, explicitly list `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md` in `Read First`.
   - Add a `Goal Pack Contract` section to `GOAL.md` stating that `PLAN.md` is the milestone source of truth, `CONSTRAINTS.md` is the guardrail/write-scope contract, `CHECKS.md` is the validation/completion-audit contract, and `PROGRESS.md` is the required live checkpoint log.
   - Append the full `Completeness Standard` section from [goal-pack-templates.md](references/goal-pack-templates.md) to every generated goal doc, including `GOAL.md`, `PLAN.md`, `CONSTRAINTS.md`, `CHECKS.md`, and `PROGRESS.md`.
   - State that the goal is not complete until `CHECKS.md` has evidence for every acceptance criterion and `PROGRESS.md` records the final validation outcome.
   - State that the goal folder must remain in `plans-to-implement` until the user explicitly confirms true completion, then it may be moved to the matching path under `implemented-plans`.
   - Make every milestone independently checkable and connect every acceptance criterion to evidence in `CHECKS.md`.
   - Include a completion audit table that maps every acceptance criterion to evidence before the goal can be marked complete.
   - If visual validation is in scope or reasonably needed, require screenshots in `<goal-folder>/proof/` with filenames and captions that explain exactly what each image proves relative to the goal.
   - A goal that requires browser, Chrome, browser-use, computer-use, screenshot, frontend, UI, visual regression, or visual review evidence cannot be marked complete unless those proof screenshots exist inside the same goal folder's `proof/` subfolder and are referenced from `CHECKS.md` and `PROGRESS.md`.
   - For visual proof, add the Visual Proof Capture Standard from [goal-pack-templates.md](references/goal-pack-templates.md) into `CHECKS.md` and `PROGRESS.md` whenever screenshots are required.
   - For user-facing work, add the UX Review Standard from [goal-pack-templates.md](references/goal-pack-templates.md) into `CHECKS.md` and `PROGRESS.md`; include a ledger for workflow, state coverage, copy/affordance review, accessibility basics, and regressions.
   - Add an explicit anti-premature-completion gate to `CHECKS.md`: the runner must perform a final audit pass after implementation rather than marking done immediately after the first green check.
   - Add Subjective Quality Rubrics to `CHECKS.md` whenever tests alone cannot prove quality; every rubric row must have evidence and status.
   - Add Branch, Commit, and PR Strategy to `PLAN.md` and `CONSTRAINTS.md` for repo work.
   - Add Scope Optioning and Dependency Graph sections to `PLAN.md` when ambiguity or sequencing risk exists.
   - Tighten AGENTS.md hygiene: stable repo-wide guidance only, task-specific context stays in the goal folder, and proposed additions should be drafted before modifying `AGENTS.md`.
   - Add Multi-Agent Coordination sections only when multi-agents are explicitly being used.
   - Add optional HTML Proof/Review Artifact sections only for UI/UX, before/after, or proof-heavy goals; they must link back to `CHECKS.md` acceptance criteria and screenshots in `proof/`.
   - Prefer browser-tab, viewport, or component-level screenshots over operating-system full-screen screenshots. Capture at a stable viewport such as 1440x1000, 1512x982, or 1600x1200 unless the product needs another size.
   - If using Browser, browser-use, Chrome, Playwright, or a similar browser automation tool, save viewport screenshots directly from the page or relevant locator. If using Computer Use, use it to navigate and verify state, then crop or recapture the active browser content so unrelated apps, tabs, desktop wallpaper, notifications, and other private context are excluded.
   - Reject proof images that are whole-desktop panoramas, unreadable due to scaling, missing the relevant UI state, missing the source URL/context, or not referenced from the completion audit. Re-capture or crop them before marking the goal complete.
   - Put hard guardrails in `CONSTRAINTS.md`: write scope, banned operations, destructive-command rules, external side effects, token/time limits, and hard-stop conditions.
   - Initialize `PROGRESS.md` with the discovery performed, files created, assumptions, next checkpoint, and unchecked validation still pending.
   - Include any setup-time traces, field comparisons, root-cause notes, and non-code conclusions in `PLAN.md` or `PROGRESS.md` so the goal runner starts from decisions, not speculation.

6. Draft the `/goal` prompt.
   - This is mandatory output.
   - Keep it under 4,000 characters; prefer under 3,000. If shell access is available, count the final command with `wc -m` or Python `len(...)` before returning it.
   - Do not paste the task brief into `/goal`. Point to `GOAL.md` and the goal directory instead.
   - Structure it as: `/goal <do the work> until <measurable end state> without <constraints being violated>. Follow <goal-dir>/GOAL.md...`
   - The prompt must tell the goal runner to reread the session context, repo docs, git/history evidence, and every goal-pack file before implementing.
   - Include the goal-pack paths, milestone loop, validation cadence, progress logging requirement, pause triggers, and final stop condition.
   - Prefer a prompt that starts with the user's intent, not a generic "implement the plan" sentence.
   - Warn the user if they are in Plan mode: active goals may appear idle there, so execution should happen in normal/default mode.
   - Tell CLI users to either paste the full generated `/goal ...` command or, if their CLI requires slash-command composition, type `/goal` first and then paste the objective text. Also tell them to type `/goal` alone first if they need to inspect active status.

## Goal Quality Bar

A task is ready for `/goal` only when Codex can check progress against evidence. Good evidence includes tests, eval scores, builds, screenshots, browser checks, deployment health checks, generated files, or a completion audit. Do not package vague goals, broad architecture debates, stakeholder judgment calls, or loose unrelated task lists as `/goal` runs without first narrowing them into verifiable milestones.

For anything user-facing, "works" is not enough. The goal must define what a good user experience means for the workflow: clear copy, visible state transitions, useful empty/error handling, reasonable loading behavior, keyboard/focus basics, responsive constraints when relevant, no visual overlap/clipping, and no regressions to adjacent surfaces.

Good personal/local-file goals are also acceptable when they have evidence: a cleaned document, a transformed notes folder, a research summary with sources, a README improvement, a file inventory with proposed removals, or a completed local artifact. They still need scope, checks, and a done condition.

Do not package safely answerable diagnosis as implementation work. If the setup agent can inspect the code, compare live records, verify a UI state, or answer a logical product question before the goal starts, it must do so and write the outcome into the pack. The implementation agent should receive the smallest correct objective plus known constraints, not a pile of open-ended research.

Within that bounded goal, do not under-scope the work. Search before building, test before shipping, document the result, and prefer the complete durable fix over a workaround or deferred follow-up when the real solution is within reach.

## Output

Finish with:
- Created or updated file paths.
- The active lifecycle location: `plans-to-implement` while pending, or `implemented-plans` only after user-confirmed completion.
- One short intent summary.
- The exact `/goal ...` command in a fenced code block, with a measured or stated character count under 4,000.
- A short launch note: check existing goal with `/goal` if needed; only one active goal at a time; run execution in normal/default mode; return to the setup chat for review and follow-on goal prompts.
- Branch/worktree/commit/PR strategy for repo goals.
- Scope options and selected default when the goal was ambiguous.
- Dependency graph summary for complex goals.
- Any required visual proof plan, including the exact `<goal-folder>/proof/` folder path and expected screenshots.
- The visual proof capture method when UI evidence is required: Browser/browser-use, Chrome, Playwright, or Computer Use plus cropped recapture. State the expected viewport/component crop and how images will be self-reviewed before completion.
- Any optional multi-agent coordination or HTML proof/review dashboard artifacts that should be created.
- Validation performed while setting up the goal pack, plus any setup checks that remain unrun.

If the user asked only for a prompt and not files, still do the deep read and return the prompt, but explain which files would be created for a full goal pack.
