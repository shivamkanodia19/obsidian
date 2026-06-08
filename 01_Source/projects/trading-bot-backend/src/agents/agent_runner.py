"""
Agent runner — calls Claude API with a prompt file and returns structured output.
This is the ONLY place LLM calls happen. Everything else is deterministic code.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import get_settings
from ..utils.logging import get_logger

logger = get_logger(__name__)

PROMPTS_DIR = Path(__file__).parent / "prompts"


def _load_prompt(agent_name: str) -> str:
    path = PROMPTS_DIR / f"{agent_name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def run_agent(agent_name: str, user_message: str, extra_context: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    Call an agent with a user message and return parsed JSON output.

    Args:
        agent_name: one of research_agent | strategy_agent | risk_agent |
                    execution_agent | review_agent | skeptic_agent
        user_message: the specific request / data to pass
        extra_context: optional dict merged into user message as additional context

    Returns:
        Parsed dict from the agent's JSON output

    Raises:
        ValueError: if Anthropic API key not configured
        RuntimeError: if agent returns non-JSON or unexpected format
    """
    settings = get_settings()

    if not settings.anthropic_api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not set. Agent calls are disabled. "
            "Set the key in .env to enable LLM agents."
        )

    try:
        import anthropic
    except ImportError:
        raise RuntimeError("anthropic package not installed. Run: pip install anthropic")

    system_prompt = _load_prompt(agent_name)

    full_message = user_message
    if extra_context:
        context_str = json.dumps(extra_context, indent=2, default=str)
        full_message = f"{user_message}\n\nAdditional context:\n```json\n{context_str}\n```"

    logger.info(f"Running agent: {agent_name}")

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    response = client.messages.create(
        model=settings.anthropic_model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": full_message}],
    )

    raw_text = response.content[0].text
    logger.debug(f"Agent {agent_name} raw output: {raw_text[:500]}...")

    # Extract JSON from the response — agents are instructed to return JSON
    parsed = _extract_json(raw_text)
    parsed["_raw_agent_output"] = raw_text
    parsed["_agent_name"] = agent_name
    return parsed


def _extract_json(text: str) -> dict[str, Any]:
    """Extract JSON from agent output, handling markdown code fences."""
    text = text.strip()

    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting from ```json ... ``` blocks
    import re
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # Try finding first { ... } block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    raise RuntimeError(
        f"Agent returned output that could not be parsed as JSON. "
        f"First 500 chars: {text[:500]}"
    )
