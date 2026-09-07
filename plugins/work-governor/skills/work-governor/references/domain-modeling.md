# Domain modeling

Use this method when the task turns on project-specific concepts, terminology, relationships, boundaries, a glossary, or an architectural decision record. Existing project instructions and conventions take priority.

## Sharpen the model

Inspect the applicable glossary and, when present, the project's context map before choosing where a concept belongs. Use the map's relationships and pointers instead of creating a parallel glossary.

- Call out a term that conflicts with the existing glossary.
- Replace fuzzy or overloaded wording with a precise canonical term.
- Test relationships and boundaries with concrete edge-case scenarios.
- Compare stated intent with observed code. Code proves observed behavior, not necessarily the desired model; surface a contradiction rather than silently choosing either.

## Record settled language

Follow [project continuity](project-continuity.md) for write authority and timing. When a glossary edit is authorized, update the correct existing context in its established style. Create a glossary only when the authorized target and project conventions require one.

Keep `CONTEXT.md` a concise project glossary. Each entry has a canonical term, a one- or two-sentence definition, and optional avoided synonyms when they prevent ambiguity. Include only domain-specific concepts. Keep specifications, implementation details, workflows, status, plans, history, and KPIs in their existing sources of truth.

## Record durable decisions

Create or propose an ADR only when all three conditions hold:

1. Reversing the decision would be meaningfully costly.
2. The choice would be surprising without its context.
3. Real alternatives and a tradeoff led to the choice.

Follow the project's existing ADR location and style. Otherwise use a short title and a one- to three-sentence rationale; add options or consequences only when they preserve necessary context. Choose the next local sequential number after inspecting existing ADRs, never overwrite a number, and preserve superseded decisions as history with the project's status convention.

Do not turn each term or minor choice into an unconditional file write. Settle ambiguity first, then write only within current authority and the project's continuity rules.
