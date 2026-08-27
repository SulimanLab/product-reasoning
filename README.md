# Product Reasoning

An open-source agent skill that helps coding agents make product decisions before they make screens.

It is designed for Claude Code, Codex, and other agents that support the Agent Skills format.

## What it changes

Most coding agents are strong at turning a request into implementation. They are weaker at noticing when the request hides a product decision.

This skill inserts a lightweight reasoning loop:

`outcome → decision → timeline → reversibility → artifact → implementation → verification`

The agent is taught to:

- design outcomes instead of screens;
- reason across states and time, not only the happy path;
- make reversible decisions without permission-seeking;
- ask precise questions before durable commitments;
- use throwaway HTML prototypes when interaction is easier to judge than prose;
- separate evidence from interpretation and assumptions;
- explore creatively without dumping idea spam;
- treat a design system as vocabulary, not proof of good UX;
- verify the experience after the code works.

## Installation

Using [skills.sh](https://skills.sh):

```bash
npx skills@latest add SulimanLab/product-reasoning
```

Then select `product-reasoning` and the agents you want to install it into.

Manual installation also works: copy `skills/product/product-reasoning/` into the skills directory used by your agent.

## Why the skill is modular

The root `SKILL.md` contains only the execution path and trigger branches. Detailed reasoning lives behind references that are loaded only when relevant.

This follows the same progressive-disclosure principle used in Matt Pocock's open-source skills: keep always-loaded context small, make pointers precise, and move branch-specific reference material out of the main path.

## Prototyping philosophy

A prototype is throwaway code that answers a question.

If the uncertainty is spatial, interactive, sequential, or state-based, the agent should often show a tiny runnable HTML prototype instead of writing a UX essay. Fidelity should rise only as uncertainty falls.

## Project-specific overlays

This repository intentionally contains no company-specific design system, brand, clinical policy, product source registry, or private examples.

Teams should layer those locally. Keep durable project facts in project-owned context and let this skill provide the general reasoning discipline.

## Origins and inspiration

This skill grew out of discussions about product design, AI-assisted design, and creativity. Several videos were useful catalysts:

- [UX/product-design video that prompted the “decisions, not pixels” discussion](https://www.youtube.com/watch?v=gr0Val2QSbM)
- **How I Use AI as a Product Designer (4 Real Workflows)** — especially the distinction between access to a design system and actual product judgment
- [The Method I Use When I Have Zero Ideas](https://www.youtube.com/watch?v=1iOAdR4Vjto) — especially creativity as a process, divergent/convergent thinking, ant/flea moves, lateral reframing, and bad-idea inversion

The repository does **not** reproduce the video transcripts. Their concepts were reworked into operational rules for agents.

For skill-authoring structure and agent-document design, [Matt Pocock's `skills`](https://github.com/mattpocock/skills) was used as a best-practices reference, particularly progressive disclosure, precise trigger descriptions, composability, shared language, and prototypes built to answer a concrete question.

## License

MIT. See [LICENSE](LICENSE).
