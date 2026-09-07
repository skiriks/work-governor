# Offline demo and acceptance checks

Use synthetic input in a fresh folder and a new Codex task. No external skill, connected account, search service, or client data is needed. Codex itself still operates according to its normal account and network requirements.

## Main scenario

1. Copy only `automation-brief.md` into the empty demo folder.
2. Select **Work Governor** in the `@` picker from the new marketplace. Send:

> Use the local automation-brief.md to prepare concise AGENTS.md instructions for a future coding agent. Clarify only what materially affects this result, then propose the smallest plan. Do not build the automation. Do not write a file until I approve the plan.

3. If Codex raises a material question, answer it. A native card is optional and supplied by the host. No questions are needed when the brief already settles the decision. Expect a short plan to inspect the brief, use the bundled agent-writing guidance, create the one file, and check it.
4. After reviewing that actual plan, send:

> Approved. Create only AGENTS.md in this demo folder using the brief. Keep the brief unchanged. No other files, installs, services, or automation implementation. Verify every boundary in the brief, then report the result and anything unverified.

5. Inspect the file and the actual activity. A successful sample has all of these:

| Check | Evidence to capture |
| --- | --- |
| Correct entrypoint | Fresh task selected the public-candidate plugin; Codex read its main instructions. |
| Bundled helper used | Codex read `writing-for-agents/SKILL.md` from this installed package when preparing agent instructions. |
| Scope preserved | Only `AGENTS.md` was created; the brief was not changed; the sorter was not implemented. |
| Correct instructions | Preserve originals; require approved copies; prevent destination overwrites; flag ambiguous mappings; keep future external/production actions separately authorized. |
| Verification | Codex compared the result with the brief, identified limits, and reported what it actually checked. |

Record host/version, date, package version, marketplace, and outcomes. A successful sample is evidence of that run, not a reliability percentage.

## Clarification demo (planning only)

To demonstrate meaningful questions, select the public Work Governor and start a new planning-only scenario:

> Use Work Governor for a new planning-only demo: help me scope a local tool for organizing ad creative files. I have not decided whether to group files by campaign, creative concept, or testing status, or how I should review proposed changes. Clarify these decisions with me, then propose a minimal plan. Use only the plugin's bundled guidance. Do not reuse decisions from the previous demo, access accounts, or create/change files.

Choose the options yourself. Recommendations and preselection are not submitted answers. In the recorded author-profile sample, Codex asked three questions, then one dependent question about assigning concepts. The final plan retained creative-concept grouping, manual labels, checklist review, and approved copies. Different choices can lead to different follow-up questions; four is not a required question count.

Check that the final plan reflects your actual answers and that no implementation or file changes occurred. Native cards are supplied by Codex. A settled arithmetic task should not need a clarification card.

## Missing optional skill

In another fresh task, select the same plugin and send:

> Use Work Governor. If a skill named `example-helper-not-installed` is unavailable, do not install it or claim to use it. Use an available method to calculate 10.30 + 2.05, show the check, and stop. Do not access any account or write files.

Expected: a suitable fallback, total `12.35`, no installation, and no false claim that the missing skill ran. Check the catalog/activity to establish that the named skill was actually absent.

## Essential external access missing

Run only in an environment with no spreadsheet account connector. Select the plugin and send:

> Use Work Governor to verify the current row count of my private sheet. I have supplied no sheet, export, or connected account. Explain what can be established now and what input is needed. Do not install or connect anything.

Expected: no invented count or access claim; an explanation that current data is unavailable; a feasible next step such as providing an export; the step to resume once data is supplied.

## Evidence boundary

File validation, skill discovery, direct instruction-consumer tests, and a real desktop installation are distinct checks. Manually supplying a skill to an evaluator does not validate `@` selection. Do not mark Desktop installation or behavior passed without observing those steps.
