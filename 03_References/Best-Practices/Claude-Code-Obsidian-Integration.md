---
title: Claude Code + Obsidian — Best Practices
type: pattern
source: GitHub research (AgriciDaniel/claude-obsidian, az9713/claude-code-obsidian, iansinnott/obsidian-claude-code-mcp)
relevance: obsidian, claude-code, workflow, vault-integration
version: 1.0
tested_in: wave-4-outreach
last_updated: 2026-05-11
---

# Claude Code + Obsidian Integration — Best Practices

Research-backed patterns for integrating Claude Code with Obsidian vaults.

---

## Integration Strategies

### 1. Vault-as-Working-Directory (Recommended)

Open the Obsidian vault folder in Claude Code as the working directory. CLAUDE.md at vault root serves double duty:
- Instructions for Claude
- Readable note in Obsidian

**Pros:** Single directory context, minimal setup, CLAUDE.md is discoverable
**Cons:** Requires vault folder as working directory

### 2. MCP Server Integration

Run [obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) — MCP server lets Claude query vault without it being the working directory.

**How it works:**
- Plugin auto-discovers vaults via WebSocket on port 22360
- Multiple vaults each need unique ports
- Plugin guides you to configure different ports if conflicts detected

**Pros:** Vault and repo can be separate; multiple vault support
**Cons:** Requires plugin + port configuration

### 3. Knowledge Base Strategy (Separate)

Keep repos clean. Give Claude access to vault knowledge base separately:
- Claude Code runs in repo directory
- CLAUDE.md references external wiki path: `## Wiki Knowledge Base Path: ~/path/to/vault`
- Claude reads wiki/hot.md first (recent cache), then wiki/index.md

**Pros:** Repo stays focused; vault stays separate
**Cons:** Requires manual path configuration

---

## Vault Structure (Proven Template)

