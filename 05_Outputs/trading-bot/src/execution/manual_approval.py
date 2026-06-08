"""
Manual approval gate.
Any function in the live execution path must call require_confirmation() first.
This module exists to make the confirmation step explicit and auditable.
"""

from __future__ import annotations

from ..agents.schemas import OrderTicket
from ..config import get_settings
from ..utils.logging import get_logger

logger = get_logger(__name__)


def require_confirmation(ticket: OrderTicket, prompt_fn=None) -> bool:
    """
    Gate that blocks execution unless the user explicitly confirms.
    In CLI context, prompt_fn is click.confirm. In tests, pass a mock.

    Returns True if confirmed, False if declined.
    Always logs the decision.
    """
    settings = get_settings()

    if not settings.require_manual_confirmation:
        logger.warning(
            "REQUIRE_MANUAL_CONFIRMATION is False — bypassing confirmation gate. "
            "This should only be done in automated testing with paper trades."
        )
        return True

    if settings.allow_live_trading and ticket.broker not in ("paper", "kalshi_demo"):
        logger.critical(
            f"LIVE TRADE CONFIRMATION REQUIRED for ticket {ticket.id}. "
            f"Broker: {ticket.broker}. Asset: {ticket.asset_or_market}. "
            f"Max loss: ${ticket.estimated_max_loss:.2f}"
        )

    if prompt_fn is None:
        # Non-interactive fallback: deny by default
        logger.warning("No prompt_fn provided to require_confirmation — denying by default.")
        return False

    confirmed = prompt_fn(
        f"\nConfirm execution of order ticket {ticket.id}?\n"
        f"  Asset: {ticket.asset_or_market}\n"
        f"  Side: {ticket.side.value}\n"
        f"  Type: {ticket.order_type.value} @ {ticket.limit_price}\n"
        f"  Qty: {ticket.quantity}\n"
        f"  Est. max loss: ${ticket.estimated_max_loss:.2f}\n"
        f"  Broker: {ticket.broker}\n"
        f"Proceed?"
    )

    logger.info(f"Manual confirmation for ticket {ticket.id}: {'CONFIRMED' if confirmed else 'DENIED'}")
    return confirmed
