# Engineering Policy

Good product reasoning must survive implementation.

## Inspect before changing

Understand the relevant route, state model, API/data contract, analytics, tests, and existing component seam before adding new structure.

## Prefer shallow commitments

When product direction is still uncertain:

- avoid schema changes;
- avoid new dependencies;
- avoid foundational abstractions;
- avoid persistence unless persistence is the question;
- keep experiments easy to delete.

## Product debt

A feature can pass tests and still create product debt through unclear state, duplicate sources of truth, hidden failure, or misleading feedback.

Tests verify implementation behavior. Product verification checks whether the resulting experience communicates truthfully and supports the intended outcome.
