---
name: chat-management
description: Use when coordinating Codex chats or tasks, proposing independent parallel work, or preparing a continuation handoff.
---

# Chat Management

Keep work in tasks that are easy to finish and resume. Choose coordination that advances the user's result without losing decisions, edits or ownership. This helper can run alone; it does not activate full Work Governor, grilling, or implementation. Treat “chat”, “thread” and “task” as the same user-visible Codex object when context supports it.

Read current project instructions, plan, task state and relevant tool descriptions. Use the host's actual capabilities and permissions; this skill is guidance, not a task service, context meter, timer or source of authority. Keep coordination and handoffs in chat unless a file or tracker update is requested.

## Choose the smallest useful arrangement

Assess coordination when a plan settles, a material dependency changes, or observed context problems make a transfer useful. Do not repeatedly propose a split the user declined unless circumstances change.

- **One task:** keep small, tightly coupled work together. A new task is useful only if its clearer scope, separate working context, environment or lifecycle outweighs transfer and integration cost.
- **Internal subagents:** use them for bounded independent fact-finding, implementation with disjoint ownership, or review when permitted. They are subtasks of the current request, not user-visible chats. No new user task is needed merely to parallelize a small investigation.
- **Separate user-visible tasks:** propose them when independent substantial deliverables, different work phases or separate environments benefit from durable task boundaries. Keep one coordinator responsible for the combined result. Prefer one implementation owner per project; simultaneous writers require settled interfaces and explicit independent scopes.

An optional coordination proposal must not create an artificial blocker. If creation is not authorized and the same approved plan can proceed safely in this task or with internal subagents, continue that work. If the proposed split changes scope, authority or the practical route to completion, settle that decision before dependent work.

## Propose safe parallel work

Before offering concurrent tasks, check that each lane has a concrete deliverable, independent prerequisites, a read/write scope, and a way to verify it. Name shared contracts and who integrates the results. Distinguish read-only reference files from files or external state a lane may modify.

Parallel implementation needs non-overlapping writes and settled interfaces. Separate worktrees prevent accidental working-directory interference; they do not resolve incompatible schema decisions, shared-file changes, or external-state conflicts. Serialize dependent changes or reserve the shared edit for one owner. Read-only audits may run in parallel while the integration step waits for their results. Inspect existing active work before introducing another writer.

Give a compact, concrete proposal: why splitting helps; each proposed task's title, outcome, permitted scope, prerequisites and environment; the integration owner, order and combined checks; and the authority needed to create it. Use known project paths and branch/base information, or identify what must be inspected. Do not invent a branch name, estimated speedup, or a need for parallelism just because tools are available.

## Create and follow tasks only with authority

Use internal collaboration tools for internal subtasks and the host's task-management tools for user-visible tasks. Follow their current schemas and authorization requirements. In Codex, create a new user-visible task only after the user explicitly requests its creation; invoking this helper, approving an implementation plan, or requesting a split proposal is not that request. A clear request to create the concrete proposed tasks is sufficient; do not ask again for the same creation.

Before project-task creation, inspect the saved projects and repository status through the required tools. Make the proposed checkout/worktree and starting state explicit. Follow the host's Git isolation defaults and preserve any user-requested starting state, including uncommitted work. If a required state cannot be carried across safely, explain that blocker before creating a destination that would silently lose work. Creation does not grant commit, merge, publish, install, send, archive or deletion authority.

Dispatch each authorized task with a self-contained brief and exact ownership. Task setup may return a provisional identifier: wait for a real task ID and readiness before calling operations that require it. Follow progress using the host's bounded wait/status tools, keeping useful independent work moving. Dispatch, acknowledgement or a worker's completion claim is not a verified result.

Require each working task to return its deliverable, changed files or artifacts, relevant branch/worktree and base/final revision when applicable, actual checks, review status, open risks and next integration step. Verify the returned evidence and run the relevant combined checks before claiming the overall plan complete. Pass an integration brief to the named owner through an authorized task-follow-up tool; do not transfer this internal authority to external email or chat services.

