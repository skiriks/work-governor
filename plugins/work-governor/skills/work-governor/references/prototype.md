# Prototype

A prototype is an explicitly requested, bounded experiment that answers one concrete design question. It is never automatic preparatory implementation during grilling.

## Gate the experiment

1. State the settled question and the smallest artifact that can answer it.
2. Give a short plan: authorized location or surface, synthetic inputs, interactions or cases, and checks.
3. Execute only when explicit authority covers that exact prototype. Reuse authority already supplied; do not repeat the interview or approval.

If the user requested only a plan, stop after the plan. If the question, artifact, or permission is materially unresolved, keep that point open instead of implementing an assumed answer.

Choose the branch by the question:

- Business logic, state transitions, or data shape: read [logic prototype](prototype-logic.md).
- Layout, hierarchy, or interaction alternatives: read [UI prototype](prototype-ui.md).

## Boundaries

Use synthetic or in-memory data unless the exact experiment authorizes something else. Network access, live data, dependencies, branches, commits, persistence, and external resources each require authority that covers them. A user-authorized demo-only path overrides the convenience of changing a nearby real page.

Inspect the relevant host or project conventions and run checks proportional to the experiment's risk. Prototype validation shows what the experiment demonstrated; it is not production acceptance. Promotion or reuse in production is a separately scoped implementation with production-quality evidence. Disposal, moving, or deleting prototype artifacts is also a separate action.

Finish with the question, observed answer, check evidence, limitations, and the still-unshipped status of the prototype.
