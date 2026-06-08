"""
Kalshi market scanner — finds active markets worth researching.
V0: delegates to KalshiClient.get_markets() with allowlist filter.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ..brokers import KalshiClient
from ..agents.schemas import KalshiMarketScan
from .strategy_interfaces import ScannerInterface


class KalshiMarketScanner(ScannerInterface):

    def __init__(self) -> None:
        self._client = KalshiClient()
        self._allowed_series = self._load_allowed_series()

    def _load_allowed_series(self) -> list[str]:
        path = Path(__file__).parent.parent / "config" / "assets_allowlist.yaml"
        if not path.exists():
            return []
        with open(path) as f:
            data: dict[str, Any] = yaml.safe_load(f)
        return [s.get("series", "") for s in data.get("kalshi_series", [])]

    def scan(self) -> list[KalshiMarketScan]:
        results = []
        if not self._allowed_series:
            return self._client.get_markets(limit=20)

        for series in self._allowed_series:
            markets = self._client.get_markets(series_ticker=series, limit=10)
            results.extend(markets)
        return results