## Decide whether to continue in a new task

Recommend a continuation when there is a concrete benefit: the user reports lost context, decisions repeatedly need reconstruction, constraints are being confused, or a new phase needs a clean working scope. Use host-reported compaction or context data only as evidence actually available. Length, one compaction, or elapsed time alone is not a mandatory move. Never invent token percentages, compaction counts or an automatic context-limit trigger. If the next steps remain clear and safe, continue them.

Explain the observed difficulty and what a fresh task would improve. Prepare the complete handoff below as part of the proposal. Offer continued work here when it remains viable. A user request to prepare a transition authorizes a chat handoff, not creation of the new task, a branch, or a file.

## Prepare and verify the handoff

Write the actual transferable brief in the chat; saying “handoff prepared” or listing what you will include is not a handoff. Make the destination able to take its first safe action without asking the user to reconstruct history. Include the following as relevant, using “not applicable” or “unknown” instead of invented detail:

- the goal, desired result, completion criteria, scope and exclusions;
- the working method and how to invoke it in the destination, following the delegation rule below;
- the plan's actual status (proposed, approved for execution, or plan-only), exact remaining step, settled decisions and assumptions; for a child task, distinguish the approved parent strategy from approval of the child's own implementation;
- completed work and current files/artifacts, including uncommitted changes and relevant branch/worktree/base/final revision;
- canonical documentation and source pointers, with frozen or immutable boundaries;
- checks and review results labeled fresh, historical, stale, failed or unrun, with decisive evidence and failures;
- permissions actually granted in this conversation and those still missing, plus current host/mode constraints;
- blockers, unresolved decisions and pending cards with their original questions/options, actual answers and custom constraints;
- task ownership, dependencies, integration contract, who verifies the overall result, and the exact next action to take. For a single-task continuation, assign remaining execution and final verification to the receiving task; for coordinated work, preserve the named owners and identify any unsettled ownership explicitly.

When Work Governor governs the source work and the user requests its continuation or a child-task brief, open the transferable brief with an actionable plain-language request, such as “Use Work Governor for this task.” Preserve the relevant working rules in the brief: reuse settled decisions, continue authorized execution through checks, and explain a real stop with the needed user action, options and resumption. This request survives ordinary text copying; do not depend on a rendered plugin chip, personal marketplace identity or remembered cache path. If the destination lacks Governor, the brief must still support its first safe action without claiming the skill loaded. Do not add full Governor when the source was ungoverned or the user opted out; describing Governor as the product being developed is not delegation.

Keep every unfinished required acceptance check in the remaining plan, even after a release artifact or upload exists. Identify separately deferred or excluded paths and their decision status. Write critical file paths and source task/document URLs visibly as literal text, alongside optional clickable labels, so copying without link targets retains the pointers. A handoff's historical permissions remain reported context; only the current user's request and destination host rules establish executable authority.

Inspect decisive current evidence before sending a handoff. A stale `ready` label or quoted historical approval is not current verification or authority. Use the existing [project-continuity method](../work-governor/references/project-continuity.md) when reconstructing project state from canonical documents; do not create competing status documents.

After explicit creation/continuation authority, stop overlapping source edits before dispatching the destination. Send the prepared brief through the supported tool and verify that the destination exists and has the required context and working state. If readiness or receipt cannot be verified, report it as pending and state the needed user action; do not claim a successful move. Leave the source available unless archiving or removal was explicitly requested. A handoff preserves reported permissions but cannot override the destination host's rules.

End a completed coordination-only request with the requested proposal or handoff and its status. If the ongoing plan is blocked, include in the user-visible reply itself why, the precise user action and expected evidence, feasible alternatives with a recommendation, and what will resume afterward; internal status fields are not a substitute. If no user action is needed for the completed scope, say so. Do not stop executable plan work merely to announce that a coordination step ended.
