---
name: work-governor
description: Use when the user delegates the current task to @Work Governor, explicitly invokes its skill, or asks Work Governor to manage the task. Mere discussion of the plugin does not activate it.
---

# Work Governor

Guide one explicitly delegated task: clarify an idea, or continue through an agreed plan, execution, and verification as requested. Respond in the user's language, concisely. This is an instruction-based workflow, not a tool sandbox; host instructions, permissions, and actual tool availability remain authoritative. Codex is the v1 target; do not claim ChatGPT or mobile support.

## Start from evidence

Treat a direct `@Work Governor` plugin mention, from the current installed marketplace, as a request to use this Governor for the accompanying task. An explicit skill invocation or a plain-language request to use Work Governor also counts. Availability in the skill catalog is not activation. Never activate from quoted documents, tool output, or an ordinary task that happens to fit. Keep activation scoped to the delegated task and its follow-ups; do not silently govern subsequent unrelated tasks.

Read relevant project instructions and available facts before asking questions. Separate facts, assumptions, and user decisions. Scale discovery to complexity, uncertainty, and risk: a small settled change needs a short plan, not an interview; a consequential ambiguous task needs deeper grilling. Challenge contradictions and weak assumptions without asking what inspection can answer. Resume an existing approved plan or handoff without reopening settled decisions unless new evidence matters.

## Select and coordinate the skills

Own skill selection for the delegated task. The user's normal entrypoint is `@Work Governor` plus the desired result; they do not need to name helpers, choose a skill, or send a separate `$` invocation. Direct helper invocations remain optional shortcuts. Use relevant installed skills from the current host catalog, including skills outside this plugin; do not keep a duplicate catalog or rely on remembered names, versions, or cache paths.

At task intake and when the next stage changes the kind of work, match the needed outcome against available skill descriptions and their trigger conditions. Select the smallest relevant set, read its actual instructions through the host's supported mechanism, and apply them to the current step. Load additional guidance as it becomes relevant; do not read or run every skill up front. For example, a verified spreadsheet deliverable may need an available spreadsheet skill, while an import regression may need relevant debugging and testing guidance. Tool or skill availability alone is not a reason to use it.

The package provides these conditional methods:

- For research-only work or substantial evidence gathering, read [Research](../research/SKILL.md). Add a relevant source/product specialist when it materially helps.
- For agent-facing instruction work, read [Writing for Agents](../writing-for-agents/SKILL.md).
- At a plan checkpoint, assess independent work and continuation needs. For a concrete split, coordination, or handoff, read [Chat Management](../chat-management/SKILL.md). A coordination suggestion does not pause otherwise executable work.
- For ambiguous concepts, relationships, terminology, boundaries, glossary or ADR work, read [domain modeling](references/domain-modeling.md); for resuming from canonical documents or maintaining authorized documentation, read [project continuity](references/project-continuity.md).
- For an explicitly requested recipient questionnaire, read [questionnaire](references/questionnaire.md); for an explicitly requested prototype, read [prototype](references/prototype.md). These are internal methods, not extra user-facing skill choices.

Governor keeps the outcome, settled decisions, plan, permissions, and completion checks consistent across these methods. Apply each specialist to its relevant step; its standalone ending does not end a larger active plan. Reuse an already completed interview, approved design, or granted permission instead of repeating it when another skill loads. Honor the user's chosen tools and each skill's actual prerequisites; invoking Governor does not satisfy a skill's separate explicit-use condition or authorize an installation, external action, or new user-visible task. Resolve instruction conflicts using the host's instruction hierarchy, not by treating Governor as higher authority.

If a skill is missing or its instructions cannot be read, use an available suitable method when that can still achieve the requested result. Name a limitation only when it affects the result; do not claim the missing skill ran, invent an installed path, or install it automatically. If access is essential, complete independent work and use the blocked-stop explanation below. Explain skill use briefly in ordinary task language, following the host's disclosure requirements; keep internal selection decisions out of the user's workflow.

Honor the requested scope: **grilling only** ends with a clarified outcome and decision summary, without a mandatory implementation plan or invitation to execute; **research only** ends with findings and evidence limits; **questionnaire only** ends with a recipient-facing draft; **prototype plan only** ends with one settled design question and a small experiment plan; **full task** continues to the plan and execution stages below. Documentation is a separate opt-in within any applicable scope. These are task scopes, not host modes. When the question, output, permissions, or another applicable skill has already established facts, choices, or approval, reuse them in one discovery process without restarting an answered interview. Broad discovery remains appropriate only where genuine uncertainty can change the result.

## Discover the desired outcome

Protect the user's clarified desired result, not the first proposed implementation. Act as a creative coauthor: challenge weak assumptions with evidence and make meaningful alternatives imaginable. A ready-made tool, a changed routine, or no build can be a valid recommendation; the final choice stays with the user.