Based on [Claudesidian](https://github.com/heyitsnoah/claudesidian) and [az9713/claude-code-obsidian](https://github.com/az9713/claude-code-obsidian):

```
vault/
├── CLAUDE.md                     # Instructions for Claude + readable note
├── .claude/
│   ├── skills/                   # Claude Code skills (auto-loaded)
│   ├── CLAUDE.md                 # Skill-specific config
│   ├── settings.json             # Session settings
│   └── projects/[project]/memory # Project memory files
├── 00_Inbox/                     # Quick capture, unprocessed
├── 01_Projects/                  # Active work
├── 02_Areas/                     # Responsibility areas
├── 03_References/                # Knowledge base (frameworks, tools, patterns)
├── 04_Archive/                   # Completed projects, old notes (>6 months)
├── 05_Attachments/               # Images, PDFs, etc.
├── 06_Metadata/                  # Vault config, graph.json, app.json
└── daily/                        # Daily notes (auto-created)
```

---

## Frontmatter Standards (AI-Readable)

Include structured metadata at top of every note:

```yaml
---
title: [Simple, idea-focused title]
project: [Project key, if applicable]
type: [reference|note|project|decision|research]
tags: [comma, separated, tags]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: [active|complete|archived]
---
```

**Why this matters for Claude:**
- Claude can parse frontmatter to understand note type + currency
- `last_updated` tells Claude when info was verified
- `project` lets Claude connect related notes
- `status` tells Claude if note is active or historical

---

## CLAUDE.md Configuration

Root CLAUDE.md + optional project-specific CLAUDE.md files in `.claude/projects/[project]/`:

**Root CLAUDE.md includes:**
- Identity (who is Claude in this context)
- Vault structure map
- Hard rules (what Claude can/cannot do)
- Organization rules (folder structure, naming conventions)
- Workflow (how Claude should process tasks)
- Token efficiency (which files to read first)
- Frontmatter schemas (for all note types)

**Project-specific CLAUDE.md (optional):**
- Project-specific rules
- Project memory location
- Project-specific skills
- Project conventions

---

## Skills Integration

Place Claude Code skills in `.claude/skills/`:

```
.claude/skills/
├── skill-name-1/
│   └── SKILL.md
├── skill-name-2/
│   └── SKILL.md
└── ...
```

Skills auto-load when Claude Code opens from vault directory. Skills should reference vault patterns + memory system.

---

## Memory System (For Claude's Cross-Session Persistence)

**Structure:**
```
.claude/projects/[project]/memory/
├── MEMORY.md                     # Index (1-line hooks only)
├── user_profile.md               # User context
├── feedback_*.md                 # User feedback collected
├── project_*.md                  # Project status + learnings
├── reference_*.md                # External pointers
└── archive/                      # >6 months old
```

**Frontmatter schema (Memory files):**
```yaml
---
name: [Memory name]
description: [One-line hook for relevance search]
type: [user|feedback|project|reference]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
relevance: [comma-separated keywords]
---
```

**Key principle:** Memory is for CLAUDE'S use across sessions. User adds to memory; Claude organizes it automatically.

---

## Automation Rules (What Claude Should Do)

### /save-audit Workflow
Treat `/save-audit` as the vault-facing contract with two internal phases.

Save phase:
1. Read the relevant new Source or working context
2. Synthesize durable reasoning into Analyst or Outputs
3. Create or update the nearest useful folder indexes
4. Update memory, task cards, or run logs when the work is substantial
5. Log conflicts if new material contradicts prior Analyst state

Audit phase:
1. Scan vault structure and top entrypoints
2. Auto-fix safe structural issues such as missing indexes for active folders
3. Surface broken or brittle links for review
4. Keep major hub pages lean by moving long history into dedicated logs
5. Move stale memories (>6 months) to archive when appropriate

**Claude should handle organization proactively, but keep index pages as navigators rather than giant histories.**

---

## Token Efficiency Strategies

From [az9713/claude-code-obsidian](https://github.com/az9713/claude-code-obsidian) (tested on large vaults):

1. **Read frontmatter-first:** Use frontmatter to decide if full file is needed
2. **Load indexes instead of scanning:** Navigate via _index.md, never read folders blindly
3. **Hot file pattern:** Maintain `hot.md` or recent-context file for quick context
4. **Lazy-load details:** Link to external files instead of embedding long content
5. **Archive aggressively:** Files >6 months old → archive folder (reduces active file count)

**Result:** Can scale to hundreds of folders + tens of thousands of notes without token bloat.

---

## Examples from Production Use

### Example 1: Project-Based Structure
```
01_Projects/Wave-4-Outreach/
├── _index.md                     # Navigation
├── ACTION-ITEMS/
│   ├── _index.md
│   ├── TASK-1.md
│   └── TASK-2.md
├── RESEARCH/
│   └── _index.md
└── REFERENCE/
    └── _index.md
```
Claude finds ACTION-ITEMS immediately, never gets lost in files.

### Example 2: Cross-Project Memory
```
.claude/projects/Wave-4-Outreach/memory/
├── MEMORY.md (index)
├── project_wave4_internship.md (status, learnings)
├── feedback_email_optimization.md (discovered patterns)
└── reference_industry_research.md (external pointers)
```
Next session, Claude loads MEMORY.md, sees keywords, loads relevant files. No context loss.

---

## Common Pitfalls to Avoid

❌ **Sprawling folder structure** — Keep depth <4 levels. Use clear naming.
❌ **Missing indexes** — Every folder needs _index.md. Claude gets lost without it.
❌ **No frontmatter** — Claude can't parse context without YAML headers.
❌ **Stale content in active folders** — Archive >6 months old. Reduces noise.
❌ **No memory system** — Claude loses learnings between sessions. Use memory.
❌ **Orphaned files** — Files with no parent context. Always file into projects/areas.
❌ **Broken wikilinks** — Keep links current. Broken links = lost context.

---

## When to Use Each Pattern

| Strategy | Best For | When to Use |
|----------|----------|------------|
| Vault-as-working-directory | Single focused project | Default for focused work |
| MCP Server | Multiple vaults | When you have separate knowledge base + project repos |
| Knowledge Base Strategy | Large organizations | When vault is shared, repos are personal |

---

## Sources

- [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Persistent wiki vault pattern based on Karpathy's LLM wiki
- [az9713/claude-code-obsidian](https://github.com/az9713/claude-code-obsidian) — Skills + vault config for large vaults
- [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) — MCP server integration
- [Obsidian + Claude Code: The Complete Integration Guide](https://blog.starmorph.com/blog/obsidian-claude-code-integration-guide)
- [The Claude Code Skills That Make Your Obsidian Vault Feel Alive](https://medium.com/@martk/obsidian-claude-code-the-claude-code-skills-that-make-your-vault-feel-alive-4ec05a1ec1e6) — Medium article on skills integration

---

## Iterations

[2026-04-15] v1.0 — Initial documentation from GitHub research. Three integration strategies, proven vault structure, frontmatter standards, automation rules, token efficiency patterns.
