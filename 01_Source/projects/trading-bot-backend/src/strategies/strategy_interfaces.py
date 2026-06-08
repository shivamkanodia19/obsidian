"""
Strategy scanner interfaces — V0 stubs.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from ..agents.schemas import KalshiMarketScan, EquityWatchlistItem


class ScannerInterface(ABC):

    @abstractmethod
    def scan(self) -> list:
        """Return a list of scan results."""
        ...
