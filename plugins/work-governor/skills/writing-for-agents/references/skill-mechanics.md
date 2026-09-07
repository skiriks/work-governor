# Skill mechanics

Read this branch only when the target is a skill.

## Invocation and metadata

- Every Codex `SKILL.md` keeps `name` and `description` in YAML frontmatter. Make the description a discriminating trigger, not a copy of the workflow.
- Automatic discovery is the default. For a user-requested explicit-only skill, keep its description and set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Do not substitute unsupported invocation keys for the current Codex policy.
- Preserve supported interface, policy, and dependency fields that are outside the requested change. Keep `interface.short_description` concise and consistent with the skill.
- When current Codex authoring fields or validation rules matter, read the bundled authoring guidance rather than copying a second version into the skill.

## Package shape

Keep shared purpose, essential constraints, and routing in `SKILL.md`. Put substantial branch-only guidance in `references/`, and link it from the point where its condition becomes relevant. Use package-relative links; installed behavior must not depend on a source checkout, cache, or another absolute local path.

Split a separate discoverable skill only when ordinary tasks should select it independently. Keep a workflow inside an explicit router when it has no legitimate independent trigger. Do not duplicate a helper's body into a router that can conditionally read the helper.

Use scripts or assets only when they materially support repeated execution or generated output. Avoid auxiliary README, changelog, or placeholder files unless the package requires them.

## Check

Validate the completed skill with the current bundled skill validator. Also inspect whether its description routes correctly, every reference is reachable, invocation policy matches the request, and the package contains only intended runtime files. Validation does not prove host discovery or real UI behavior.
