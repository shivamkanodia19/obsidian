"""
Order ticket creation helpers.
Ticket creation is separate from execution — a ticket is just a structured intent.
"""

from __future__ import annotations

from ..agents.schemas import (
    AssetType,
    ExecutionStatus,
    OrderSide,
    OrderTicket,
    OrderType,
    TradeProposal,
)
from ..risk import check_ticket
from ..utils.ids import new_id


def create_order_ticket(
    proposal: TradeProposal,
    risk_engine_result_id: str,
    broker: str,
    side: OrderSide,
    limit_price: float,
    quantity: float,
    stop_price: float | None = None,
    notes: str = "",
) -> tuple[OrderTicket, list[str]]:
    """
    Create an OrderTicket from an approved proposal.
    Returns (ticket, errors). If errors is non-empty, ticket is invalid and should not be used.
    """
    estimated_max_loss: float
    if stop_price is not None:
        estimated_max_loss = abs(limit_price - stop_price) * quantity
    else:
        # Conservative fallback: assume full position is at risk (for prediction markets, etc.)
        estimated_max_loss = limit_price * quantity

    ticket = OrderTicket(
        id=new_id(),
        proposal_id=proposal.id,
        risk_engine_result_id=risk_engine_result_id,
        broker=broker,
        asset_or_market=proposal.asset_or_market,
        asset_type=proposal.asset_type,
        side=side,
        order_type=OrderType.LIMIT,
        limit_price=limit_price,
        quantity=quantity,
        estimated_max_loss=round(estimated_max_loss, 4),
        requires_user_confirmation=True,
        execution_status=ExecutionStatus.PENDING_APPROVAL,
        notes=notes,
    )

    errors = check_ticket(ticket)
    return ticket, errors
