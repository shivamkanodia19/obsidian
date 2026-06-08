"""
Robinhood Crypto adapter — V0 stub.

Robinhood Crypto API is separate from their equity platform.
They have announced a public API for crypto (crypto.robinhood.com/api).
This stub prepares the interface for when we integrate it.

Crypto is disabled by default in risk_limits.yaml.
"""

from __future__ import annotations

from typing import Any

from ..agents.schemas import OrderTicket
from ..utils.logging import get_logger
from .broker_interfaces import BrokerInterface

logger = get_logger(__name__)


class RobinhoodCryptoClient(BrokerInterface):

    def get_name(self) -> str:
        return "robinhood_crypto_stub"

    def is_live(self) -> bool:
        return False

    def get_quote(self, asset_or_market: str) -> dict[str, Any]:
        """TODO (V2+): Implement via Robinhood Crypto API."""
        logger.warning(f"RobinhoodCryptoClient stub called for {asset_or_market}")
        return {"stub": True, "bid": None, "ask": None, "last": None, "volume": None}

    def submit_order(self, ticket: OrderTicket) -> dict[str, Any]:
        raise NotImplementedError("Robinhood Crypto trading not implemented in V0.")
