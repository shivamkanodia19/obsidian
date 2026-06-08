---
name: superclaude-mcp-servers
description: Reference guide for SuperClaude MCP servers — which servers exist, what triggers them, required API keys, configuration JSON for ~/.claude.json, troubleshooting steps, and recommended server combinations for common workflows.
---

# SuperClaude MCP Servers

## Overview

MCP (Model Context Protocol) servers extend Claude Code's capabilities through specialized tools. SuperClaude integrates 8 MCP servers and provides Claude with instructions on when to activate them based on your tasks.

- **What MCP servers are**: External Node.js processes that provide additional tools
- **What they aren't**: Built-in SuperClaude functionality
- **How activation works**: Claude reads instructions to use appropriate servers based on context

## Servers at a Glance

| Server | Purpose | API Key Required |
|--------|---------|-----------------|
| **context7** | Official library documentation and patterns | No |
| **sequential-thinking** | Multi-step reasoning and analysis | No |
| **magic** | Modern UI component generation (21st.dev) | Yes — `TWENTYFIRST_API_KEY` |
| **playwright** | Browser automation and E2E testing | No |
| **morphllm-fast-apply** | Pattern-based code transformations | Yes — `MORPH_API_KEY` |
| **serena** | Semantic code understanding and project memory | No (needs Python 3.9+ + uv) |
| **tavily** | Web search and real-time information retrieval | Yes — `TAVILY_API_KEY` (free tier) |
| **chrome-devtools** | Performance analysis and debugging | No |

## Auto-Activation Triggers

| Request Contains | Servers Activated |
|-----------------|------------------|
| Library imports, API names | **context7** |
| `--think`, debugging | **sequential-thinking** |
| `component`, `UI`, frontend | **magic** |
| `test`, `e2e`, `browser` | **playwright** |
| Multi-file edits, refactoring | **morphllm-fast-apply** |
| Large projects, sessions | **serena** |
| `/sc:research`, `latest`, `current` | **tavily** |
| `performance`, `debug`, `LCP` | **chrome-devtools** |

## Configuration (`~/.claude.json`)

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "magic": {
      "command": "npx",
      "args": ["@21st-dev/magic"],
      "env": {"TWENTYFIRST_API_KEY": "${TWENTYFIRST_API_KEY}"}
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "morphllm-fast-apply": {
      "command": "npx",
      "args": ["@morph-llm/morph-fast-apply"],
      "env": {"MORPH_API_KEY": "${MORPH_API_KEY}"}
    },
    "serena": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide-assistant"]
    },
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {"TAVILY_API_KEY": "${TAVILY_API_KEY}"}
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

## API Key Setup

```bash
export TWENTYFIRST_API_KEY="your_key_here"   # magic — paid
export MORPH_API_KEY="your_key_here"         # morphllm — paid
export TAVILY_API_KEY="tvly-your_key_here"   # tavily — free tier at https://app.tavily.com

# Persist in shell profile
echo 'export TAVILY_API_KEY="tvly-..."' >> ~/.bashrc
```

## Server Combinations by Workflow

| Workflow | Servers |
|---------|---------|
| Free (no API keys) | context7 + sequential-thinking + playwright + serena |
| Learning / analysis | context7 + sequential-thinking |
| Web development | magic + context7 + playwright |
| Enterprise refactoring | serena + morphllm + sequential-thinking |
| Deep research | tavily + sequential-thinking + serena + playwright |
| Current events / web search | tavily + context7 + sequential-thinking |
| Performance tuning | chrome-devtools + sequential-thinking + playwright |

## Manual Server Control

```bash
# Enable specific servers
/sc:analyze codebase/ --c7 --seq

# Disable all MCP servers
/sc:implement "simple function" --no-mcp

# Enable all servers
/sc:design "complex architecture" --all-mcp
```

## Tavily Research Depth

```bash
--depth quick       # 5-10 sources, basic synthesis
--depth standard    # 10-20 sources, structured report (default)
--depth deep        # 20-40 sources, comprehensive analysis
--depth exhaustive  # 40+ sources, academic-level research
```

## Unified Gateway Alternative (AIRIS)

Single SSE endpoint instead of 8 stdio connections. Provides 50 tools from 7 servers with lazy loading.

```bash
git clone https://github.com/agiletec-inc/airis-mcp-gateway.git
cd airis-mcp-gateway
docker compose up -d
claude mcp add --scope user --transport sse airis-mcp-gateway http://localhost:9400/sse
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| No servers connected | Check `node --version` — need v16+ |
| Context7 fails | `npm cache clean --force` |
| Magic / Morphllm errors | Expected without API keys (paid) |
| Server timeouts | Restart Claude Code session |

```bash
# Test without MCP
/sc:command --no-mcp

# Check config exists
ls ~/.claude.json
```
