---
name: save-audit
description: Vault-aware save and audit workflow for context management and stronger non-development agent output. Agent-led synthesis first; script-backed index and link maintenance second.
user-invocable: true
---

# save-audit

Vault-aware save and audit workflow for this Obsidian system.

This skill is for preserving durable reasoning, writing, research, outreach, planning, and decision-support work without letting the vault drift into index bloat or broken navigation.

## What This Skill Really Does

`save-audit` has two parts:

1. Agent-led save work
   - Read the relevant topic context
   - Update the canonical Analyst, References, or Outputs note
   - Update the nearest project `_index.md` frontmatter when it carries agent task context
   - Add task cards or run logs when the work is substantial
   - Update the nearest useful `_index.md`

2. Script-backed audit work
   - Refresh active `_index.md` files in `02_Analyst`, `03_References`, and `05_Outputs`
   - Derive root Analyst metadata that should not drift by hand
   - Seed missing frontmatter on active index files
   - Update `last_updated` on changed index files
   - Remove dead index-only link lines
   - Log broken links and brittle index-link styles
   - Surface contradiction clusters such as competing `current` notes, alias folders, duplicate note stems, and duplicate index headings
   - Check root guidance and memory-index health

## Important Boundary

The bundled script does **not** autonomously synthesize raw Source into Analyst-quality notes.

If a topic is provided, the agent should perform the reasoning and note updates first, then run the audit backend.

## When to Use This Skill

Invoke this skill when:
- a meaningful work block changed project knowledge
- a topic area needs a durable save pass plus cleanup
- active `_index.md` files may be stale
- you want the vault checked without manually scanning folders

## Invocation Patterns

Skill-level use:
- `save-audit` - run the audit backend and refresh active navigation
- `save-audit internships` - do a vault-aware save for internships, then audit

Backend script:

```bash
python scripts/save_audit.py --dry-run
python scripts/save_audit.py --topic internships --dry-run
python scripts/save_audit.py --topic clinicalhours
python scripts/save_audit.py --topic clinicalhours --commit
```

## Default Workflow

### 1. Agent-Led Save Phase

When a topic is specified:

1. Load the smallest sufficient context first
2. Update the canonical durable note instead of creating duplicates
3. If an older note is being replaced, downgrade it to `snapshot`, `historical`, or `superseded` instead of leaving two notes looking current
4. If the nearest relevant `_index.md` has `agent_context: true`, update its prompt-critical frontmatter first:
   - `current_focus`
   - `active_tasks`
   - `prompt_context`
   - `definition_of_done`
   - `blocked_by` when useful
   - `surface_in_root: true` only for primary hubs that should appear on the root Analyst index
5. Add a standalone task card only when the work is high-stakes, cross-project, reusable, or likely to need resumption
6. Update the nearest project or domain `_index.md`

### 2. Script-Backed Audit Phase

Run `scripts/save_audit.py` to:

1. Refresh active `_index.md` files in:
   - `02_Analyst`
   - `03_References`
   - `05_Outputs`
2. Ensure active indexes have frontmatter and `last_updated`
3. Normalize rooted wiki links like `[[/02_Analyst/...]]`
4. Remove dead link lines from indexes only
5. Log unresolved broken links and brittle link styles to `.vault-broken-links.md`
6. Check whether `INDEX.md`, `CLAUDE.md`, and top hubs are present and non-empty
7. Validate `MEMORY.md` health without pretending to rewrite memory automatically
8. Write `.vault-contradictions.md` with:
   - open vs closed `.vault-conflicts` queue counts
   - competing `current`/truth-claim note clusters
   - sibling alias-folder collisions
   - duplicate note stems classified through `references/DUPLICATE-STEM-POLICY.json`
   - duplicate `## New Files` headings in indexes
   - missing task-context fields on any `_index.md` that declares `agent_context: true`
   - prompt-context drift when an `agent_context` index points to missing or historical notes
9. Derive root Analyst metadata from explicit signals:
   - `active_projects` from `surface_in_root: true` indexes
   - `open_conflicts` and `unreviewed_conflicts` from `.vault-conflicts`
   - `latest_audit_notes` from the audit families

### 3. Optional Commit Phase

Commits are **off by default**.

Use `--commit` only when the user explicitly wants a git commit.

## Non-Goals

This skill should not:
- auto-commit by default
- invent Analyst synthesis from raw Source without agent reasoning
- silently delete user content
- rewrite rich custom project notes just to satisfy a rigid template

## Success Criteria

After a good `save-audit` run:
- the durable note is updated
- the nearest useful indexes are current
- active indexes have frontmatter
- root guidance is still readable
- broken links are surfaced, not buried
- contradiction clusters are surfaced and routed instead of being left implicit
- agent-context indexes carry a usable prompt brief instead of forcing agents to infer task state from scattered prose
- root-derived metadata reflects the real queue and root-visible hubs
- a future agent can resume with less context hunting

## Files Included

- `scripts/save_audit.py` - audit backend for indexes, frontmatter, root checks, link logging, and contradiction surfacing
- `references/OPTIMIZATION-RULES.md` - vault-specific save-audit contract summary
- `references/PROJECT-INDEX-TASK-PROTOCOL.md` - required frontmatter contract for project-local prompt context
- `references/DUPLICATE-STEM-POLICY.json` - machine-readable allowlist and classification rules for duplicate stems
- `references/DUPLICATE-STEM-POLICY.md` - human guide for extending the duplicate-stem policy
