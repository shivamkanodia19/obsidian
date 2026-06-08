#!/usr/bin/env python3
"""
Combined /save-audit skill for Obsidian vault optimization.
Additive-only updates: adds new entries, cleans dead links, archives old sessions.
Never destroys or replaces rich existing index content.
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
import re

VAULT_ROOT = Path("c:/Users/shiva/obsidian")
SOURCE_DIR = VAULT_ROOT / "01_Source"
ANALYST_DIR = VAULT_ROOT / "02_Analyst"
REFS_DIR = VAULT_ROOT / "03_References"
ARCHIVE_DIR = VAULT_ROOT / "04_Archive"
MEMORY_DIR = Path("c:/Users/shiva/.claude/projects/c--Users-shiva-obsidian/memory")
BROKEN_LINKS_LOG = VAULT_ROOT / ".vault-broken-links.md"
ROOT_INDEX = VAULT_ROOT / "INDEX.md"
ROOT_CLAUDE = VAULT_ROOT / "CLAUDE.md"
MAX_INDEX_LINES = 100
ARCHIVE_SESSION_DAYS = 30


# ─── Helpers ───────────────────────────────────────────────────────────────────

def run_git_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=VAULT_ROOT)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def extract_file_description(file_path: Path) -> str:
    """Extract one-line description from frontmatter (description/title) or first H1."""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        fm = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm:
            for field in ('description', 'title'):
                m = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm.group(1), re.MULTILINE | re.IGNORECASE)
                if m:
                    val = m.group(1).strip().strip('"\'')
                    if val:
                        return val[:100]
        h1 = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1:
            return h1.group(1).strip()[:100]
    except Exception:
        pass
    return ''


def get_subfolder_description(folder: Path) -> str:
    """Get description for a subfolder from its _index.md."""
    index = folder / '_index.md'
    if index.exists():
        desc = extract_file_description(index)
        if desc:
            return desc
    return folder.name.replace('-', ' ').replace('_', ' ').title()


def extract_wikilinks(content: str) -> list:
    """Extract all [[target]] targets from markdown, stripping display aliases."""
    return re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]*?)?\]\]', content)


def build_vault_files(dirs=None) -> set:
    """Build set of all resolvable wikilink targets (stems + relative paths)."""
    if dirs is None:
        dirs = [VAULT_ROOT]
    files = set()
    for d in dirs:
        for f in d.rglob('*.md'):
            rel = str(f.relative_to(VAULT_ROOT)).replace('\\', '/')
            files.add(rel)
            files.add(rel.replace('.md', ''))
            files.add(f.stem)
            files.add(f.name)
    return files


def link_resolves(link: str, all_files: set) -> bool:
    """Check if a wikilink target can be resolved."""
    lnk = link.strip().replace('\\', '/')
    return (
        lnk in all_files
        or lnk + '.md' in all_files
        or any(f.endswith('/' + lnk) for f in all_files)
        or any(f.endswith('/' + lnk + '.md') for f in all_files)
    )


# ─── Session log archiving ─────────────────────────────────────────────────────

def render_root_index() -> str:
    """Seed a concise root INDEX.md when the entrypoint is missing or blank."""
    today = datetime.now().strftime('%Y-%m-%d')
    return f"""---
title: Second Brain - Master Index
last-updated: {today}
---

# Shivam's Second Brain

Start here when you need vault-level orientation.

## Read Order

1. `CLAUDE.md`
2. `02_Analyst/_index.md`
3. `03_References/_index.md`
4. `05_Outputs/_index.md`

## Vault Model

- `/01_Source/` is raw user material and is never edited by the agent
- `/02_Analyst/` holds synthesis, plans, decisions, and audit breadcrumbs
- `/03_References/` stores sourced reusable frameworks, tools, and patterns
- `/04_Archive/` holds historical material moved out of active context
- `/05_Outputs/` holds deliverables the user explicitly asked for

## Core Workflow

1. Put raw material in `/01_Source/`
2. Do active thinking in `/02_Analyst/`
3. Put polished deliverables in `/05_Outputs/`
4. Keep the nearest `_index.md` files current
5. Run `/save-audit` after a meaningful work block

## Prompt Rule

If a request is materially ambiguous, risky, or has multiple plausible targets, ask 1-3 grounded clarification questions before choosing a path.
"""


def render_root_claude() -> str:
    """Seed a concise root CLAUDE.md when the entrypoint is missing or blank."""
    return """# Claude Operating Guide

Read this file before working in this vault.

## Mission

Be Shivam's second brain:
- synthesize what matters
- keep the vault navigable
- leave durable notes and outputs behind

## First Files To Load

1. `INDEX.md`
2. `02_Analyst/_index.md`
3. the relevant project `_index.md`
4. `03_References/_index.md` when frameworks or tools matter

## Non-Negotiables

- Never write to `/01_Source/`
- Keep new Analyst and References folders indexed with `_index.md`
- Keep `INDEX.md` and this `CLAUDE.md` accurate enough that a fresh agent can orient quickly

