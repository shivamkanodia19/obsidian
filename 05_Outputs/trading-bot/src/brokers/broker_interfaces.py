"""
Abstract broker interface.
All broker clients must implement this interface.
The risk engine and execution layer talk to this — never directly to broker clients.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..agents.schemas import KalshiMarketScan, EquityWatchlistItem, OrderTicket


class BrokerInterface(ABC):

    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def is_live(self) -> bool:
        """Returns True if this broker executes real money trades."""
        ...

    @abstractmethod
    def get_quote(self, asset_or_market: str) -> dict[str, Any]:
        """
        Return a quote dict with at minimum:
        {'bid': float, 'ask': float, 'last': float, 'volume': float}
        """
        ...

    @abstractmethod
    def submit_order(self, ticket: OrderTicket) -> dict[str, Any]:
        """
        Submit an order. Must raise NotImplementedError if live trading is disabled.
        Returns broker confirmation dict.
        """
        ...

    def get_spread_percent(self, bid: float, ask: float) -> float:
        if ask <= 0:
            return 100.0
        return ((ask - bid) / ask) * 100
