# Security Policy

## Supported versions

Security fixes are applied to the latest version on `main`. Once releases exist, only the latest release line will be supported unless stated otherwise.

## What counts as a security issue

This repository contains agent instructions rather than a network service, but security still matters. Please report issues such as:

- instructions that could cause an agent to expose secrets or private project data;
- unsafe handling of untrusted repository, document, or tool content;
- installation or plugin metadata that executes or requests more access than documented;
- accidental inclusion of private or company-specific information in the public package;
- a reproducible path that makes the skill bypass an agent's normal safety or permission boundaries.

Ordinary product disagreements, prompt-quality suggestions, and behavioral improvements belong in normal issues.

## Reporting

Do not publish exploit details, secrets, private data, or proof-of-concept material in a public issue.

If GitHub offers **Report a vulnerability** for this repository, use that private channel. Otherwise, open a minimal issue titled `Security contact requested` with no sensitive details; a maintainer can then arrange a private channel.

Include, privately when possible:

1. the affected file or behavior;
2. the agent/client and version used;
3. minimal reproduction steps;
4. the impact you observed;
5. any mitigation you already tested.

We will acknowledge credible reports as soon as practical and coordinate disclosure after a fix or mitigation is available.
