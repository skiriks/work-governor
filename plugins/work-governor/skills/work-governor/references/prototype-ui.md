# UI prototype

Use this branch to compare layout, information hierarchy, or primary affordances. Build inside the exact authorized demo surface; do not alter a real product page merely because it is convenient.

## Artifact

- Follow the authorized project's framework, component library, and styling conventions.
- Default to three structurally different variants. Vary layout, hierarchy, and primary action, not only color or copy.
- Keep all data synthetic or read-only and all actions fake unless broader behavior is explicitly in scope.
- Present variants on one authorized route or surface. When useful and supported by the project, make selection reload-stable with a `?variant=` parameter and a small clearly separate switcher.
- Preserve normal input behavior if keyboard navigation is added. Mark the surface as a prototype and keep it out of production behavior.

Prefer embedding variants in an existing host surface only when that surface is explicitly in scope. Otherwise use the authorized demo page or the project's existing prototype route. A new route is appropriate only when it is within authority and no supplied demo surface fits.

Hand over the variant keys and the local way to view them. Capture which structure answered the question and why. The chosen design is evidence for a later implementation, not code authorized for production; promotion and cleanup remain separate actions.