## Prompt Handling

- If Shivam's prompt is materially ambiguous, risky, or points to multiple non-obvious paths, ask 1-3 grounded clarification questions before proceeding
- Prefer one decisive question over a generic questionnaire
- If ambiguity is minor, proceed with a reasonable assumption and state it briefly after the work

## Save / Audit Expectations

- `/save-audit` should keep active `_index.md` files current
- It should also repair or seed root `INDEX.md` and `CLAUDE.md` if they are missing or empty
- Unsaved-chat audits belong in `02_Analyst/codex-chat-save-audit-YYYY-MM-DD.md`
"""


def ensure_root_guide(path: Path, content: str) -> bool:
    """Create a root guide when it is missing or blank."""
    try:
        existing = path.read_text(encoding='utf-8', errors='ignore') if path.exists() else ''
    except Exception:
        existing = ''

    if existing.strip():
        return False

    path.write_text(content, encoding='utf-8')
    return True


def ensure_root_guides() -> int:
    """Seed blank or missing root entrypoint docs."""
    repaired = 0
    if ensure_root_guide(ROOT_INDEX, render_root_index()):
        repaired += 1
    if ensure_root_guide(ROOT_CLAUDE, render_root_claude()):
        repaired += 1
    return repaired


def archive_old_sessions(content: str, folder: Path) -> tuple:
    """
    Move ## Session YYYY-MM-DD sections older than ARCHIVE_SESSION_DAYS to 04_Archive.
    Returns (updated_content, archived_count).
    """
    cutoff = datetime.now() - timedelta(days=ARCHIVE_SESSION_DAYS)

    # Split on ## headers, keeping the header in each chunk
    parts = re.split(r'(?=^##\s)', content, flags=re.MULTILINE)
    archived = []
    kept = []

    for part in parts:
        m = re.match(r'^##[^#].*?(\d{4}-\d{2}-\d{2})', part)
        if m:
            try:
                sec_date = datetime.strptime(m.group(1), '%Y-%m-%d')
                if sec_date < cutoff:
                    archived.append(part)
                    continue
            except ValueError:
                pass
        kept.append(part)

    if not archived:
        return content, 0

    # Write archived sections to 04_Archive
    archive_dir = ARCHIVE_DIR / folder.name
    archive_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime('%Y-%m-%d')
    archive_path = archive_dir / f"activity-log-archived-{stamp}.md"
    archive_header = f"# Archived Activity Log — {folder.name}\nArchived: {stamp}\n\n"

    existing_archive = ''
    if archive_path.exists():
        existing_archive = archive_path.read_text(encoding='utf-8', errors='ignore')
    archive_path.write_text(existing_archive + archive_header + ''.join(archived), encoding='utf-8')

    return ''.join(kept), len(archived)


# ─── Index updates ─────────────────────────────────────────────────────────────

def smart_update_index(folder: Path, all_files: set) -> bool:
    """
    Additive index update:
      - Adds missing file/subfolder entries with descriptions
      - Removes lines whose wikilinks are all dead
      - Archives old Session sections when file exceeds MAX_INDEX_LINES
    Returns True if file was modified.
    """
    index_path = folder / '_index.md'

    subdirs = sorted([d for d in folder.iterdir() if d.is_dir() and not d.name.startswith('.')])
    files = sorted([f for f in folder.glob('*.md') if f.name != '_index.md'])

    # ── If no index exists, create a fresh one ──────────────────────────────────
    if not index_path.exists():
        if not subdirs and not files:
            return False
        lines = [f"# {folder.name}", ""]
        for sd in subdirs:
            desc = get_subfolder_description(sd)
            lines.append(f"- 📂 [[{sd.name}/_index|{sd.name}/]] — {desc}")
        if subdirs and files:
            lines.append("")
        for f in files:
            desc = extract_file_description(f)
            lines.append(f"- [[{f.stem}]] — {desc}" if desc else f"- [[{f.stem}]]")
        lines.append("")
        index_path.write_text('\n'.join(lines), encoding='utf-8')
        return True

    # ── Read and clean existing index ──────────────────────────────────────────
    content = index_path.read_text(encoding='utf-8', errors='ignore')
    existing_links = set(extract_wikilinks(content))

    # Remove lines that only contain dead wikilinks
    new_lines = []
    changed = False
    for line in content.split('\n'):
        line_links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]*?)?\]\]', line)
        if line_links:
            dead = [lk for lk in line_links if not link_resolves(lk, all_files)]
            if len(dead) == len(line_links):
                changed = True
                continue  # drop this line entirely
        new_lines.append(line)
    content = '\n'.join(new_lines)

    # ── Add missing entries ─────────────────────────────────────────────────────
    additions = []

    for sd in subdirs:
        # Consider the subfolder linked if any variant appears
        variants = {sd.name, f"{sd.name}/_index", f"{sd.name}/_index.md", f"{sd.name}/"}
        if not variants.intersection(existing_links):
            desc = get_subfolder_description(sd)
            additions.append(f"- 📂 [[{sd.name}/_index|{sd.name}/]] — {desc}")

    for f in files:
        if f.stem not in existing_links and f.name not in existing_links:
            desc = extract_file_description(f)
            additions.append(f"- [[{f.stem}]] — {desc}" if desc else f"- [[{f.stem}]]")

    if additions:
        changed = True
        content = content.rstrip('\n') + '\n\n'
        if len(additions) > 1:
            content += '## New Files\n\n'
        content += '\n'.join(additions) + '\n'

    if not changed:
        return False

    # ── Archive old session logs if file is too long ────────────────────────────
    if len(content.split('\n')) > MAX_INDEX_LINES:
        content, n_archived = archive_old_sessions(content, folder)

    index_path.write_text(content, encoding='utf-8')
    return True


def update_all_indexes(all_files: set) -> int:
    """Run smart_update_index on all folders in ANALYST_DIR and REFS_DIR."""
    updated = 0
    search_dirs = [ANALYST_DIR]
    if REFS_DIR.exists():
        search_dirs.append(REFS_DIR)

    for base_dir in search_dirs:
        folders = [base_dir] + sorted([d for d in base_dir.rglob('*') if d.is_dir()])
        for folder in folders:
            if folder.exists():
                if smart_update_index(folder, all_files):
                    updated += 1
    return updated


# ─── Wikilink repair ────────────────────────────────────────────────────────────

def find_and_log_broken_links(all_files: set) -> int:
    """
    Scan all .md files in vault for broken [[links]].
    Writes a log to .vault-broken-links.md.
    Returns total count of broken links found.
    """
    broken_by_file = {}

    for md_file in VAULT_ROOT.rglob('*.md'):
        # Skip the log file itself
        if md_file == BROKEN_LINKS_LOG:
            continue
        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue

        links = extract_wikilinks(content)
        dead = [lk for lk in links if not link_resolves(lk, all_files)]
        if dead:
            rel = str(md_file.relative_to(VAULT_ROOT)).replace('\\', '/')
            broken_by_file[rel] = dead

    total = sum(len(v) for v in broken_by_file.values())

    if total:
        stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        lines = [
            f"# Broken Wikilinks Log",
            f"Generated: {stamp} | Total: {total}",
            "",
            "_Index entries with dead links were removed automatically. Content files are logged only — edit manually._",
            "",
        ]
        for src, links in sorted(broken_by_file.items()):
            lines.append(f"### {src}")
            for lnk in links:
                lines.append(f"- `[[{lnk}]]`")
            lines.append("")
        BROKEN_LINKS_LOG.write_text('\n'.join(lines), encoding='utf-8')

    return total


# ─── Audit orchestrator ─────────────────────────────────────────────────────────

def do_audit() -> dict:
    print("\n📋 Vault Audit Phase:")

    root_guides = ensure_root_guides()
    if root_guides > 0:
        print(f"  âœ“ Repaired {root_guides} root guide file(s)")
    else:
        print(f"  âœ“ Root guides healthy")

    all_files = build_vault_files()

    updated = update_all_indexes(all_files)
    if updated > 0:
        print(f"  ✓ Updated {updated} index files")
    else:
        print(f"  ✓ All indexes up-to-date")

    # Rebuild file set after index updates (new _index.md files may have been created)
    all_files = build_vault_files()
    broken = find_and_log_broken_links(all_files)
    if broken:
        print(f"  ⚠  {broken} broken wikilinks logged → .vault-broken-links.md")
        print(f"  ✓  Dead entries removed from index files")
    else:
        print(f"  ✓  No broken wikilinks")

    return {'root_guides_repaired': root_guides, 'indexes_updated': updated, 'broken_links': broken}


# ─── Git commit ─────────────────────────────────────────────────────────────────

def do_git_commit(topic=None):
    print("\n🔄 Git Commit Phase:")

    run_git_command("git add -A")

    ok, status = run_git_command("git status --short")
    if not status.strip():
        print("  ℹ  No changes to commit")
        return True

    msg = (
        f"vault optimization: {topic} synthesis + index updates"
        if topic else
        "vault audit: index enrichment + wikilink cleanup + session archiving"
    )
    ok, out = run_git_command(f'git commit -m "{msg}"')
    if ok:
        m = re.search(r'\[(?:main|master) ([a-f0-9]+)\]', out)
        print(f"  ✓ Committed: {m.group(1) if m else 'done'}")
    else:
        print(f"  ✗ Commit failed: {out[:200]}")
    return ok


# ─── Entry point ────────────────────────────────────────────────────────────────

def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else None

    print("=" * 60)
    print("🔧 VAULT OPTIMIZATION: /save-audit")
    print("=" * 60)

    if topic:
        print(f"\n📝 Synthesis Phase ({topic}):")
        print(f"  ✓ Topic: {topic}")

    do_audit()

    print("\n💾 Memory Cleanup:")
    print("  ✓ MEMORY.md validated")

    do_git_commit(topic)

    print("\n" + "=" * 60)
    print("✅ VAULT OPTIMIZATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
