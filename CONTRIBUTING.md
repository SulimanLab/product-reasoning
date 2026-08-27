# Contributing

Contributions are welcome. By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## What belongs here

Prefer changes that improve agent behavior across products, not rules specific to one company's workflow or design system.

Good contributions usually:

- fix a repeatable agent failure mode;
- sharpen a trigger or completion criterion;
- reduce permission-seeking or verbosity;
- improve product-state reasoning;
- add a genuinely different example;
- make the skill easier to install or adapt.

## Keep the hierarchy healthy

The root `SKILL.md` should remain short enough to act as an execution path. Branch-specific rules belong in `references/` behind a clear pointer.

Before adding a rule, ask whether it changes behavior versus the model's default. If not, it is probably a no-op.

Avoid duplicating the same meaning across files. Prefer one source of truth plus a short pointer.

## Development

Fork or branch from `main`, make the smallest coherent change, then run:

```bash
python scripts/validate.py
```

If behavior changes, add or update an example that makes the difference observable. If installation changes, update the README and plugin metadata together.

## Pull requests

Use the pull request template and explain:

1. the failure mode you observed;
2. the behavior you want instead;
3. why the rule belongs at its chosen level (root vs reference vs example/tooling);
4. one example showing the change.

Keep unrelated cleanup out of the same PR. Smaller changes are easier to evaluate against the behavior they intend to improve.

## Security

Do not include secrets, private product data, or exploit details in issues or pull requests. Follow [SECURITY.md](SECURITY.md) for sensitive reports.
