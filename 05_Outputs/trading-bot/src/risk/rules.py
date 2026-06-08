"""
Deterministic risk rules loaded from risk_limits.yaml.
These are hard limits — not LLM suggestions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class RiskLimits:
    # Account-level
    max_daily_loss_dollars: float = 50.0
    max_open_positions: int = 5
    max_allocation_per_trade_percent: float = 10.0

    # Trade-level
    max_trade_risk_dollars: float = 25.0
    reject_market_orders: bool = True
    max_spread_percent: float = 3.0
    min_liquidity_threshold: float = 100.0
    max_thesis_age_minutes: int = 60

    # Asset classes
    allow_equities: bool = True
    allow_options: bool = False
    allow_crypto: bool = False
    allow_prediction_markets: bool = True
    allow_futures: bool = False

    # Execution gates
    allow_live_trading: bool = False
    require_manual_confirmation: bool = True
    allowed_brokers: list[str] = field(default_factory=lambda: ["paper", "kalshi_demo"])

    # Risk score thresholds
    approve_below: int = 40
    warn_above: int = 40
    reject_above: int = 70

    @classmethod
    def from_yaml(cls, path: Path) -> "RiskLimits":
        with open(path, encoding="utf-8") as f:
            raw: dict[str, Any] = yaml.safe_load(f)

        account = raw.get("account", {})
        trade = raw.get("trade", {})
        assets = raw.get("asset_classes", {})
        execution = raw.get("execution", {})
        thresholds = raw.get("risk_score_thresholds", {})
        warn_range = thresholds.get("warn_between", [40, 70])

        return cls(
            max_daily_loss_dollars=account.get("max_daily_loss_dollars", 50.0),
            max_open_positions=account.get("max_open_positions", 5),
            max_allocation_per_trade_percent=account.get("max_allocation_per_trade_percent", 10.0),
            max_trade_risk_dollars=trade.get("max_trade_risk_dollars", 25.0),
            reject_market_orders=trade.get("reject_market_orders", True),
            max_spread_percent=trade.get("max_spread_percent", 3.0),
            min_liquidity_threshold=trade.get("min_liquidity_threshold", 100.0),
            max_thesis_age_minutes=trade.get("max_thesis_age_minutes", 60),
            allow_equities=assets.get("allow_equities", True),
            allow_options=assets.get("allow_options", False),
            allow_crypto=assets.get("allow_crypto", False),
            allow_prediction_markets=assets.get("allow_prediction_markets", True),
            allow_futures=assets.get("allow_futures", False),
            allow_live_trading=execution.get("allow_live_trading", False),
            require_manual_confirmation=execution.get("require_manual_confirmation", True),
            allowed_brokers=execution.get("allowed_brokers", ["paper", "kalshi_demo"]),
            approve_below=thresholds.get("approve_below", 40),
            warn_above=warn_range[0] if warn_range else 40,
            reject_above=thresholds.get("reject_above", 70),
        )
