# Product Reasoning + Arabic Natural Writing

[![validate](https://github.com/SulimanLab/product-reasoning/actions/workflows/validate.yml/badge.svg)](https://github.com/SulimanLab/product-reasoning/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An open-source collection of Agent Skills for coding and product agents.

This repository currently ships two skills:

- **`product-reasoning`** — helps agents reason about outcomes, decisions, timelines, reversibility, prototypes, and product QA before implementation.
- **`arabic-natural-writing`** — helps agents write Arabic from meaning rather than English-shaped structure, with a linguistic foundation drawn from work on **العَرَنجية** and modern Arabic usage.

## Install

### Codex and other Agent Skills clients

Using [skills.sh](https://skills.sh):

```bash
npx skills@latest add SulimanLab/product-reasoning
```

Select either or both skills when prompted.

### Claude Code

The Claude Code plugin bundles both skills:

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

Copy the skill directory you want:

```text
skills/product-reasoning/
skills/arabic-natural-writing/
```

---

## `product-reasoning`

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
- treat a design system as vocabulary, not proof of good UX;
- verify the experience after the code works.

One strong recommendation beats three cosmetic options.

See [`skills/product-reasoning/SKILL.md`](skills/product-reasoning/SKILL.md).

---

## `arabic-natural-writing` — عربية بلا عرنجية

The core rule is simple:

> Write Arabic from **meaning**, not from the source sentence.

The skill diagnoses translation residue across:

- syntax and sentence frames;
- particles and prepositions;
- morphology;
- semantic calques and collocations;
- imported metaphors and rhetorical rhythm;
- filler and bureaucratic scaffolding.

It deliberately avoids linguistic purism. Modern Arabic terms and constructions remain acceptable when they are natural, precise, established, and useful.

Its operating sequence is:

`meaning → Arabic construction → diagnosis → correction → register → verification`

The primary conceptual reference is أحمد الغامدي's **العَرَنجية: بلسان عربي هجين**, with explicit guardrails against turning the subject into a blacklist or overcorrection exercise. `AbadLife/ux-araby` was also used as a practical Agent Skill reference.

See:

- [`skills/arabic-natural-writing/SKILL.md`](skills/arabic-natural-writing/SKILL.md)
- [`skills/arabic-natural-writing/SOURCES.md`](skills/arabic-natural-writing/SOURCES.md)
- [`skills/arabic-natural-writing/examples/GOLD-STANDARD.md`](skills/arabic-natural-writing/examples/GOLD-STANDARD.md)

---

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
skills/
  product-reasoning/
    SKILL.md
    references/
    examples/
  arabic-natural-writing/
    SKILL.md
    SOURCES.md
    ACKNOWLEDGEMENTS.md
    references/
    examples/
    tests/
ACKNOWLEDGEMENTS.md
CODE_OF_CONDUCT.md
CONTEXT.md
CONTRIBUTING.md
SECURITY.md
LICENSE
```

## Design philosophy

Both skills follow the same authoring principle: keep the root `SKILL.md` focused on execution and load deeper references only when they matter.

The repository is intentionally product-agnostic. Company-specific context, design systems, private terminology, and domain policy should live in local overlays rather than the public core.

## Origins and inspiration

For `product-reasoning`, see [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md), including the product-design videos that shaped the reasoning model and Matt Pocock's `skills` repository as a skill-authoring reference.

For `arabic-natural-writing`, see its [SOURCES.md](skills/arabic-natural-writing/SOURCES.md) and [ACKNOWLEDGEMENTS.md](skills/arabic-natural-writing/ACKNOWLEDGEMENTS.md).

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Run the repository checks with:

```bash
python scripts/validate.py
```

For sensitive reports, follow [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