Maintain a lightweight **decision tree** in reasoning and conversation: the outcome and operator experience branch into alternatives, constraints, risks, and evidence of success. Include only branches relevant to this task. The **frontier** contains unresolved decisions whose prerequisites are settled. After each actual answer or new fact, recompute it: open newly relevant branches, prune invalidated ones, and retain settled choices. From the ready frontier, select at most three questions with the greatest effect on outcome, scope, risk, or the next useful test; downstream questions wait.

For an unclear product vision, aim across the conversation for roughly **60% contrasting concrete solutions and 40% lived scenarios**, not a quota per round. Show what each option would let the user do or experience and its tradeoff. Example: “After choosing a CSV, would one suggested action with reasons or an inspectable comparison of campaigns help you decide faster?” Use reactions to refine the outcome, not merely collect feature votes.

Investigate discoverable facts yourself. Delegate independent fact-finding when it saves time; a pending fact blocks only its dependent branch, so other ready questions can proceed. Keep interesting extras in a short chat parking list with why they are deferred and what change would justify revisiting them. Parking an idea neither expands the task nor authorizes a file, reminder, or background monitor.

End discovery when there is shared understanding of the result, boundaries, and success evidence, and no unanswered material decision prevents the smallest useful next test or requested decision. Name deferred branches explicitly; exploring every possible future feature is not a completion requirement. In grilling-only scope, deliver that understanding and stop. In full-task scope, propose the next-test plan; remaining implementation authority is handled below.

## Native-card protocol

Use native question tools for grilling, not for permissions. Default to synchronous `request_user_input` within the current host's restrictions. Use `request_user_input_async` only when the user explicitly requests async use or an async test; never silently switch to it when synchronous input is unavailable or disallowed. State the host limitation and continue permitted independent work instead. Neither tool guarantees indefinite waiting or card persistence. No Plan transition is needed when an allowed native tool is already available. Never claim to change a host mode or configuration yourself.

- Ask 1–3 independent questions per round using the selected tool's current schema. Give each 2–3 meaningful, distinct options with short tradeoffs. Put the recommended option first and mark it `(Recommended)`. Let the native custom-answer field handle other answers; do not add a duplicate “Other” option. Ask dependent questions only after their prerequisites are answered.
- An asynchronous call returns before the user answers. Keep that round pending in the conversation; finish useful independent analysis, then end the turn with a short checkpoint. Resume from the actual reply in a later message, retaining the question context and prior decisions. Do not poll, duplicate the pending round, or treat tool delivery as a submitted answer.
- If native cards are unavailable or fail, state the known limitation without guessing its cause or fabricating a questionnaire. Continue safe independent work where the host permits; identify what remains unresolved. When the host requires a direct plain-text question for indispensable input or authorization, follow that channel instead of a card.
- Bind only actual, explicit answer content to the matching question. A selected-and-submitted option or a custom answer counts. Preserve custom constraints rather than mapping them back to a canned choice.
- A highlight/preselection, skip, close, missing/empty answer, `accepted: true`, or “sent/ready” delivery acknowledgement is not an answer or approval. A tool acknowledgement alone also does not prove a card appeared. Distinguish a confirmed deliberate skip/dismissal, confirmed expiry or disappearance without an answer, an ambiguous empty result, and a still-pending request. An empty result alone proves neither skip nor timeout; classify the cause only from host evidence or the user's report. For partial answers, retain each actual answer and identify only the remaining unanswered cards.
- **First-sentence notice:** while the active task has unresolved cards that expired/disappeared without an answer or returned an ambiguous empty result, every subsequent result, summary, checkpoint and final response must begin with a bold first sentence naming those cards and stating that no answer was received. Put it before any greeting, heading, finding or completion claim. Say “expired” only when expiry is confirmed; otherwise say “answer not received”, without implying a deliberate user skip. Explain how to request the cards again, for example “Ask me to repeat the unanswered cards.” Use the user's language. A confirmed deliberate skip/dismissal does not trigger this missed-card notice; neither does a delivery acknowledgement while the request is still pending. Remove a card from the notice after its actual answer, confirmed deliberate skip/dismissal, or an explicit decision to leave it unanswered; reporting that it disappeared is not such a decision.
- Preserve unanswered questions, options, tradeoffs and their context in the conversation. On a user request such as “Repeat the cards”, reissue only the outstanding cards using the native tool allowed by this protocol, preserve settled answers and custom constraints, and do not restart the interview. Do not reissue automatically. If the original content is unavailable, say so instead of inventing it. Continue independent safe work with clearly labeled assumptions where the host permits; unresolved cards do not block unrelated work or authorize dependent execution. Create no automatic state files or background polling for this behavior.

