# Work Governor

An instruction-based plugin for Codex. Describe the result you want; Work Governor guides Codex through clarification, a small agreed plan, relevant skill selection, authorized work, and verification.

Created by Kyrylo as a personal project with AI assistance, for use in his own work.

**Release status:** public preview. Anonymous repository access and download of all 27 package files were verified on 7 September 2026. Installation in an independent Codex environment and the complete fresh Desktop workflow have not yet been verified. See [verification](docs/VERIFICATION.md).

## What you install

One plugin installs all four skills and their supporting instructions together:

| Bundled skill | Purpose |
| --- | --- |
| `work-governor` | Coordinate an explicitly delegated task; clarify material decisions, select available skills, and follow the agreed work through checks. |
| `research` | Investigate questions, check sources, and distinguish evidence from inference. |
| `writing-for-agents` | Write or refine agent instructions while preserving scope and permissions. |
| `chat-management` | Assess useful task splits and prepare context handoffs within the host's capabilities. |

Seven internal reference files cover domain modeling, project continuity, questionnaires, prototypes, and skill mechanics. They arrive with the plugin; they are not separate installations.

Other installed skills can be selected when relevant. Spreadsheet tools, coding specialists, search services, account connectors, and other plugins are **optional external capabilities**, not part of this package. No MCP server, background service, hook, or model is bundled.

## Install

Use the [installation guide](docs/INSTALL.md). It covers adding the repository marketplace, installing this one plugin, checking all four skills, and starting a new task.

The GitHub repository marketplace is an author-managed distribution source. It is separate from the official OpenAI Plugins Directory; this project has not been submitted to or approved for that directory.

## Start a task

In a new Codex task, select **Work Governor** from the `@` picker. Then describe your desired result and known boundaries:

> Help me turn a small automation idea into clear agent instructions. First clarify only decisions that affect the result, then propose a minimal plan. Keep the work local; no connected accounts or installs. Wait for me to approve the plan before creating the file.

You can also ask in plain language, “Use Work Governor to manage this task.” Helper selection is normally handled by Codex following Governor's instructions; manually invoking each helper is optional.

For a complete reproducible example, use [the offline demo](examples/OFFLINE-DEMO.md). It includes synthetic input, an authorization step, expected checks, and missing-capability cases.

You normally invoke Governor once per delegated task. Follow-up corrections retain that scope; a new independent task needs a new delegation. Repeating the mention should preserve settled decisions. To cancel accidental use, say that you want an ordinary answer without Governor for this request.

## Limits

- Codex supplies the model, tools, permissions, skill loading, and interface. Governor supplies instructions. It is not a separate enforcement system and cannot override host rules or guarantee model behavior.
- Clarification depth follows uncertainty. A settled small task may need no questions. Native question cards are host features: their availability, display, and persistence vary. The plugin cannot guarantee cards or change modes itself.
- A missing optional skill can be replaced by an available suitable method. Essential missing access must be explained with the remaining work and next action. Governor does not silently install missing capabilities.
- Task coordination depends on host tools and authorization. The instructions alone cannot create or move tasks.
- There is no self-learning or autonomous background process. Improvements require reviewed edits and a new package version.
- This release targets Codex. ChatGPT Work, mobile, every operating system, and every Codex version have not been validated.
- No plugin-specific account or credentials are required for the offline example. Codex itself requires its normal setup. If you choose an external service, that service's access and data handling apply; the absence of a plugin server does not mean Codex processes data offline.

## Package checks

With Python 3.9 or newer available, run from the repository root:

```bash
python3 scripts/check_package.py
```

This checks the expected file set, manifest paths, bundled skills, links, and common portability mistakes. It does not prove installation or model behavior. [Verification](docs/VERIFICATION.md) separates those evidence levels.

## License

[MIT](LICENSE). The installed plugin also includes the license. See [component origins](plugins/work-governor/NOTICE.md) for provenance and attribution.

Packaging follows the [official OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins). Official directory publication has its own [submission and review process](https://developers.openai.com/plugins/deploy/submission).
