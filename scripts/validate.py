#!/usr/bin/env python3
"""Dependency-free repository checks for the public skill package."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "product-reasoning"
SKILL = SKILL_DIR / "SKILL.md"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


required = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "ACKNOWLEDGEMENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CONTEXT.md",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    SKILL,
]
for path in required:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

if SKILL.is_file():
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    else:
        parts = text.split("---", 2)
        if len(parts) < 3:
            fail("SKILL.md frontmatter is not closed")
        else:
            frontmatter = parts[1]
            name = re.search(r"(?m)^name:\s*(.+?)\s*$", frontmatter)
            description = re.search(r"(?m)^description:\s*(.+?)\s*$", frontmatter)
            if not name or name.group(1).strip() != "product-reasoning":
                fail("SKILL.md name must be product-reasoning")
            if not description or len(description.group(1).strip()) < 40:
                fail("SKILL.md needs a specific, useful invocation description")

    for target in re.findall(r"\]\((references/[^)#]+\.md)\)", text):
        if not (SKILL_DIR / target).is_file():
            fail(f"broken SKILL.md reference: {target}")

for manifest_name in ["plugin.json", "marketplace.json"]:
    path = ROOT / ".claude-plugin" / manifest_name
    if path.is_file():
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")

plugin = ROOT / ".claude-plugin" / "plugin.json"
if plugin.is_file():
    data = json.loads(plugin.read_text(encoding="utf-8"))
    for rel in data.get("skills", []):
        target = (ROOT / rel).resolve()
        if not target.is_dir() or not (target / "SKILL.md").is_file():
            fail(f"plugin skill path does not resolve to a skill: {rel}")

# Public repo hygiene: company-specific/private material must stay in overlays, not core.
forbidden = ["safaa", "صفاء", "vffjs97", "safaa-sa/"]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    if path.suffix.lower() not in {".md", ".json", ".txt", ".py", ".yml", ".yaml"}:
        continue
    content = path.read_text(encoding="utf-8", errors="ignore").lower()
    for token in forbidden:
        if token.lower() in content:
            fail(f"private/company-specific token found in {path.relative_to(ROOT)}: {token}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("product-reasoning validation passed")
