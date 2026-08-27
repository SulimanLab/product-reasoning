---
name: arabic-natural-writing
description: Write, rewrite, localize, and review Arabic so it reads as Arabic rather than English-shaped Arabic. Use for Arabic UX copy, product text, emails, captions, articles, guides, help text, notifications, localization, or any Arabic draft that feels translated, bureaucratic, stiff, or عرنجي. Diagnose foreign influence in syntax, particles, morphology, semantics, collocations, metaphors, and discourse structure; then rewrite from meaning using Arabic-native resources. Do not enforce linguistic purity: keep familiar modern terms and constructions when they are natural, precise, and useful.
---

# Arabic Natural Writing — عربية بلا عرنجية

Write Arabic from **meaning**, not from the source sentence.

Use this order:

`meaning → Arabic construction → diagnosis → correction → register → verification`

## 1. Reconstruct before editing

First state the intended meaning mentally in plain terms. Then ask:

- How would Arabic normally carry this meaning?
- Does Arabic need the same subject, pronoun, noun phrase, preposition, transition, tense marker, or metaphor?
- Can Arabic express the idea more directly through a verb, derivation, particle, or word order?

If the Arabic sentence mirrors the source too closely, do not patch it word by word. Rewrite it.

Read [references/FOUNDATIONS.md](references/FOUNDATIONS.md) when the task needs the linguistic basis.

## 2. Diagnose the type of residue

Classify the issue before fixing it:

1. **Syntax / sentence frame** — source-language order or construction.
2. **Particles / relations** — translating prepositions and connectors one-for-one.
3. **Morphology** — replacing an economical Arabic form with a multi-word analytic construction.
4. **Semantics** — an Arabic word carrying a foreign meaning or collocation unnaturally.
5. **Style / metaphor** — translated slogans, metaphors, transitions, or rhetorical rhythm.
6. **Filler / bureaucracy** — nominalization and scaffolding that Arabic does not need.

Read [references/DIAGNOSTICS.md](references/DIAGNOSTICS.md).

## 3. Prefer Arabic's own resources

Before importing a source-language structure, test whether Arabic already has a lighter tool:

- a direct verb instead of `القيام بـ + مصدر`;
- an attached pronoun instead of `الخاص بك`;
- `إذا` / `إن` when the relation is conditional rather than temporal;
- a direct preposition or a different sentence frame instead of translating `through`, `against`, `toward`, `for`, or `in case` mechanically;
- a native derived form where it is genuinely natural;
- `أفعل` where it is more natural than `الأكثر + مصدر/صفة`;
- Arabic word order instead of copying English subject-first structure.

Read [references/SYNTAX-AND-MORPHOLOGY.md](references/SYNTAX-AND-MORPHOLOGY.md).

## 4. Treat suspicious words as signals, not automatic bans

A word may be Arabic and still carry an imported meaning. A modern usage may also be completely acceptable.

Do not condemn words by etymology. Judge the **actual sentence**.

For terms, collocations, metaphors, and modern usage, read [references/SEMANTICS-AND-USAGE.md](references/SEMANTICS-AND-USAGE.md).

## 5. Fit the register

Default:

**فصحى معاصرة طبيعية، قريبة من الكلام دون أن تصبح عامية.**

Do not make text archaic to make it “more Arabic.” Do not inject dialect merely to make it “local.”

Read [references/REGISTER.md](references/REGISTER.md).

## 6. Review with three outcomes

- 🔴 **غيّرها** — foreign frame, wrong nuance, or clearly unnatural Arabic.
- 🟡 **حسّنها إن أمكن** — understandable but heavy, padded, or needlessly translated.
- 🟢 **اتركها** — natural and clear. Do not rewrite for novelty or purity.

## 7. Use the back-translation smell test

As a diagnostic only:

> If the Arabic maps unusually cleanly back into the source language word-for-word and in the same order, inspect it for a borrowed frame.

This is **not proof** of عرنجية. It is a prompt to look again.

## 8. Product writing must survive production

For UX text, preserve placeholders, plural logic, bidi/RTL behavior, product names, currency, and technical tokens.

Read [references/PRODUCT-AND-PRODUCTION.md](references/PRODUCT-AND-PRODUCTION.md).

## 9. Examples are normative

When an abstract rule and a natural example pull in different directions, prefer the natural example unless correctness or meaning would break.

Read [examples/GOLD-STANDARD.md](examples/GOLD-STANDARD.md).

## Output behavior

For a single rewrite, lead with the answer:

`الأفضل: ...`

Explain only when the reason matters.

For an audit, group by 🔴 / 🟡 / 🟢 and keep commentary compact.

## Final rule

> The goal is not Arabic that is “translated well.” The goal is Arabic that no longer feels translated.
