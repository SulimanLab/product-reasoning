---
name: product-reasoning
description: Use for product, UX, UI, flow, frontend, or product-facing backend work where an agent must reason about user outcomes, decisions, states, trade-offs, evidence, prototypes, or consequential implementation choices before building. Especially use when a request looks like “just add/change this UI” but may change the experience.
---

# Product Reasoning

Build the right experience before building the interface.

Use this loop:

`outcome → decision → timeline → reversibility → artifact → implementation → verification`

## 1. Frame before building

Before choosing components or code, determine:

- the user's situation and intended outcome;
- the decision, uncertainty, or action at this moment;
- the business/product outcome;
- the technical constraints that matter;
- the meaningful risk or trust consequences;
- what is evidence versus assumption.

If the request is obviously local and these answers are already clear from context, do this silently.

For deeper framing, read [references/product-reasoning.md](references/product-reasoning.md). For uncertain claims, read [references/evidence.md](references/evidence.md).

## 2. Choose a mode by reversibility

Read [references/decision-authority.md](references/decision-authority.md) when the choice may create future coupling.

- **Reversible:** decide and proceed.
- **Ambiguous but cheap:** make the best assumption; state it only if it materially affects the result.
- **Consequential:** narrow the unresolved choice, recommend one option, then ask precisely before committing the consequential part.
- **Exploratory:** if the obvious answer is weak or stale, use [references/creative-exploration.md](references/creative-exploration.md).

Uncertainty alone is not a reason to ask. Future cost is.

## 3. Design the timeline, not the screenshot

For meaningful actions, reason through the relevant states across time: before, action, feedback, wait, success, failure, interruption, recovery, return, aftermath.

Only model states that affect understanding, trust, completion, safety, or recoverability.

Read [references/experience-timeline.md](references/experience-timeline.md) when the task includes async work, navigation, persistence, payments, uploads, bookings, external systems, or failure/retry behavior.

## 4. Use the smallest useful artifact

Default ladder:

`one concise recommendation → simple structure/flow → throwaway interactive HTML → production`

Skip levels when they do not help.

Read [references/prototyping.md](references/prototyping.md) when seeing or interacting with the idea would settle the decision faster than prose.

A prototype answers a question. It is not a half-built product.

## 5. Fit the product, not just the design system

Inspect the relevant code, flow, design system, product docs, and evidence before inventing new patterns.

Use existing components when they express the right experience. Consistency is not proof of good UX.

Read [references/design-system.md](references/design-system.md) when creating or breaking product/UI patterns. Read [references/engineering.md](references/engineering.md) when implementation choices may create durable contracts or architecture.

## 6. Communicate with signal

Read [references/communication.md](references/communication.md) when presenting a recommendation, prototype, trade-off, or consequential question.

Default user-facing shape:

1. recommendation;
2. artifact only if useful;
3. material trade-off only if it changes the choice;
4. question only if the unresolved choice is consequential.

One strong recommendation beats option spam.

## 7. Verify the experience

Do not stop at “tests pass” or “matches the design.” Verify the intended user outcome and state transitions.

Read [references/qa.md](references/qa.md) before declaring a meaningful product change done.

## Failure modes

If work drifts into screen-first implementation, permission-seeking, generic UX advice, premature polish, happy-path-only design, novelty for novelty's sake, or cosmetic option sets, read [references/anti-patterns.md](references/anti-patterns.md).

## Project overlays

This skill is intentionally product-agnostic. A repository or team may provide a project-specific product context, design language, source registry, safety policy, or decision history. Treat those as overlays, not replacements for the reasoning loop.

Current explicit user instruction and hard safety/legal requirements outrank this skill's heuristics.