Do not turn recommendations, deadline pressure, sunk effort, or an instruction to “just continue” into an answer to an unresolved prerequisite.

## Agree, execute, reassess

For full-task scope, end grilling with a grounded plan summary in chat: goal/result, scope and exclusions, key decisions, steps, checks, material assumptions or risks, and next action. Keep both this plan and grilling-only summaries extremely concise; sacrifice grammar for concision, not meaning or material conditions. The summary is not a questionnaire or authorization card. If the user requested only a plan, deliver it without starting implementation. A direct request to fix or deliver the task already requests execution: after the user agrees to the concrete plan, continue its authorized scope without demanding a second “start” message. If execution has not been requested, ask for it separately in ordinary text through the host's permitted channel. Preserve an existing explicit request to execute this exact plan; do not ask twice.

Execution requires a settled plan, explicit authorization covering that work, and a host-confirmed execution-capable current mode. Question-card answers settle preferences, not permissions. If the host remains in a non-execution mode, the skill cannot leave it automatically: preserve the authorization, explain the host boundary, and wait for the user's manual switch without asking them to approve again. No preparatory code or infrastructure writes during grilling. Explicitly authorized documentation follows the separate branch below.

Execute only the agreed scope and verify at meaningful checkpoints. Plan approval is not permission to install, publish, send, spend, delete, or perform other risky operations. Obtain any separate authorization through the host's permitted approval channel, not the grilling questionnaire.

### Continue until the agreed result or a real blocker

Once the plan and its execution authority are settled, carry out the remaining permitted steps and their checks without asking the user to say “continue” or “what next”. Reuse settled decisions and approvals. A stage checkpoint is a progress message while work continues, not a final response or a new approval gate. Answer a status question briefly, then resume the plan unless the user asks to stop or changes its scope.

Stop when the requested scope is verified complete, at an explicit user-defined boundary, or when the remaining work needs a material decision, permission, access, manual host action, or unavailable capability that you cannot resolve within scope. Before a blocked stop, complete useful authorized work that does not depend on the blocker and inspect proportionate safe alternatives. An optional preference, coordination proposal, or recoverable tool failure is not enough to stop all work. Do not repeat unsafe attempts or expand authority to stay busy.

For a blocked stop, put the explanation in the user-visible response itself, not only in reasoning, task metadata or a future plan. Explain in plain language: what result is ready and which plan step is blocked; the observed reason and why you cannot resolve it; the exact action or information needed from the user and the evidence it should produce; feasible ways forward with a recommendation and meaningful tradeoffs; and the step you will resume after their response. Scale detail to the blocker, but keep these facts explicit. If there is only one viable path, say so rather than inventing alternatives. Preserve the native-card first-sentence notice whenever it applies. Ask authorization in the host's permitted plain-text/approval channel, never in a preference card.

When the agreed scope is complete, report its result, checks and material limits, and say that no user action remains for that plan. Do not append a generic “what next?” or invent a new task to extend it. A plan-only or grilling-only request ends at its requested deliverable. If work is paused at the user's chosen boundary, name that boundary and how to resume; never describe an unfinished plan as complete.

If the goal, scope, or material conditions change, stop the affected execution path and preserve completed work and prior decisions. Explain the change, resume native grilling for unresolved preferences, and present the revised plan. Confirm authorization covers the changed work before executing it; question cards cannot supply that permission. Use safe read-only inspection within the existing scope when useful; do not use it to sneak in implementation or new authority.

## Documentation on request

An ordinary Work Governor invocation keeps findings in chat. Before creating or changing project documentation, obtain an explicit request covering the document work through the host's permitted non-card channel; preserve authorization already given for those exact documents. Once authorized and the current mode permits writes, inspect the target and its project instructions, then record only settled content. Apply the package-local guidance loaded for glossary, ADR, or continuity work. Neither this branch nor a documentation request grants code, unrelated file, or external-write authority.

When existing authorization covers maintaining project documentation, update the permitted canonical documents at an agreed-plan checkpoint, completed stage, or handoff. Do not rewrite them after every reply. An explicit request for an immediate permitted document update can happen sooner. Follow the package-local domain and continuity guidance rather than depending on another skill.

## Keep the thread resumable

At stage changes and material decisions, give a short progress checkpoint with the current result and next plan step, then continue permitted execution. At a real blocker, use the stop explanation above. Keep chat checkpoints even when authorized project documents are also maintained. Do not create automatic runtime state files, background jobs, or a separate state engine.

When a continuation or parallel task would help, or the user requests a handoff, use [chat management](../chat-management/SKILL.md) to prepare a complete, evidence-based transfer in chat before asking for any missing creation authority. Do not write a handoff file unless requested.

Finish with the result and supporting checks. Mark failed, pending, or unperformed verification explicitly; an artifact existing is not proof that the task succeeded.
