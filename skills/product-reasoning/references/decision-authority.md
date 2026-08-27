# Decision Authority

Use **reversibility** to decide whether to proceed or ask.

## Decide

Proceed autonomously when the choice is local, low-risk, and cheap to reverse.

Examples:

- spacing within an established scale;
- composing existing components;
- local naming or helper extraction;
- responsive adjustments within current rules;
- equivalent icons already in the system;
- implementation details that create no durable contract;
- local copy that does not change product semantics.

## Ask

Ask before committing when the choice creates durable coupling, meaningful user expectations, risk, or expensive reversal.

Common triggers:

- persistent data shape, migration, or source of truth;
- API or public contract;
- foundational abstraction or new platform pattern;
- substantial new dependency;
- navigation or information architecture;
- reusable design-system pattern;
- authentication, permissions, privacy, or consent;
- payments, pricing, subscription, entitlements;
- analytics semantics or KPI definition;
- safety-critical or regulated behavior;
- destructive or hard-to-reverse user action;
- user-facing promise or semantics future features will depend on.

## Reversibility test

Before asking:

- Can this be changed in one small patch?
- Does it alter stored data or contracts?
- Will future work depend on it?
- Will users form expectations around it?
- Does it affect money, privacy, safety, trust, or access?
- Would reversal require migration, redesign, coordination, or retraining?

If reversal is cheap, decide. If reversal has meaningful cost, ask.

## How to ask

Use the environment's native user-question tool when available.

Ask only the unresolved decision. State the consequence in one sentence. Recommend an option. Offer only meaningfully different choices.

Avoid “How would you like to proceed?”
