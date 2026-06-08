"""
Equity watchlist scanner — V0 stub.
TODO (V1): Fetch live quotes via official Robinhood API or alternative data source.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ..agents.schemas import EquityWatchlistItem
from .strategy_interfaces import ScannerInterface


class EquityWatchlistScanner(ScannerInterface):

    def scan(self) -> list[EquityWatchlistItem]:
        """Returns allowlist tickers with null prices (no live data in V0)."""
        path = Path(__file__).parent.parent / "config" / "assets_allowlist.yaml"
        if not path.exists():
            return []
        with open(path) as f:
            data: dict[str, Any] = yaml.safe_load(f)
        return [
            EquityWatchlistItem(
                ticker=e.get("ticker", ""),
                notes=e.get("notes", ""),
            )
            for e in data.get("equities", [])
        ]
