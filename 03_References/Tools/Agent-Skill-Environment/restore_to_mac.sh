#!/usr/bin/env bash

set -euo pipefail

bundle_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
timestamp="$(date +%Y%m%d-%H%M%S)"

backup_path() {
  local target="$1"
  if [ -e "$target" ]; then
    local backup="${target}.backup.${timestamp}"
    mv "$target" "$backup"
    echo "Backed up $target -> $backup"
  fi
}

restore_dir() {
  local source_rel="$1"
  local target_rel="$2"
  local source_dir="$bundle_dir/$source_rel"
  local target_dir="$HOME/$target_rel"

  if [ ! -d "$source_dir" ]; then
    echo "Skipping missing source: $source_rel"
    return
  fi

  mkdir -p "$(dirname "$target_dir")"
  backup_path "$target_dir"
  mkdir -p "$target_dir"
  ditto "$source_dir" "$target_dir"
  echo "Restored $target_rel"
}

restore_dir "roots/home-claude-skills" ".claude/skills"
restore_dir "roots/home-codex-skills" ".codex/skills"
restore_dir "roots/home-agents-skills" ".agents/skills"

cat <<EOF

Restore complete.

Manual follow-up:
- Review $bundle_dir/roots/codex-plugin-cache before copying any plugin cache content into macOS. Some cached plugin assets are platform-specific.
- Review $bundle_dir/extras/windows-claude-settings before reusing Claude settings on macOS.
- Re-auth any apps/plugins that depend on local login state.
- Inspect $bundle_dir/extras/project-save-audit if you want to recreate that helper under the Mac's Claude project path.
EOF
