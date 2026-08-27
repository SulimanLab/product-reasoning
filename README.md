# Product Reasoning

[![validate](https://github.com/SulimanLab/product-reasoning/actions/workflows/validate.yml/badge.svg)](https://github.com/SulimanLab/product-reasoning/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An open-source agent skill that helps coding agents make **product decisions before they make screens**.

It is designed for Claude Code, Codex, and other agents that support the Agent Skills format.

## What it changes

Coding agents are strong at turning requests into implementation. They are weaker at noticing when a request hides a product decision.

This skill inserts a lightweight reasoning loop:

`outcome → decision → timeline → reversibility → artifact → implementation → verification`

It teaches an agent to:

- design outcomes instead of screens;
- reason across time and meaningful states, not only the happy path;
- make cheap, reversible decisions without permission-seeking;
- ask one precise question before durable commitments;
- use throwaway prototypes when interaction is easier to judge than prose;
- separate evidence, interpretation, assumptions, and proposals;
- explore creatively without dumping idea spam;
- treat a design system as vocabulary, not proof of good UX;
- verify the experience after the code works.

## Install

### Codex and other Agent Skills clients

Using [skills.sh](https://skills.sh):

```bash
npx skills@latest add SulimanLab/product-reasoning
```

Select `product-reasoning` and the agents you want to install it into.

### Claude Code

This repository also ships as a Claude Code plugin. From Claude Code:

```text
/plugin marketplace add SulimanLab/product-reasoning
/plugin install product-reasoning@sulimanlab
```

For local development:

```bash
git clone https://github.com/SulimanLab/product-reasoning.git
cd product-reasoning
claude --plugin-dir .
```

### Manual

Copy `skills/product-reasoning/` into the skills directory used by your agent.

## How it behaves

The skill is intentionally decisive.

- **Reversible choice:** decide and move.
- **Ambiguous but cheap:** make the best assumption.
- **Consequential choice:** recommend one direction and ask precisely before committing it.
- **Visual/interaction uncertainty:** build the smallest artifact that makes the decision inspectable.
- **Clear direction:** implement instead of continuing to discuss.

One strong recommendation beats three cosmetic options.

## Why the skill is modular

`SKILL.md` contains the execution path and precise pointers. Branch-specific reasoning lives in `references/` and is loaded only when relevant.

That architecture is deliberate: less always-loaded context, less instruction dilution, and clearer completion criteria.

## Repository structure

```text
.claude-plugin/
  plugin.json
  marketplace.json
.github/
  ISSUE_TEMPLATE/
  pull_request_template.md
  workflows/
    validate.yml
scripts/
  validate.py
skills/product-reasoning/
  SKILL.md
  references/
  examples/
ACKNOWLEDGEMENTS.md
CODE_OF_CONDUCT.md
CONTEXT.md
CONTRIBUTING.md
SECURITY.md
LICENSE
```

## Prototyping philosophy

A prototype is **throwaway code that answers a question**.

If uncertainty is spatial, interactive, sequential, or state-based, a tiny runnable HTML prototype can be more useful than a UX essay. Fidelity should rise only as uncertainty falls.

## Project overlays

This repository is intentionally product-agnostic. It contains no company-specific design system, brand, product source registry, domain policy, or private examples.

Teams should layer those locally. Project context should refine the general reasoning discipline, not fork it into a second giant prompt.

## Origins and inspiration

This skill grew out of discussions about product design, AI-assisted design, and creativity. These videos were useful catalysts:

- [UX/product-design video behind the “decisions, not pixels” discussion](https://www.youtube.com/watch?v=gr0Val2QSbM)
- **How I Use AI as a Product Designer (4 Real Workflows)** — especially the distinction between access to a design system and actual product judgment
- [The Method I Use When I Have Zero Ideas](https://www.youtube.com/watch?v=1iOAdR4Vjto) — especially creativity as a process, divergent/convergent thinking, ant/flea moves, lateral reframing, and bad-idea inversion

The repository does **not** reproduce the video transcripts. Their ideas were independently restated and converted into operational guidance for coding agents. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

For skill-authoring structure, [Matt Pocock's `skills`](https://github.com/mattpocock/skills) was used as a best-practices reference, especially small composable skills, progressive disclosure, precise context pointers, shared vocabulary, and question-driven throwaway prototypes.

This is an independent project and is not affiliated with Matt Pocock, Anthropic, OpenAI, or the creators of the referenced videos.

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Changes should fix a repeatable agent failure mode, sharpen behavior, or improve installability without bloating always-loaded context.

Run the repository checks with:

```bash
python scripts/validate.py
```

For sensitive reports, follow [SECURITY.md](SECURITY.md) rather than posting exploit details publicly.

## License

MIT. See [LICENSE](LICENSE).
