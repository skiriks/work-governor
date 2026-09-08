#!/usr/bin/env python3
"""Check this release's package invariants using Python's standard library.

This is a focused packaging check, not a general YAML/schema validator or a
behavioral test. It never installs plugins or changes Codex configuration.
"""
import hashlib
import json
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/work-governor"
SKILLS = ("work-governor", "research", "writing-for-agents", "chat-management")
RUNTIME = {".codex-plugin/plugin.json", "assets/work-governor.png"}
for skill in SKILLS:
    RUNTIME.update((f"skills/{skill}/SKILL.md", f"skills/{skill}/agents/openai.yaml"))
for reference in ("domain-modeling", "project-continuity", "prototype", "prototype-logic", "prototype-ui", "questionnaire"):
    RUNTIME.add(f"skills/work-governor/references/{reference}.md")
RUNTIME.add("skills/writing-for-agents/references/skill-mechanics.md")
EXPECTED = {f"plugins/work-governor/{p}" for p in RUNTIME}
EXPECTED.update({
    ".agents/plugins/marketplace.json", "README.md", "LICENSE",
    "docs/INSTALL.md", "docs/VERIFICATION.md", "examples/OFFLINE-DEMO.md",
    "examples/automation-brief.md", "scripts/check_package.py",
    "plugins/work-governor/LICENSE", "plugins/work-governor/NOTICE.md",
    "plugins/work-governor/LICENSES/MIT-mattpocock.txt",
})
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"Cannot parse {path.relative_to(ROOT)}: {exc}")
        return {}


actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts}
check(actual == EXPECTED, f"File inventory mismatch: missing={sorted(EXPECTED-actual)}, extra={sorted(actual-EXPECTED)}")
for path in ROOT.rglob("*"):
    if ".git" not in path.relative_to(ROOT).parts:
        check(not path.is_symlink(), f"Symlink is not allowed: {path.relative_to(ROOT)}")

manifest = read_json(PLUGIN / ".codex-plugin/plugin.json")
check(manifest.get("name") == "work-governor", "Incorrect plugin name")
check(manifest.get("version") == "0.1.3", "Unexpected release version")
check(manifest.get("skills") == "./skills/", "Incorrect bundled skills path")
check(manifest.get("license") == "MIT", "Missing project license metadata")
check(not ({"apps", "mcpServers", "hooks"} & manifest.keys()), "Unexpected runtime dependency")
check(manifest.get("interface", {}).get("displayName") == "Work Governor", "Incorrect display name")
for field in ("composerIcon", "logo"):
    check(manifest.get("interface", {}).get(field) == "./assets/work-governor.png", f"Incorrect icon metadata: {field}")
icon = PLUGIN / "assets/work-governor.png"
if icon.is_file():
    image = icon.read_bytes()
    check(len(image) >= 24 and image[:8] == b"\x89PNG\r\n\x1a\n", "Icon must be a PNG")
    if len(image) >= 24:
        width, height = struct.unpack(">II", image[16:24])
        check(width == height and width >= 1024, "Icon must be square and at least 1024 pixels")
check('src="plugins/work-governor/assets/work-governor.png"' in (ROOT / "README.md").read_text(), "README icon path differs from bundled asset")
check(manifest.get("repository") == "https://github.com/skiriks/work-governor", "Incorrect repository metadata")
marketplace = read_json(ROOT / ".agents/plugins/marketplace.json")
check(marketplace.get("name") == "skiriks-work-governor", "Incorrect marketplace identity")
entries = marketplace.get("plugins", [])
check(len(entries) == 1, "Marketplace must expose exactly one plugin")
if len(entries) == 1:
    entry = entries[0]
    check(entry.get("name") == "work-governor", "Marketplace plugin name mismatch")
    check(entry.get("source") == {"source": "local", "path": "./plugins/work-governor"}, "Marketplace path must resolve from repo root")
    check(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Unexpected install policy")
    check(entry.get("category") == "Productivity", "Missing marketplace category")

for skill in SKILLS:
    folder = PLUGIN / "skills" / skill
    if not (folder / "SKILL.md").is_file():
        continue
    text = (folder / "SKILL.md").read_text()
    header = re.match(r"\A---\nname: ([a-z-]+)\ndescription: ([^\n]+)\n---\n", text)
    check(bool(header) and header[1] == skill, f"Invalid expected simple frontmatter: {skill}")
    metadata = (folder / "agents/openai.yaml").read_text()
    check('allow_implicit_invocation: true' in metadata, f"Discovery policy changed: {skill}")
    check('display_name: "' in metadata and 'short_description: "' in metadata, f"Missing UI metadata: {skill}")
    for line in metadata.splitlines():
        if "default_prompt:" in line:
            check(f"${skill}" in line, f"Skill starter missing direct skill reference: {skill}")

links = 0
private_patterns = [r"/Us" + r"ers/", r"/private/" + r"tmp/", r"plugin://work-governor@" + r"personal", r"\.codex-backups", r"ghp_[A-Za-z0-9]{20,}", r"sk-proj-[A-Za-z0-9_-]{20,}"]
for relative in sorted(actual):
    path = ROOT / relative
    if path.suffix not in (".md", ".json", ".yaml", ".txt"):
        continue
    content = path.read_text()
    for pattern in private_patterns:
        check(not re.search(pattern, content), f"Potential private or nonportable content: {relative}")
    if path.suffix == ".md":
        for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", content):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            check(ROOT in resolved.parents and resolved.is_file(), f"Missing or escaping link in {relative}: {target}")
            if path.is_relative_to(PLUGIN / "skills"):
                check(PLUGIN in resolved.parents, f"Runtime reference escapes installed plugin: {relative}")
            links += 1

if (PLUGIN / "LICENSE").is_file():
    check((ROOT / "LICENSE").read_bytes() == (PLUGIN / "LICENSE").read_bytes(), "Installed project license differs")
upstream = PLUGIN / "LICENSES/MIT-mattpocock.txt"
if upstream.is_file():
    check("Copyright (c) 2026 Matt Pocock" in upstream.read_text(), "Upstream copyright missing")

if errors:
    print("FAIL\n" + "\n".join(f"- {error}" for error in errors))
    sys.exit(1)
fingerprint = hashlib.sha256("\n".join(f"{p}:{hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}" for p in sorted(actual)).encode()).hexdigest()
print(f"PASS: {len(actual)} selected files; {len(RUNTIME)} runtime files; 4 skills; {links} local links.")
print(f"Content fingerprint: {fingerprint}")
print("Not tested by this command: installation, host discovery, Desktop invocation, or model behavior.")
