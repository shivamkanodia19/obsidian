#!/usr/bin/env python3
"""
Vault-aware audit backend for the save-audit skill.

The agent performs topic-specific reasoning and note updates first.
This script then refreshes active index files, seeds frontmatter where needed,
checks root guidance, logs broken links, and optionally commits changes.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


VAULT_ROOT = Path("c:/Users/shiva/obsidian")
SKILL_ROOT = Path(__file__).resolve().parent.parent
ANALYST_DIR = VAULT_ROOT / "02_Analyst"
REFS_DIR = VAULT_ROOT / "03_References"
OUTPUTS_DIR = VAULT_ROOT / "05_Outputs"
ACTIVE_INDEX_DIRS = [ANALYST_DIR, REFS_DIR, OUTPUTS_DIR]
ACTIVE_LINK_SCAN_DIRS = [ANALYST_DIR, REFS_DIR, OUTPUTS_DIR]
MEMORY_DIR = Path("c:/Users/shiva/.claude/projects/c--Users-shiva-obsidian/memory")
MEMORY_INDEX = MEMORY_DIR / "MEMORY.md"
BROKEN_LINKS_LOG = VAULT_ROOT / ".vault-broken-links.md"
CONTRADICTIONS_LOG = VAULT_ROOT / ".vault-contradictions.md"
DUPLICATE_STEM_POLICY = SKILL_ROOT / "references" / "DUPLICATE-STEM-POLICY.json"
ROOT_GUIDANCE_FILES = [VAULT_ROOT / "INDEX.md", VAULT_ROOT / "CLAUDE.md"]
TOP_HUBS = [
    ANALYST_DIR / "_index.md",
    REFS_DIR / "_index.md",
    OUTPUTS_DIR / "_index.md",
]
MAX_INDEX_LINES = 120
ARCHIVE_SESSION_DAYS = 30
STALE_CONFLICT_DAYS = 5
IGNORED_SOURCE_PREFIXES = (
    ".trash/",
    ".obsidian/",
    ".codex_scratch/",
    "04_Archive/",
)
IGNORED_NAV_FOLDER_NAMES = {
    "node_modules",
    "artifacts",
    "charts",
}
AGENT_INBOX_GENERATED_DIRS = {
    "completed",
    "failed",
    "logs",
    "pending",
    "processing",
    "result-outbox",
    "runs",
    "test-artifacts",
}
IGNORED_TARGET_PREFIXES = (
    ".trash/",
    ".obsidian/",
    ".codex_scratch/",
)
IGNORED_ROOT_FILES = {
    "CLAUDE.original.md",
}
ROOT_AUTO_INDEX_SKIP_FILE_GLOBS = (
    "02_Analyst/codex-chat-save-audit-*.md",
    "02_Analyst/vault-audit-*.md",
    "02_Analyst/GRAPH_REPORT.md",
)
AUDIT_FILE_PATTERNS = {
    "codex-chat-save-audit": "02_Analyst/codex-chat-save-audit-*.md",
    "vault-audit": "02_Analyst/vault-audit-*.md",
}
TRUTH_CLAIM_PHRASES = (
    "source of truth",
    "canonical note",
)
TASK_CONTEXT_REQUIRED_SCALARS = (
    "project",
    "scope",
    "status",
)
TASK_CONTEXT_REQUIRED_LISTS = (
    "current_focus",
    "active_tasks",
    "prompt_context",
    "definition_of_done",
)
IGNORED_SOURCE_GLOBS = (
    "02_Analyst/codex-chat-save-audit-*.md",
    "02_Analyst/GRAPH_REPORT.md",
    "02_Analyst/tasks/*template*.md",
    "02_Analyst/run-logs/*template*.md",
)


SPECIAL_INDEX_METADATA = {
    "02_Analyst": (
        "Analyst Index",
        "Core synthesis layer for reasoning, writing, research, outreach, and decision support",
    ),
    "03_References": (
        "References Index",
        "Reusable frameworks, tools, patterns, and best practices",
    ),
    "05_Outputs": (
        "Outputs Index",
        "User-requested deliverables organized by project and output type",
    ),
    "02_Analyst/tasks": (
        "Task System",
        "Structured task specs for major agent work",
    ),
    "02_Analyst/run-logs": (
        "Run Logs",
        "Structured execution breadcrumbs for significant agent runs",
    ),
}


@dataclass
class AuditReport:
    indexes_created: int = 0
    indexes_updated: int = 0
    broken_links: int = 0
    brittle_index_links: int = 0
    root_warnings: int = 0
    empty_folders: int = 0
    oversize_indexes: int = 0
    memory_lines: int = 0
    memory_exists: bool = False
    open_conflicts: int = 0
    pending_validation_conflicts: int = 0
    closed_conflicts: int = 0
    truth_collisions: int = 0
    alias_collisions: int = 0
    duplicate_note_stems: int = 0
    intentional_duplicate_stems: int = 0
    scoped_duplicate_stems: int = 0
    duplicate_index_headings: int = 0
    task_context_indexes: int = 0
    task_context_indexes_needing_review: int = 0
    task_context_drifted_indexes: int = 0


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def rel(path: Path) -> str:
    return str(path.relative_to(VAULT_ROOT)).replace("\\", "/")


def relative_parts(path: Path) -> tuple[str, ...]:
    try:
        return path.relative_to(VAULT_ROOT).parts
    except ValueError:
        return path.parts


def yaml_quote(value: str) -> str:
    return '"' + value.replace('"', "'") + '"'


def pretty_name(name: str) -> str:
    return name.replace("_", " ").replace("-", " ").strip().title()


def default_title(folder: Path) -> str:
    key = rel(folder)
    if key in SPECIAL_INDEX_METADATA:
        return SPECIAL_INDEX_METADATA[key][0]
    return pretty_name(folder.name)


def default_description(folder: Path) -> str:
    key = rel(folder)
    if key in SPECIAL_INDEX_METADATA:
        return SPECIAL_INDEX_METADATA[key][1]
    return f"Navigation hub for {folder.name.replace('_', ' ').replace('-', ' ')}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_command(args: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            cwd=VAULT_ROOT,
        )
        return result.returncode == 0, (result.stdout + result.stderr).strip()
    except Exception as exc:
        return False, str(exc)


def should_ignore_source_file(path: Path) -> bool:
    relative = rel(path)
    if relative.startswith(IGNORED_SOURCE_PREFIXES):
        return True
    if should_ignore_navigation_path(path):
        return True
    return any(fnmatch.fnmatch(relative, pattern) for pattern in IGNORED_SOURCE_GLOBS)


def should_ignore_navigation_path(path: Path) -> bool:
    parts = relative_parts(path)
    return any(part in IGNORED_NAV_FOLDER_NAMES for part in parts)


def has_part_sequence(parts: tuple[str, ...], sequence: tuple[str, ...]) -> bool:
    if len(parts) < len(sequence):
        return False
    for start in range(len(parts) - len(sequence) + 1):
        if parts[start : start + len(sequence)] == sequence:
            return True
    return False


def classify_path(path: Path) -> str:
    parts = relative_parts(path)
    if not parts:
        return "navigable"
    if parts[0] == "04_Archive":
        return "archive"
    if parts[0] == "05_Outputs" and has_part_sequence(parts, ("pipeline", "runs")):
        return "generated_artifact"
    if parts[0] == "05_Outputs":
        for index, part in enumerate(parts[:-1]):
            if part != "agent-inbox":
                continue
            if parts[index + 1] in AGENT_INBOX_GENERATED_DIRS:
                return "generated_artifact"
    return "navigable"


def should_skip_index_maintenance(path: Path) -> bool:
    return should_ignore_navigation_path(path) or classify_path(path) == "generated_artifact"


def should_skip_auto_index_file(folder: Path, file_path: Path) -> bool:
    if folder != ANALYST_DIR:
        return False
    return any(fnmatch.fnmatch(rel(file_path), pattern) for pattern in ROOT_AUTO_INDEX_SKIP_FILE_GLOBS)


def split_frontmatter(content: str) -> tuple[str | None, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", content, re.DOTALL)
    if not match:
        return None, content
    return match.group(1), content[match.end():]


def parse_frontmatter_fields(content: str) -> dict[str, str]:
    fm, _ = split_frontmatter(content)
    if fm is None:
        return {}

    fields: dict[str, str] = {}
    for raw_line in fm.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def strip_yaml_scalar(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse_inline_list(value: str) -> list[str]:
    trimmed = value.strip()
    if not trimmed.startswith("[") or not trimmed.endswith("]"):
        return []
    inner = trimmed[1:-1].strip()
    if not inner:
        return []
    return [strip_yaml_scalar(item) for item in inner.split(",") if item.strip()]


def parse_frontmatter_data(content: str) -> tuple[list[str], dict[str, Any], str]:
    fm, body = split_frontmatter(content)
    if fm is None:
        return [], {}, body

    order: list[str] = []
    data: dict[str, Any] = {}
    current_field: str | None = None

    for raw_line in fm.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith((" ", "\t")):
            if current_field is None:
                continue
            item_match = re.match(r"^\s*-\s*(.+?)\s*$", raw_line)
            if item_match:
                if not isinstance(data.get(current_field), list):
                    data[current_field] = []
                data[current_field].append(strip_yaml_scalar(item_match.group(1)))
            continue

        current_field = None
        block_match = re.match(r"^([A-Za-z0-9_-]+):\s*$", raw_line)
        if block_match:
            key = block_match.group(1)
            current_field = key
            if key not in order:
                order.append(key)
            data[key] = []
            continue

        scalar_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", raw_line)
        if not scalar_match:
            continue

        key = scalar_match.group(1)
        value = scalar_match.group(2)
        if key not in order:
            order.append(key)

        inline_items = parse_inline_list(value)
        if inline_items or value.strip() == "[]":
            data[key] = inline_items
        else:
            data[key] = strip_yaml_scalar(value)

    return order, data, body


def yaml_scalar(value: str) -> str:
    if value.lower() in {"true", "false", "null"}:
        return value.lower()
    if re.fullmatch(r"-?\d+(?:\.\d+)?", value):
        return value
    if re.fullmatch(r"[A-Za-z0-9_./-]+", value):
        return value
    return yaml_quote(value)


def render_frontmatter_data(order: list[str], data: dict[str, Any], body: str) -> str:
    lines = ["---"]
    rendered_keys = list(order)
    for key in data:
        if key not in rendered_keys:
            rendered_keys.append(key)

    for key in rendered_keys:
        value = data[key]
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {yaml_scalar(str(item))}")
        else:
            lines.append(f"{key}: {yaml_scalar(str(value))}")

    lines.extend(["---", "", body.lstrip()])
    return "\n".join(lines).rstrip() + "\n"


def parse_frontmatter_list_fields(
    content: str,
    target_fields: set[str] | None = None,
) -> dict[str, list[str]]:
    fm, _ = split_frontmatter(content)
    if fm is None:
        return {}

    fields: dict[str, list[str]] = {}
    current_field: str | None = None

    for raw_line in fm.splitlines():
        if not raw_line.strip():
            continue

        if not raw_line.startswith((" ", "\t")):
            block_match = re.match(r"^([A-Za-z0-9_-]+):\s*$", raw_line)
            if block_match:
                key = block_match.group(1)
                current_field = key if target_fields is None or key in target_fields else None
                if current_field is not None:
                    fields.setdefault(current_field, [])
                continue

            scalar_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", raw_line)
            if scalar_match:
                key = scalar_match.group(1)
                current_field = None
                if target_fields is None or key in target_fields:
                    inline_items = parse_inline_list(scalar_match.group(2))
                    if inline_items or scalar_match.group(2).strip() == "[]":
                        fields[key] = inline_items
                continue

            current_field = None
            continue

        if current_field is None:
            continue

        item_match = re.match(r"^\s*-\s*(.+?)\s*$", raw_line)
        if item_match:
            fields.setdefault(current_field, []).append(strip_yaml_scalar(item_match.group(1)))

    return fields


def load_duplicate_stem_policy() -> dict:
    default_policy = {
        "redirect_markers": [
            "canonical note:",
            "stable redirect",
            "redirect stub",
            "legacy alias",
            "preferred canonical folder",
            "do not create new",
        ],
        "rules": [],
    }
    if not DUPLICATE_STEM_POLICY.exists():
        return default_policy

    try:
        loaded = json.loads(read_text(DUPLICATE_STEM_POLICY))
    except Exception:
        return default_policy

    if not isinstance(loaded, dict):
        return default_policy

    return {
        "redirect_markers": loaded.get("redirect_markers", default_policy["redirect_markers"]),
        "rules": loaded.get("rules", []),
    }


def ensure_frontmatter(content: str, index_path: Path, stamp: str) -> tuple[str, bool]:
    fm, body = split_frontmatter(content)
    if fm is None:
        frontmatter = (
            "---\n"
            f"title: {yaml_quote(default_title(index_path.parent))}\n"
            f"description: {yaml_quote(default_description(index_path.parent))}\n"
            f"last_updated: {stamp}\n"
            "---\n\n"
        )
        return frontmatter + body.lstrip(), True

    changed = False
    updated_fm = fm

    if not re.search(r"(?m)^title:\s*", updated_fm):
        updated_fm = f'title: {yaml_quote(default_title(index_path.parent))}\n' + updated_fm
        changed = True

    if not re.search(r"(?m)^description:\s*", updated_fm):
        updated_fm = (
            f'description: {yaml_quote(default_description(index_path.parent))}\n' + updated_fm
        )
        changed = True

    if not re.search(r"(?m)^last_updated:\s*", updated_fm):
        updated_fm = updated_fm.rstrip() + f"\nlast_updated: {stamp}"
        changed = True

    rebuilt = f"---\n{updated_fm.strip()}\n---\n\n{body.lstrip()}"
    return rebuilt, changed


def bump_last_updated(content: str, stamp: str) -> str:
    fm, body = split_frontmatter(content)
    if fm is None:
        return content
    if re.search(r"(?m)^last_updated:\s*", fm):
        fm = re.sub(r"(?m)^last_updated:\s*.*$", f"last_updated: {stamp}", fm)
    else:
        fm = fm.rstrip() + f"\nlast_updated: {stamp}"
    return f"---\n{fm.strip()}\n---\n\n{body.lstrip()}"


def normalize_rooted_links(content: str) -> tuple[str, int]:
    count = len(re.findall(r"\[\[/", content))
    if count == 0:
        return content, 0
    return re.sub(r"\[\[/+", "[[", content), count


def extract_wikilinks(content: str) -> list[str]:
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]*?)?\]\]", content)


def build_vault_targets() -> set[str]:
    targets: set[str] = set()
    for file_path in VAULT_ROOT.rglob("*"):
        if not file_path.is_file():
            continue
        if should_ignore_navigation_path(file_path):
            continue
        relative = rel(file_path)
        if relative.startswith(IGNORED_TARGET_PREFIXES):
            continue
        targets.add(relative)
        targets.add(file_path.name)
        if file_path.suffix:
            targets.add(relative.removesuffix(file_path.suffix))
        if file_path.stem:
            targets.add(file_path.stem)
    for base_dir in ACTIVE_INDEX_DIRS:
        if not base_dir.exists():
            continue
        for folder in [base_dir] + [d for d in base_dir.rglob("*") if d.is_dir()]:
            if should_ignore_navigation_path(folder):
                continue
            index_md = folder / "_index.md"
            index_rel = rel(index_md)
            targets.add(index_rel)
            targets.add(index_rel.removesuffix(".md"))
            targets.add(folder.name)
            targets.add(f"{folder.name}/")
    return targets


def sanitize_markdown_for_link_scan(content: str) -> str:
    sanitized = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    sanitized = re.sub(r"~~~.*?~~~", "", sanitized, flags=re.DOTALL)
    sanitized = re.sub(r"`[^`\n]+`", "", sanitized)
    return sanitized


def normalize_link_target(link: str) -> str | None:
    norm = link.strip().replace("\\", "/")
    if not norm:
        return None
    if norm.startswith(("http://", "https://", "mailto:")):
        return None
    if "..." in norm:
        return None
    if "[" in norm or "]" in norm:
        return None
    norm = norm.split("#", 1)[0]
    norm = norm.split("^", 1)[0]
    norm = norm.strip()
    if not norm:
        return None
    return norm


def link_resolves(link: str, all_targets: set[str]) -> bool:
    norm = normalize_link_target(link)
    if norm is None:
        return True
    return (
        norm in all_targets
        or (norm + ".md") in all_targets
        or any(target.endswith("/" + norm) for target in all_targets)
        or any(target.endswith("/" + norm + ".md") for target in all_targets)
    )


def link_points_to_folder(link: str, folder: Path) -> bool:
    norm = link.strip().replace("\\", "/")
    candidates = {
        folder.name,
        f"{folder.name}/",
        f"{folder.name}/_index",
        f"{folder.name}/_index.md",
        rel(folder / "_index"),
        rel(folder / "_index.md"),
    }
    return norm in candidates or norm.endswith(f"/{folder.name}/_index") or norm.endswith(
        f"/{folder.name}/_index.md"
    )


def link_points_to_file(link: str, file_path: Path) -> bool:
    norm = link.strip().replace("\\", "/")
    candidates = {
        file_path.stem,
        file_path.name,
        rel(file_path),
        rel(file_path).removesuffix(".md"),
    }
    return norm in candidates or norm.endswith("/" + file_path.stem) or norm.endswith(
        "/" + file_path.name
    )


def extract_file_description(file_path: Path) -> str:
    try:
        content = read_text(file_path)
    except Exception:
        return ""
    fm, body = split_frontmatter(content)
    if fm:
        for field in ("description", "title"):
            match = re.search(
                rf'(?m)^{field}:\s*["\']?(.+?)["\']?\s*$',
                fm,
            )
            if match:
                return match.group(1).strip()[:100]
    h1 = re.search(r"(?m)^#\s+(.+)$", body)
    if h1:
        return h1.group(1).strip()[:100]
    return ""


def scan_conflict_entries() -> list[dict[str, str | datetime | None]]:
    conflict_file = VAULT_ROOT / ".vault-conflicts"
    if not conflict_file.exists():
        return []

    content = read_text(conflict_file)
    if "## Recent Conflicts" not in content:
        return []

    recent = content.split("## Recent Conflicts", 1)[1]
    recent = recent.split("## Archive", 1)[0]
    raw_blocks = [block.strip() for block in re.split(r"(?m)^###\s+", recent) if block.strip()]
    entries: list[dict[str, str | datetime | None]] = []

    for block in raw_blocks:
        lines = block.splitlines()
        heading = lines[0].strip()
        body = "\n".join(lines[1:])
        status_match = re.search(
            r"(?im)^(?:\*\*Status:\*\*|Status:)\s*([A-Za-z_]+)",
            body,
        )
        if not status_match:
            continue

        status = status_match.group(1).lower()
        if status == "supported_by_example":
            status = "resolved"

        timestamp: datetime | None = None
        timestamp_match = re.search(r"\[(\d{4}-\d{2}-\d{2})(?:\s+(\d{2}:\d{2}))?\]", heading)
        if timestamp_match:
            raw_time = timestamp_match.group(2) or "00:00"
            try:
                timestamp = datetime.strptime(
                    f"{timestamp_match.group(1)} {raw_time}",
                    "%Y-%m-%d %H:%M",
                )
            except ValueError:
                timestamp = None

        entries.append(
            {
                "heading": heading,
                "status": status,
                "timestamp": timestamp,
            }
        )

    return entries


def scan_conflict_queue() -> dict[str, int]:
    open_count = 0
    pending_validation = 0
    closed_count = 0
    for entry in scan_conflict_entries():
        status = str(entry["status"])
        if status == "awaiting_review":
            open_count += 1
        elif status == "pending_validation":
            open_count += 1
            pending_validation += 1
        elif status in {"resolved", "archived", "acknowledged"}:
            closed_count += 1

    return {
        "open": open_count,
        "pending_validation": pending_validation,
        "closed": closed_count,
    }


def format_conflict_ref(entry: dict[str, str | datetime | None]) -> str:
    heading = str(entry["heading"])
    return heading


def scan_duplicate_index_headings() -> dict[str, int]:
    issues: dict[str, int] = {}
    for base_dir in ACTIVE_INDEX_DIRS:
        if not base_dir.exists():
            continue
        for index_path in base_dir.rglob("_index.md"):
            if should_skip_index_maintenance(index_path):
                continue
            content = read_text(index_path)
            count = len(re.findall(r"(?m)^## New Files\s*$", content))
            if count > 1:
                issues[rel(index_path)] = count
    return issues


def scan_alias_folder_collisions() -> dict[str, list[str]]:
    collisions: dict[str, list[str]] = {}
    for base_dir in [ANALYST_DIR, REFS_DIR]:
        if not base_dir.exists():
            continue
        parents = [base_dir] + [
            folder
            for folder in base_dir.rglob("*")
            if folder.is_dir() and not should_ignore_navigation_path(folder)
        ]
        for parent in parents:
            children = [
                child
                for child in parent.iterdir()
                if child.is_dir() and not should_ignore_navigation_path(child)
            ]
            normalized: dict[str, list[Path]] = {}
            for child in children:
                key = child.name.lower().replace(" ", "-").replace("_", "-")
                normalized.setdefault(key, []).append(child)

            sibling_collisions = [
                " | ".join(sorted(item.name for item in group))
                for group in normalized.values()
                if len(group) > 1
            ]
            if sibling_collisions:
                collisions[rel(parent)] = sibling_collisions
    return collisions


def path_matches_globs(path_string: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(path_string, glob) for glob in globs)


def looks_like_redirect_stub(path: Path, content: str, redirect_markers: list[str], siblings: list[Path]) -> bool:
    lower_content = content.lower()
    if not any(marker.lower() in lower_content for marker in redirect_markers):
        return False

    meaningful_lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(meaningful_lines) > 12:
        return False

    sibling_depths = [len(rel(item).split("/")) for item in siblings if item != path]
    return bool(sibling_depths) and len(rel(path).split("/")) == min(len(rel(item).split("/")) for item in siblings)


def classify_duplicate_stem(stem: str, paths: list[Path], policy: dict) -> tuple[str, str]:
    path_strings = [rel(path) for path in sorted(paths, key=lambda item: str(item).lower())]
    contents = {path_string: read_text(VAULT_ROOT / path_string) for path_string in path_strings}

    for rule in policy.get("rules", []):
        if rule.get("stem") != stem:
            continue

        required_paths = set(rule.get("required_paths", []))
        if required_paths and not required_paths.issubset(set(path_strings)):
            continue

        path_globs = rule.get("path_globs", [])
        if path_globs and not all(path_matches_globs(path_string, path_globs) for path_string in path_strings):
            continue

        exact_count = rule.get("exact_count")
        if exact_count is not None and len(path_strings) != exact_count:
            continue

        required_markers = [marker.lower() for marker in rule.get("required_markers", [])]
        if required_markers:
            if not any(all(marker in contents[path_string].lower() for marker in required_markers) for path_string in path_strings):
                continue

        return rule.get("classification", "review_candidate"), rule.get("reason", "Matched duplicate-stem policy.")

    redirect_markers = policy.get("redirect_markers", [])
    if len(paths) == 2:
        for path in paths:
            path_string = rel(path)
            content = contents[path_string]
            if looks_like_redirect_stub(path, content, redirect_markers, paths):
                return "intentional_redirect", "Redirect-stub heuristic matched: short note with canonical redirect markers."

    return "review_candidate", "No duplicate-stem policy rule matched."


def scan_duplicate_note_stems(policy: dict) -> dict[str, dict[str, dict[str, str | list[str]]]]:
    by_stem: dict[str, list[Path]] = {}
    for base_dir in ACTIVE_INDEX_DIRS:
        if not base_dir.exists():
            continue
        for md_file in base_dir.rglob("*.md"):
            if md_file.name == "_index.md" or should_skip_index_maintenance(md_file):
                continue
            by_stem.setdefault(md_file.stem.lower(), []).append(md_file)

    duplicates: dict[str, dict[str, dict[str, str | list[str]]]] = {
        "review_candidate": {},
        "intentional_redirect": {},
        "scoped_duplicate": {},
    }
    for stem, paths in by_stem.items():
        if len(paths) > 1:
            classification, reason = classify_duplicate_stem(stem, paths, policy)
            duplicates.setdefault(classification, {})
            duplicates[classification][stem] = {
                "paths": [rel(path) for path in sorted(paths, key=lambda item: str(item).lower())],
                "reason": reason,
            }
    return duplicates


def scan_truth_collisions() -> dict[str, list[str]]:
    collisions: dict[str, list[str]] = {}
    folders = [ANALYST_DIR] + [
        folder
        for folder in ANALYST_DIR.rglob("*")
        if folder.is_dir() and not should_ignore_navigation_path(folder)
    ]
    for folder in folders:
        if folder == ANALYST_DIR:
            continue
        md_files = [path for path in folder.glob("*.md") if path.name != "_index.md"]
        if len(md_files) < 2:
            continue

        grouped: dict[str, list[str]] = {}
        group_counts: dict[str, dict[str, int]] = {}

        for md_file in md_files:
            content = read_text(md_file)
            fields = parse_frontmatter_fields(content)
            markers: list[str] = []
            group_key = fields.get("scope") or rel(folder)

            if fields.get("status", "").lower() == "current":
                markers.append("status=current")
                group_counts.setdefault(group_key, {"current": 0, "claims": 0})["current"] += 1
            if fields.get("canonical", "").lower() == "true":
                markers.append("canonical=true")
                group_counts.setdefault(group_key, {"current": 0, "claims": 0})["claims"] += 1

            lower_content = content.lower()
            for phrase in TRUTH_CLAIM_PHRASES:
                if phrase in lower_content:
                    markers.append(phrase)
                    group_counts.setdefault(group_key, {"current": 0, "claims": 0})["claims"] += 1
                    break

            if markers:
                grouped.setdefault(group_key, []).append(f"{rel(md_file)} ({', '.join(markers)})")

        for group_key, items in grouped.items():
            counts = group_counts.get(group_key, {"current": 0, "claims": 0})
            if len(items) >= 2 and ((counts["current"] >= 2 and counts["claims"] >= 1) or counts["claims"] >= 2):
                collisions[group_key] = items

    return collisions


def scan_task_context_coverage() -> dict[str, list[str] | dict[str, list[str]]]:
    complete: list[str] = []
    needs_review: dict[str, list[str]] = {}
    target_list_fields = set(TASK_CONTEXT_REQUIRED_LISTS)

    for index_path in ANALYST_DIR.rglob("_index.md"):
        if should_ignore_navigation_path(index_path):
            continue

        content = read_text(index_path)
        scalar_fields = parse_frontmatter_fields(content)
        if scalar_fields.get("agent_context", "").lower() != "true":
            continue

        list_fields = parse_frontmatter_list_fields(content, target_fields=target_list_fields)
        missing: list[str] = []

        for field in TASK_CONTEXT_REQUIRED_SCALARS:
            if not scalar_fields.get(field):
                missing.append(field)

        for field in TASK_CONTEXT_REQUIRED_LISTS:
            if not list_fields.get(field):
                missing.append(field)

        if missing:
            needs_review[rel(index_path)] = missing
        else:
            complete.append(rel(index_path))

    return {
        "complete": sorted(complete),
        "needs_review": dict(sorted(needs_review.items())),
    }


def resolve_markdown_target(link: str) -> Path | None:
    raw_link = link.strip()
    wrapper_match = re.match(r"^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]$", raw_link)
    if wrapper_match:
        raw_link = wrapper_match.group(1)

    norm = normalize_link_target(raw_link)
    if norm is None:
        return None

    candidates = [
        VAULT_ROOT / norm,
        VAULT_ROOT / f"{norm}.md",
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def scan_task_context_drift() -> dict[str, list[str]]:
    issues: dict[str, list[str]] = {}
    target_list_fields = {"prompt_context", "task_cards"}
    bad_statuses = {"historical", "snapshot", "superseded", "archived"}

    for index_path in ANALYST_DIR.rglob("_index.md"):
        if should_ignore_navigation_path(index_path):
            continue

        content = read_text(index_path)
        scalar_fields = parse_frontmatter_fields(content)
        if scalar_fields.get("agent_context", "").lower() != "true":
            continue

        list_fields = parse_frontmatter_list_fields(content, target_fields=target_list_fields)
        current_issues: list[str] = []

        for field_name in sorted(target_list_fields):
            for raw_link in list_fields.get(field_name, []):
                target_path = resolve_markdown_target(raw_link)
                if target_path is None:
                    current_issues.append(f"{field_name} -> missing target {raw_link}")
                    continue

                target_fields = parse_frontmatter_fields(read_text(target_path))
                target_status = target_fields.get("status", "").lower()
                if target_status in bad_statuses:
                    current_issues.append(
                        f"{field_name} -> {rel(target_path)} has status {target_status}"
                    )

        if current_issues:
            issues[rel(index_path)] = current_issues

    return dict(sorted(issues.items()))


def build_contradictions_log(
    queue_summary: dict[str, int],
    truth_collisions: dict[str, list[str]],
    alias_collisions: dict[str, list[str]],
    duplicate_stems: dict[str, dict[str, dict[str, str | list[str]]]],
    duplicate_index_headings: dict[str, int],
    task_context_coverage: dict[str, list[str] | dict[str, list[str]]],
    task_context_drift: dict[str, list[str]],
    dry_run: bool,
) -> None:
    review_duplicate_stems = duplicate_stems.get("review_candidate", {})
    intentional_duplicate_stems = duplicate_stems.get("intentional_redirect", {})
    scoped_duplicate_stems = duplicate_stems.get("scoped_duplicate", {})
    task_context_complete = task_context_coverage.get("complete", [])
    task_context_needs_review = task_context_coverage.get("needs_review", {})
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Vault Contradiction Audit",
        f"Generated: {stamp}",
        f"Open conflicts: {queue_summary['open']}",
        f"Pending validation: {queue_summary['pending_validation']}",
        f"Closed conflicts: {queue_summary['closed']}",
        f"Potential current-truth collisions: {len(truth_collisions)}",
        f"Sibling alias-folder collisions: {len(alias_collisions)}",
        f"Duplicate note stems requiring review: {len(review_duplicate_stems)}",
        f"Intentional duplicate stems: {len(intentional_duplicate_stems)}",
        f"Scoped duplicate stems: {len(scoped_duplicate_stems)}",
        f"Indexes with duplicate `## New Files` headings: {len(duplicate_index_headings)}",
        f"Agent-context indexes with full task coverage: {len(task_context_complete)}",
        f"Agent-context indexes needing task review: {len(task_context_needs_review)}",
        f"Agent-context indexes with prompt drift: {len(task_context_drift)}",
        "",
    ]

    if truth_collisions:
        lines.extend(["## Potential Current-Truth Collisions", ""])
        for folder, items in sorted(truth_collisions.items()):
            lines.append(f"### {folder}")
            for item in items:
                lines.append(f"- {item}")
            lines.append("- Recommendation: pick one canonical current note, downrank the rest, and update the nearest `_index.md`.")
            lines.append("")

    if alias_collisions:
        lines.extend(["## Sibling Alias Folders", ""])
        for folder, items in sorted(alias_collisions.items()):
            lines.append(f"### {folder}")
            for item in items:
                lines.append(f"- {item}")
            lines.append("- Recommendation: keep one canonical folder and mark the others as legacy aliases.")
            lines.append("")

    if intentional_duplicate_stems:
        lines.extend(["## Intentional Duplicate Stems", ""])
        for stem, payload in sorted(intentional_duplicate_stems.items()):
            lines.append(f"### {stem}")
            for item in payload["paths"]:
                lines.append(f"- {item}")
            lines.append(f"- Reason: {payload['reason']}")
            lines.append("")

    if scoped_duplicate_stems:
        lines.extend(["## Scoped Duplicate Stems", ""])
        for stem, payload in sorted(scoped_duplicate_stems.items()):
            lines.append(f"### {stem}")
            for item in payload["paths"]:
                lines.append(f"- {item}")
            lines.append(f"- Reason: {payload['reason']}")
            lines.append("")

    if review_duplicate_stems:
        lines.extend(["## Duplicate Note Stems Requiring Review", ""])
        for stem, payload in sorted(review_duplicate_stems.items()):
            lines.append(f"### {stem}")
            for item in payload["paths"]:
                lines.append(f"- {item}")
            lines.append(f"- Reason: {payload['reason']}")
            lines.append("")

    if duplicate_index_headings:
        lines.extend(["## Duplicate Index Sections", ""])
        for index_path, count in sorted(duplicate_index_headings.items()):
            lines.append(f"- `{index_path}` has {count} `## New Files` headings")
        lines.append("")

    if task_context_needs_review:
        lines.extend(["## Task Context Coverage", ""])
        for index_path, missing_fields in sorted(task_context_needs_review.items()):
            rendered = ", ".join(f"`{field}`" for field in missing_fields)
            lines.append(f"- `{index_path}` is missing: {rendered}")
        lines.append("")

    if task_context_drift:
        lines.extend(["## Task Context Drift", ""])
        for index_path, drift_items in sorted(task_context_drift.items()):
            lines.append(f"### {index_path}")
            for item in drift_items:
                lines.append(f"- {item}")
            lines.append("")

    if not any(
        [
            truth_collisions,
            alias_collisions,
            review_duplicate_stems,
            intentional_duplicate_stems,
            scoped_duplicate_stems,
            duplicate_index_headings,
            task_context_needs_review,
            task_context_drift,
        ]
    ):
        lines.append("No contradiction clusters detected beyond the existing queue summary.")

    write_text(CONTRADICTIONS_LOG, "\n".join(lines).rstrip() + "\n", dry_run)


def run_contradiction_audit(report: AuditReport, dry_run: bool) -> None:
    queue_summary = scan_conflict_queue()
    truth_collisions = scan_truth_collisions()
    alias_collisions = scan_alias_folder_collisions()
    duplicate_stem_policy = load_duplicate_stem_policy()
    duplicate_stems = scan_duplicate_note_stems(duplicate_stem_policy)
    duplicate_index_headings = scan_duplicate_index_headings()
    task_context_coverage = scan_task_context_coverage()
    task_context_drift = scan_task_context_drift()

    report.open_conflicts = queue_summary["open"]
    report.pending_validation_conflicts = queue_summary["pending_validation"]
    report.closed_conflicts = queue_summary["closed"]
    report.truth_collisions = len(truth_collisions)
    report.alias_collisions = len(alias_collisions)
    report.duplicate_note_stems = len(duplicate_stems.get("review_candidate", {}))
    report.intentional_duplicate_stems = len(duplicate_stems.get("intentional_redirect", {}))
    report.scoped_duplicate_stems = len(duplicate_stems.get("scoped_duplicate", {}))
    report.duplicate_index_headings = len(duplicate_index_headings)
    report.task_context_indexes = len(task_context_coverage.get("complete", []))
    report.task_context_indexes_needing_review = len(task_context_coverage.get("needs_review", {}))
    report.task_context_drifted_indexes = len(task_context_drift)

    build_contradictions_log(
        queue_summary,
        truth_collisions,
        alias_collisions,
        duplicate_stems,
        duplicate_index_headings,
        task_context_coverage,
        task_context_drift,
        dry_run,
    )


def build_new_index(folder: Path, subdirs: list[Path], files: list[Path], stamp: str) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(default_title(folder))}",
        f"description: {yaml_quote(default_description(folder))}",
        f"last_updated: {stamp}",
        "---",
        "",
        f"# {default_title(folder)}",
        "",
        default_description(folder) + ".",
    ]

    if subdirs:
        lines.extend(["", "## Folders", ""])
        for subdir in subdirs:
            desc = default_description(subdir)
            lines.append(f"- [[{subdir.name}/_index|{subdir.name}/]] - {desc}")

    if files:
        lines.extend(["", "## Files", ""])
        for file_path in files:
            desc = extract_file_description(file_path)
            if desc:
                lines.append(f"- [[{file_path.stem}]] - {desc}")
            else:
                lines.append(f"- [[{file_path.stem}]]")

    lines.append("")
    return "\n".join(lines)


def archive_old_sessions(content: str, folder: Path, dry_run: bool) -> tuple[str, int]:
    cutoff = datetime.now() - timedelta(days=ARCHIVE_SESSION_DAYS)
    parts = re.split(r"(?=^##\s)", content, flags=re.MULTILINE)
    archived: list[str] = []
    kept: list[str] = []

    for part in parts:
        match = re.match(r"^##[^#].*?(\d{4}-\d{2}-\d{2})", part)
        if match:
            try:
                section_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if section_date < cutoff:
                    archived.append(part)
                    continue
            except ValueError:
                pass
        kept.append(part)

    if not archived:
        return content, 0

    archive_dir = VAULT_ROOT / "04_Archive" / folder.name
    archive_path = archive_dir / f"activity-log-archived-{today()}.md"
    archive_header = f"# Archived Activity Log - {folder.name}\nArchived: {today()}\n\n"
    existing = read_text(archive_path) if archive_path.exists() else ""
    write_text(archive_path, existing + archive_header + "".join(archived), dry_run)
    return "".join(kept), len(archived)


def merge_new_files_sections(content: str) -> tuple[str, bool]:
    lines = content.splitlines()
    sections: list[tuple[int, int, list[str]]] = []
    idx = 0

    while idx < len(lines):
        if lines[idx].strip() != "## New Files":
            idx += 1
            continue

        start = idx
        idx += 1
        section_lines: list[str] = []
        while idx < len(lines) and not re.match(r"^##\s+", lines[idx]):
            section_lines.append(lines[idx])
            idx += 1
        sections.append((start, idx, section_lines))

    if len(sections) <= 1:
        return content, False

    merged_items: list[str] = []
    seen: set[str] = set()
    for _, _, section_lines in sections:
        for raw_line in section_lines:
            line = raw_line.rstrip()
            if not line:
                continue
            if line not in seen:
                seen.add(line)
                merged_items.append(line)

    first_start = sections[0][0]
    for start, end, _ in reversed(sections):
        del lines[start:end]

    replacement = ["## New Files", ""]
    replacement.extend(merged_items)
    lines[first_start:first_start] = replacement

    return "\n".join(lines).rstrip() + "\n", True


def append_to_new_files_section(content: str, additions: list[str]) -> str:
    match = re.search(r"(?ms)^## New Files\s*\n(.*?)(?=^##\s|\Z)", content)
    if not match:
        return content.rstrip() + "\n\n## New Files\n\n" + "\n".join(additions) + "\n"

    existing_lines = [line.rstrip() for line in match.group(1).splitlines() if line.strip()]
    seen = set(existing_lines)
    merged_lines = existing_lines[:]
    for addition in additions:
        if addition not in seen:
            seen.add(addition)
            merged_lines.append(addition)

    replacement = "## New Files\n\n" + "\n".join(merged_lines).rstrip() + "\n"
    return content[: match.start()] + replacement + content[match.end() :]


def smart_update_index(folder: Path, all_targets: set[str], report: AuditReport, dry_run: bool) -> bool:
    index_path = folder / "_index.md"
    subdirs = sorted(
        [
            d
            for d in folder.iterdir()
            if d.is_dir() and not d.name.startswith(".") and not should_skip_index_maintenance(d)
        ],
        key=lambda item: item.name.lower(),
    )
    files = sorted(
        [
            f
            for f in folder.glob("*.md")
            if f.name != "_index.md" and not should_skip_index_maintenance(f)
        ],
        key=lambda item: item.name.lower(),
    )
    visible_files = [f for f in files if not should_skip_auto_index_file(folder, f)]

    stamp = today()
    if not index_path.exists():
        if not subdirs and not visible_files:
            return False
        content = build_new_index(folder, subdirs, visible_files, stamp)
        write_text(index_path, content, dry_run)
        report.indexes_created += 1
        return True

    original = read_text(index_path)
    content = original
    changed = False

    content, rooted_fixed = normalize_rooted_links(content)
    if rooted_fixed:
        report.brittle_index_links += rooted_fixed
        changed = True

    content, fm_changed = ensure_frontmatter(content, index_path, stamp)
    changed = changed or fm_changed

    content, merged_new_files = merge_new_files_sections(content)
    changed = changed or merged_new_files

    existing_links = set(extract_wikilinks(content))
    cleaned_lines: list[str] = []
    removed_dead_lines = False
    traversal_count = 0

    for line in content.splitlines():
        traversal_count += line.count("[[../")
        line_links = extract_wikilinks(line)
        if line_links:
            dead = [link for link in line_links if not link_resolves(link, all_targets)]
            if dead and len(dead) == len(line_links):
                removed_dead_lines = True
                continue
        cleaned_lines.append(line)

    if traversal_count:
        report.brittle_index_links += traversal_count

    if removed_dead_lines:
        content = "\n".join(cleaned_lines).rstrip() + "\n"
        changed = True

    additions: list[str] = []

    for subdir in subdirs:
        if not any(link_points_to_folder(link, subdir) for link in existing_links):
            additions.append(f"- [[{subdir.name}/_index|{subdir.name}/]] - {default_description(subdir)}")

    for file_path in visible_files:
        if not any(link_points_to_file(link, file_path) for link in existing_links):
            desc = extract_file_description(file_path)
            additions.append(f"- [[{file_path.stem}]] - {desc}" if desc else f"- [[{file_path.stem}]]")

    if additions:
        changed = True
        content = append_to_new_files_section(content, additions)

    if len(content.splitlines()) > MAX_INDEX_LINES:
        content, archived_count = archive_old_sessions(content, folder, dry_run)
        if archived_count == 0 and index_path in TOP_HUBS:
            report.oversize_indexes += 1
        elif len(content.splitlines()) > MAX_INDEX_LINES:
            report.oversize_indexes += 1

    if not changed:
        return False

    content = bump_last_updated(content, stamp)
    write_text(index_path, content, dry_run)
    report.indexes_updated += 1
    return True


def update_all_indexes(report: AuditReport, dry_run: bool) -> None:
    all_targets = build_vault_targets()
    for base_dir in ACTIVE_INDEX_DIRS:
        if not base_dir.exists():
            continue
        folders = [base_dir] + sorted(
            [
                folder
                for folder in base_dir.rglob("*")
                if folder.is_dir() and not should_skip_index_maintenance(folder)
            ],
            key=lambda item: str(item).lower(),
        )
        for folder in folders:
            smart_update_index(folder, all_targets, report, dry_run)


def audit_root_guidance(report: AuditReport, dry_run: bool) -> None:
    for root_file in ROOT_GUIDANCE_FILES:
        if not root_file.exists() or not read_text(root_file).strip():
            report.root_warnings += 1
            continue
        content = read_text(root_file)
        normalized, count = normalize_rooted_links(content)
        if count:
            report.brittle_index_links += count
            write_text(root_file, normalized, dry_run)

    for hub in TOP_HUBS:
        if not hub.exists() or not read_text(hub).strip():
            report.root_warnings += 1
            continue
        if len(read_text(hub).splitlines()) > MAX_INDEX_LINES:
            report.oversize_indexes += 1


def validate_memory(report: AuditReport) -> None:
    report.memory_exists = MEMORY_INDEX.exists()
    if report.memory_exists:
        report.memory_lines = len(read_text(MEMORY_INDEX).splitlines())


def find_empty_active_folders(report: AuditReport) -> list[str]:
    empty: list[str] = []
    for base_dir in ACTIVE_INDEX_DIRS:
        if not base_dir.exists():
            continue
        for folder in sorted(
            [
                d
                for d in base_dir.rglob("*")
                if d.is_dir() and not should_skip_index_maintenance(d)
            ],
            key=lambda item: str(item).lower(),
        ):
            items = [child for child in folder.iterdir() if not child.name.startswith(".")]
            if not items:
                empty.append(rel(folder))
    report.empty_folders = len(empty)
    return empty


def iter_active_scan_files() -> list[Path]:
    files: list[Path] = []

    for root_file in ROOT_GUIDANCE_FILES:
        if root_file.exists():
            files.append(root_file)

    for root_file in VAULT_ROOT.glob("*.md"):
        if root_file.name in IGNORED_ROOT_FILES:
            continue
        if root_file in ROOT_GUIDANCE_FILES or root_file == BROKEN_LINKS_LOG:
            continue
        files.append(root_file)

    for base_dir in ACTIVE_LINK_SCAN_DIRS:
        if not base_dir.exists():
            continue
        files.extend(base_dir.rglob("*.md"))

    unique: list[Path] = []
    seen: set[Path] = set()
    for path in files:
        if should_ignore_source_file(path):
            continue
        if path not in seen:
            unique.append(path)
            seen.add(path)
    return unique


def build_broken_link_log(
    broken_by_file: dict[str, list[str]],
    style_warnings: dict[str, list[str]],
    empty_folders: list[str],
    report: AuditReport,
    dry_run: bool,
) -> None:
    total_broken = sum(len(links) for links in broken_by_file.values())
    report.broken_links = total_broken
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Vault Link and Navigation Audit",
        f"Generated: {stamp}",
        f"Broken links: {report.broken_links}",
        f"Brittle index links: {report.brittle_index_links}",
        f"Root warnings: {report.root_warnings}",
        f"Oversize indexes: {report.oversize_indexes}",
        "",
        "_Dead link-only lines may be removed from `_index.md` files automatically. Content-note links are logged for manual review._",
        "",
    ]

    if broken_by_file:
        lines.append("## Broken Wikilinks")
        lines.append("")
        for source, links in sorted(broken_by_file.items()):
            lines.append(f"### {source}")
            for link in links:
                lines.append(f"- `[[{link}]]`")
            lines.append("")

    if style_warnings:
        lines.append("## Brittle Link Styles")
        lines.append("")
        for source, warnings in sorted(style_warnings.items()):
            lines.append(f"### {source}")
            for warning in warnings:
                lines.append(f"- {warning}")
            lines.append("")

    if empty_folders:
        lines.append("## Empty Active Folders")
        lines.append("")
        for folder in empty_folders:
            lines.append(f"- `{folder}`")
        lines.append("")

    if report.root_warnings or report.oversize_indexes:
        lines.append("## Root Guidance Warnings")
        lines.append("")
        if report.root_warnings:
            lines.append(f"- {report.root_warnings} root guidance file(s) or top hubs are missing or empty")
        if report.oversize_indexes:
            lines.append(f"- {report.oversize_indexes} index file(s) exceed the preferred line budget")
        lines.append("")

    write_text(BROKEN_LINKS_LOG, "\n".join(lines).rstrip() + "\n", dry_run)


def find_and_log_broken_links(report: AuditReport, dry_run: bool) -> None:
    all_targets = build_vault_targets()
    broken_by_file: dict[str, list[str]] = {}
    style_warnings: dict[str, list[str]] = {}

    for md_file in iter_active_scan_files():
        if md_file == BROKEN_LINKS_LOG:
            continue
        content = read_text(md_file)
        links = extract_wikilinks(sanitize_markdown_for_link_scan(content))
        dead = [link for link in links if not link_resolves(link, all_targets)]
        if dead:
            broken_by_file[rel(md_file)] = dead

        if md_file.name == "_index.md" or md_file in ROOT_GUIDANCE_FILES:
            warnings: list[str] = []
            if "[[../" in content:
                warnings.append("contains relative traversal links like `[[../...]]`")
            if "[[/" in content:
                warnings.append("contains rooted links like `[[/...]]`")
            if warnings:
                style_warnings[rel(md_file)] = warnings

    empty_folders = find_empty_active_folders(report)
    build_broken_link_log(broken_by_file, style_warnings, empty_folders, report, dry_run)


def scan_surface_in_root_projects() -> list[str]:
    surfaced: list[str] = []
    for index_path in sorted(ANALYST_DIR.rglob("_index.md"), key=lambda item: str(item).lower()):
        if should_ignore_navigation_path(index_path) or index_path == ANALYST_DIR / "_index.md":
            continue
        fields = parse_frontmatter_fields(read_text(index_path))
        if fields.get("agent_context", "").lower() != "true":
            continue
        if fields.get("surface_in_root", "").lower() != "true":
            continue
        if fields.get("status", "").lower() not in {"active", "current"}:
            continue

        folder_rel = rel(index_path.parent)
        if folder_rel.startswith("02_Analyst/"):
            folder_rel = folder_rel[len("02_Analyst/") :]
        surfaced.append(folder_rel)
    return surfaced


def extract_dated_filename_sort_key(path: Path) -> tuple[str, str]:
    match = re.search(r"(\d{4}-\d{2}-\d{2})", path.name)
    return (match.group(1) if match else "0000-00-00", path.name.lower())


def scan_latest_audit_notes() -> list[str]:
    latest: list[str] = []
    for pattern in AUDIT_FILE_PATTERNS.values():
        matches = sorted(
            [path for path in VAULT_ROOT.glob(pattern) if path.is_file()],
            key=extract_dated_filename_sort_key,
        )
        if matches:
            latest.append(rel(matches[-1]).removesuffix(".md"))
    return latest


def sync_analyst_root_metadata(dry_run: bool) -> None:
    root_index = ANALYST_DIR / "_index.md"
    if not root_index.exists():
        return

    content = read_text(root_index)
    order, data, body = parse_frontmatter_data(content)
    if not data:
        return

    open_entries = [
        entry
        for entry in scan_conflict_entries()
        if str(entry["status"]) in {"awaiting_review", "pending_validation"}
    ]
    stale_cutoff = datetime.now() - timedelta(days=STALE_CONFLICT_DAYS)
    stale_entries = [
        entry
        for entry in open_entries
        if isinstance(entry["timestamp"], datetime) and entry["timestamp"] <= stale_cutoff
    ]

    data["active_projects"] = scan_surface_in_root_projects()
    data["open_conflicts"] = [format_conflict_ref(entry) for entry in open_entries]
    data["unreviewed_conflicts"] = [format_conflict_ref(entry) for entry in stale_entries]
    data["open_conflict_count"] = str(len(open_entries))
    data["pending_validation_count"] = str(
        len([entry for entry in open_entries if str(entry["status"]) == "pending_validation"])
    )
    data["latest_audit_notes"] = scan_latest_audit_notes()

    rebuilt = render_frontmatter_data(order, data, body)
    rebuilt = bump_last_updated(rebuilt, today())
    write_text(root_index, rebuilt, dry_run)


def do_git_commit(topic: str | None, commit: bool) -> None:
    print("\nGit Commit Phase:")
    if not commit:
        print("  INFO Commit skipped (use --commit only when explicitly requested)")
        return

    ok, output = run_command(["git", "add", "-A"])
    if not ok:
        print(f"  ERROR git add failed: {output[:200]}")
        return

    ok, status = run_command(["git", "status", "--short"])
    if not ok or not status.strip():
        print("  INFO No changes to commit")
        return

    message = (
        f"vault save-audit: {topic} maintenance"
        if topic
        else "vault save-audit: audit and index maintenance"
    )
    ok, output = run_command(["git", "commit", "-m", message])
    if not ok:
        print(f"  ERROR Commit failed: {output[:200]}")
        return

    ok, commit_hash = run_command(["git", "rev-parse", "--short", "HEAD"])
    if ok:
        print(f"  OK Committed: {commit_hash.strip()} - {message}")
    else:
        print(f"  OK Committed: {message}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Vault-aware audit backend for save-audit")
    parser.add_argument("topic", nargs="?", help="Optional topic label for the save phase")
    parser.add_argument("--topic", dest="topic_flag", help="Optional topic label")
    parser.add_argument("--commit", action="store_true", help="Create a git commit after audit")
    parser.add_argument("--dry-run", action="store_true", help="Report actions without writing files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    topic = args.topic_flag or args.topic
    dry_run = args.dry_run
    report = AuditReport()

    print("=" * 60)
    print("VAULT OPTIMIZATION: /save-audit")
    print("=" * 60)

    if topic:
        print(f"\nSave Context: {topic}")
        print("  INFO Topic mode assumes the agent already updated the durable note(s) for this work")

    if dry_run:
        print("\nDry Run Mode: no files will be written and no commit will be created")

    print("\nAudit Phase:")
    audit_root_guidance(report, dry_run)
    update_all_indexes(report, dry_run)
    validate_memory(report)
    find_and_log_broken_links(report, dry_run)
    run_contradiction_audit(report, dry_run)
    sync_analyst_root_metadata(dry_run)

    print(f"  OK Indexes created: {report.indexes_created}")
    print(f"  OK Indexes updated: {report.indexes_updated}")
    if report.broken_links:
        print(f"  WARN Broken wikilinks logged: {report.broken_links}")
    else:
        print("  OK No broken wikilinks detected")
    if report.brittle_index_links:
        print(f"  WARN Brittle index-link warnings: {report.brittle_index_links}")
    if report.root_warnings:
        print(f"  WARN Root guidance warnings: {report.root_warnings}")
    if report.oversize_indexes:
        print(f"  WARN Oversize index warnings: {report.oversize_indexes}")
    if report.empty_folders:
        print(f"  WARN Empty active folders surfaced: {report.empty_folders}")

    print("\nContradiction Audit:")
    print(f"  OK Open conflict queue items: {report.open_conflicts}")
    if report.pending_validation_conflicts:
        print(f"  WARN Pending validation items: {report.pending_validation_conflicts}")
    else:
        print("  OK No pending-validation items detected")
    if report.truth_collisions:
        print(f"  WARN Potential current-truth collisions: {report.truth_collisions}")
    else:
        print("  OK No competing current-truth clusters detected")
    if report.alias_collisions:
        print(f"  WARN Sibling alias-folder collisions: {report.alias_collisions}")
    if report.duplicate_note_stems:
        print(f"  WARN Duplicate note stems requiring review: {report.duplicate_note_stems}")
    else:
        print("  OK No duplicate note stems requiring review")
    if report.intentional_duplicate_stems:
        print(f"  OK Intentional duplicate stems recognized: {report.intentional_duplicate_stems}")
    if report.scoped_duplicate_stems:
        print(f"  OK Scoped duplicate stems recognized: {report.scoped_duplicate_stems}")
    if report.duplicate_index_headings:
        print(f"  WARN Duplicate index-section headings: {report.duplicate_index_headings}")
    if report.task_context_indexes_needing_review:
        print(f"  WARN Agent-context indexes needing task review: {report.task_context_indexes_needing_review}")
    else:
        print("  OK All agent-context indexes have required task frontmatter")
    if report.task_context_indexes:
        print(f"  OK Agent-context indexes covered: {report.task_context_indexes}")
    if report.task_context_drifted_indexes:
        print(f"  WARN Agent-context indexes with prompt drift: {report.task_context_drifted_indexes}")

    print("\nMemory Health:")
    if report.memory_exists:
        print(f"  OK MEMORY.md present ({report.memory_lines} lines)")
    else:
        print("  WARN MEMORY.md not found")

    do_git_commit(topic, args.commit and not dry_run)

    print("\n" + "=" * 60)
    print("VAULT OPTIMIZATION COMPLETE")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
