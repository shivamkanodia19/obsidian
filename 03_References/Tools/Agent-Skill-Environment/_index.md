---
description: "Portable export of local agent skills and related runtime caches for Mac setup"
title: Agent Skill Environment
project: references
strategic: false
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-06-08
tags: [references, tools, codex, claude, migration]
---

# Agent Skill Environment

This folder is a non-sensitive export of the local skill environment from this Windows machine so the MacBook can pick up the same agent-facing tooling faster.

## Included

- `roots/home-claude-skills`
- `roots/home-codex-skills`
- `roots/home-agents-skills`
- `roots/codex-plugin-cache/openai-bundled`
- `roots/codex-plugin-cache/openai-curated`
- `roots/codex-plugin-cache/openai-curated-remote`
- `roots/codex-plugin-cache/openai-primary-runtime`
- `extras/project-save-audit`
- `extras/windows-claude-settings`
- `inventory.json`
- `restore_to_mac.sh`

## Intentionally Excluded

- Claude project memory/session logs
- obvious secret material
- Python cache files such as `__pycache__`, `*.pyc`, and `*.pyo`

## Mac Restore

1. Clone this repo onto the Mac.
2. From the repo root, run:

```bash
bash 03_References/Tools/Agent-Skill-Environment/restore_to_mac.sh
```

3. Review `extras/windows-claude-settings/` manually before reusing any settings, because the paths are Windows-specific.
4. Treat `roots/codex-plugin-cache/` as reference material first. Some bundled plugin cache contents are platform-specific, so they should not be blindly copied into a live macOS cache.

## Notes

- The restore script backs up any existing target directories before replacing them.
- The restore script only installs the portable user skill roots automatically.
- Plugin/app login state does not travel with this export; expect to sign in again on the Mac.
- `extras/project-save-audit` is included as reference material, not auto-installed, because the Claude project slug will differ on macOS.
