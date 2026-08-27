#!/usr/bin/env python3
"""Dependency-free repository checks for the public Agent Skills package."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


required_root = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "ACKNOWLEDGEMENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CONTEXT.md",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
]
for path in required_root:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

required_skills = {
    "product-reasoning",
    "arabic-natural-writing",
}

actual_skills = {
    path.name for path in SKILLS_ROOT.iterdir()
    if path.is_dir() and (path / "SKILL.md").is_file()
} if SKILLS_ROOT.is_dir() else set()

for name in sorted(required_skills - actual_skills):
    fail(f"missing required skill: skills/{name}/SKILL.md")

for skill_dir in sorted((SKILLS_ROOT / name for name in actual_skills), key=lambda p: p.name):
    skill = skill_dir / "SKILL.md"
    text = skill.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        fail(f"{skill.relative_to(ROOT)} must start with YAML frontmatter")
        continue

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"{skill.relative_to(ROOT)} frontmatter is not closed")
        continue

    frontmatter = parts[1]
    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", frontmatter)
    description = re.search(r"(?m)^description:\s*(.+?)\s*$", frontmatter)

    if not name_match or name_match.group(1).strip() != skill_dir.name:
        fail(f"{skill.relative_to(ROOT)} name must match directory: {skill_dir.name}")
    if not description or len(description.group(1).strip()) < 40:
        fail(f"{skill.relative_to(ROOT)} needs a specific, useful invocation description")

    for target in re.findall(r"\]\(([^)#]+\.md)\)", text):
        resolved = (skill_dir / target).resolve()
        if skill_dir.resolve() not in resolved.parents and resolved != skill_dir.resolve():
            fail(f"reference escapes skill directory in {skill.relative_to(ROOT)}: {target}")
        elif not resolved.is_file():
            fail(f"broken SKILL.md reference in {skill.relative_to(ROOT)}: {target}")

arabic_skill = SKILLS_ROOT / "arabic-natural-writing"
for rel in [
    "SOURCES.md",
    "ACKNOWLEDGEMENTS.md",
    "examples/GOLD-STANDARD.md",
    "tests/GOLDEN-CASES.md",
    "references/FOUNDATIONS.md",
    "references/DIAGNOSTICS.md",
    "references/SYNTAX-AND-MORPHOLOGY.md",
    "references/SEMANTICS-AND-USAGE.md",
    "references/REGISTER.md",
    "references/PRODUCT-AND-PRODUCTION.md",
]:
    if not (arabic_skill / rel).is_file():
        fail(f"missing arabic-natural-writing reference: {rel}")

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
    manifest_skills = set()
    for rel in data.get("skills", []):
        target = (ROOT / rel).resolve()
        if not target.is_dir() or not (target / "SKILL.md").is_file():
            fail(f"plugin skill path does not resolve to a skill: {rel}")
        else:
            manifest_skills.add(target.name)
    if not required_skills.issubset(manifest_skills):
        fail("plugin.json must expose all required skills")

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

print(f"agent-skills validation passed ({len(actual_skills)} skills)")
