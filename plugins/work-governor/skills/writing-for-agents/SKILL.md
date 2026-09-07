---
name: writing-for-agents
description: Use when creating or editing skills, AGENTS.md, CLAUDE.md, or other instructions read by agents.
---

# Writing for Agents

Write the smallest instruction set that reliably preserves the requested behavior. Keep the user's authority boundaries and the existing source of truth intact.

## Method

1. Inspect the target, applicable project instructions, and canonical references before editing. Change only the authorized files and preserve unrelated fields and behavior.
2. Separate ordered steps from reference material. Keep what every run needs in the entrypoint; move branch-specific detail behind a clear conditional pointer.
3. Make each pointer name the observable condition that loads its target. Put each meaning in one canonical place; point to schemas, commands, and configuration that the environment can reveal instead of copying stale caches.
4. Co-locate a concept with its rules and caveats. Give consequential steps checkable completion criteria.
5. Prefer concise positive instructions that describe the desired output. Keep explicit prohibitions for genuine safety or authority boundaries and pair them with the permitted path.
6. Verify the focused diff, links, preserved constraints, and the relevant validator or consumer behavior before claiming completion.

For a skill, read [skill mechanics](references/skill-mechanics.md) before changing frontmatter, invocation policy, package layout, or supporting references.

Ordinary authorized agent-document work remains scoped to that document. It does not activate Work Governor or authorize installation, publishing, external writes, or adjacent configuration changes.
