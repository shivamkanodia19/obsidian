#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tomllib
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


CHICAGO_TZ = ZoneInfo("America/Chicago")


@dataclass
class VaultPaths:
    app_dir: Path
    vault_root: Path
    config_dir: Path
    runtime_dir: Path
    notes_root: Path
    proposals_data_dir: Path
    risk_data_dir: Path
    approvals_data_dir: Path
    reviews_data_dir: Path
    executions_data_dir: Path
    proposals_note_dir: Path
    risk_note_dir: Path
    approvals_note_dir: Path
    reviews_note_dir: Path
    journal_note_dir: Path
    snapshot_note_dir: Path
    broker_state_path: Path

    @property
    def policy_path(self) -> Path:
        return self.config_dir / "risk_policy.toml"

    def managed_runtime_dirs(self) -> list[Path]:
        return [
            self.proposals_data_dir,
            self.risk_data_dir,
            self.approvals_data_dir,
            self.reviews_data_dir,
            self.executions_data_dir,
        ]

    def managed_note_dirs(self) -> list[Path]:
        return [
            self.proposals_note_dir,
            self.risk_note_dir,
            self.approvals_note_dir,
            self.reviews_note_dir,
            self.journal_note_dir,
            self.snapshot_note_dir,
        ]


@dataclass
class RiskPolicy:
    market_timezone: str
    max_trade_size_usd: float
    max_account_exposure_percent: float
    max_single_ticker_exposure_percent: float
    max_trades_per_day: int
    allow_market_orders: bool
    allow_options: bool
    allow_short_sales: bool
    allow_after_hours: bool
    require_initial_approval: bool
    require_final_approval: bool
    blocked_tickers: list[str] = field(default_factory=list)


@dataclass
class TradeProposal:
    proposal_id: str
    created_at: str
    ticker: str
    asset_type: str
    direction: str
    order_type: str
    order_session: str
    position_size_usd: float
    limit_price: float
    time_horizon: str
    thesis: str
    invalidation: str
    confidence: str
    strategy_tag: str
    source_note: str | None
    requires_initial_approval: bool
    requires_final_approval: bool
    status: str = "drafted"

    def initial_approval_phrase(self) -> str:
        return (
            f"APPROVE TRADE: {self.ticker} {self.direction.upper()} "
            f"{self.position_size_usd:.2f} USD LIMIT {self.limit_price:.2f} [{self.proposal_id}]"
        )

    def final_approval_phrase(self) -> str:
        return (
            f"FINAL APPROVE TRADE: {self.ticker} {self.direction.upper()} "
            f"{self.position_size_usd:.2f} USD LIMIT {self.limit_price:.2f} [{self.proposal_id}]"
        )


def make_default_paths(script_file: Path | None = None) -> VaultPaths:
    script_path = (script_file or Path(__file__)).resolve()
    app_dir = script_path.parent
    vault_root = app_dir.parents[2]
    config_dir = app_dir / "config"
    runtime_dir = app_dir / "runtime"
    notes_root = vault_root / "02_Analyst" / "stocks" / "agentic-trading"
    return VaultPaths(
        app_dir=app_dir,
        vault_root=vault_root,
        config_dir=config_dir,
        runtime_dir=runtime_dir,
        notes_root=notes_root,
        proposals_data_dir=runtime_dir / "proposals",
        risk_data_dir=runtime_dir / "risk-checks",
        approvals_data_dir=runtime_dir / "approvals",
        reviews_data_dir=runtime_dir / "reviews",
        executions_data_dir=runtime_dir / "executions",
        proposals_note_dir=notes_root / "proposals",
        risk_note_dir=notes_root / "risk-checks",
        approvals_note_dir=notes_root / "approvals",
        reviews_note_dir=notes_root / "reviews",
        journal_note_dir=notes_root / "journal",
        snapshot_note_dir=notes_root / "snapshots",
        broker_state_path=runtime_dir / "mock_broker_state.json",
    )


def make_paths_for_testing(base_dir: Path) -> VaultPaths:
    app_dir = base_dir / "05_Outputs" / "automation-code" / "robinhood-trading-cockpit"
    notes_root = base_dir / "02_Analyst" / "stocks" / "agentic-trading"
    return VaultPaths(
        app_dir=app_dir,
        vault_root=base_dir,
        config_dir=app_dir / "config",
        runtime_dir=app_dir / "runtime",
        notes_root=notes_root,
        proposals_data_dir=app_dir / "runtime" / "proposals",
        risk_data_dir=app_dir / "runtime" / "risk-checks",
        approvals_data_dir=app_dir / "runtime" / "approvals",
        reviews_data_dir=app_dir / "runtime" / "reviews",
        executions_data_dir=app_dir / "runtime" / "executions",
        proposals_note_dir=notes_root / "proposals",
        risk_note_dir=notes_root / "risk-checks",
        approvals_note_dir=notes_root / "approvals",
        reviews_note_dir=notes_root / "reviews",
        journal_note_dir=notes_root / "journal",
        snapshot_note_dir=notes_root / "snapshots",
        broker_state_path=app_dir / "runtime" / "mock_broker_state.json",
    )


def now_iso(tz_name: str = "America/Chicago") -> str:
    return datetime.now(ZoneInfo(tz_name)).isoformat(timespec="seconds")


def timestamp_slug() -> str:
    return datetime.now(CHICAGO_TZ).strftime("%Y%m%dT%H%M%S")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def ensure_structure(paths: VaultPaths) -> None:
    paths.config_dir.mkdir(parents=True, exist_ok=True)
    paths.runtime_dir.mkdir(parents=True, exist_ok=True)
    paths.notes_root.mkdir(parents=True, exist_ok=True)
    for directory in paths.managed_runtime_dirs():
        directory.mkdir(parents=True, exist_ok=True)
    for directory in paths.managed_note_dirs():
        directory.mkdir(parents=True, exist_ok=True)


def reset_managed_state(paths: VaultPaths) -> None:
    for directory in paths.managed_runtime_dirs():
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)
    for directory in paths.managed_note_dirs():
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)
    if paths.broker_state_path.exists():
        paths.broker_state_path.unlink()


def load_risk_policy(policy_path: Path) -> RiskPolicy:
    raw = tomllib.loads(policy_path.read_text(encoding="utf-8"))
    limits = raw.get("limits", {})
    permissions = raw.get("permissions", {})
    hours = raw.get("hours", {})
    lists = raw.get("lists", {})
    return RiskPolicy(
        market_timezone=hours.get("timezone", "America/Chicago"),
        max_trade_size_usd=float(limits.get("max_trade_size_usd", 75)),
        max_account_exposure_percent=float(limits.get("max_account_exposure_percent", 35)),
        max_single_ticker_exposure_percent=float(limits.get("max_single_ticker_exposure_percent", 15)),
        max_trades_per_day=int(limits.get("max_trades_per_day", 2)),
        allow_market_orders=bool(permissions.get("allow_market_orders", False)),
        allow_options=bool(permissions.get("allow_options", False)),
        allow_short_sales=bool(permissions.get("allow_short_sales", False)),
        allow_after_hours=bool(permissions.get("allow_after_hours", False)),
        require_initial_approval=bool(permissions.get("require_initial_approval", True)),
        require_final_approval=bool(permissions.get("require_final_approval", True)),
        blocked_tickers=list(lists.get("blocked_tickers", [])),
    )


def default_mock_broker_state() -> dict[str, Any]:
    return {
        "account_id": "mock-agentic-001",
        "currency": "USD",
        "updated_at": now_iso(),
        "buying_power_usd": 450.0,
        "positions": [
            {
                "ticker": "QQQM",
                "quantity": 0.25,
                "avg_price": 186.0,
                "last_price": 188.1,
            }
        ],
        "quotes": {
            "IBIT": 42.05,
            "NVDA": 950.0,
            "QQQM": 188.1,
            "SPY": 529.8,
            "MSTR": 1825.0,
        },
        "orders": [],
    }


def bootstrap_mock_state(paths: VaultPaths) -> dict[str, Any]:
    if not paths.broker_state_path.exists():
        state = default_mock_broker_state()
        write_json(paths.broker_state_path, state)
        return state
    return read_json(paths.broker_state_path)


def account_value_usd(state: dict[str, Any]) -> float:
    positions_value = sum(float(position["quantity"]) * float(position["last_price"]) for position in state["positions"])
    return round(float(state["buying_power_usd"]) + positions_value, 2)


def total_long_exposure_usd(state: dict[str, Any]) -> float:
    return round(sum(float(position["quantity"]) * float(position["last_price"]) for position in state["positions"]), 2)


def ticker_exposure_usd(state: dict[str, Any], ticker: str) -> float:
    return round(
        sum(
            float(position["quantity"]) * float(position["last_price"])
            for position in state["positions"]
            if position["ticker"].upper() == ticker.upper()
        ),
        2,
    )


def today_fill_count(state: dict[str, Any], tz_name: str) -> int:
    today = datetime.now(ZoneInfo(tz_name)).date()
    count = 0
    for order in state["orders"]:
        filled_at = order.get("filled_at")
        if not filled_at:
            continue
        order_date = datetime.fromisoformat(filled_at).astimezone(ZoneInfo(tz_name)).date()
        if order.get("status") == "filled" and order_date == today:
            count += 1
    return count


def build_proposal(
    ticker: str,
    position_size_usd: float,
    limit_price: float,
    thesis: str,
    invalidation: str,
    time_horizon: str,
    confidence: str,
    strategy_tag: str,
    source_note: str | None,
    requires_initial_approval: bool,
    requires_final_approval: bool,
) -> TradeProposal:
    proposal_id = f"TP-{timestamp_slug()}-{ticker.upper()}"
    return TradeProposal(
        proposal_id=proposal_id,
        created_at=now_iso(),
        ticker=ticker.upper(),
        asset_type="equity",
        direction="buy",
        order_type="limit",
        order_session="regular",
        position_size_usd=round(position_size_usd, 2),
        limit_price=round(limit_price, 2),
        time_horizon=time_horizon,
        thesis=thesis.strip(),
        invalidation=invalidation.strip(),
        confidence=confidence,
        strategy_tag=strategy_tag,
        source_note=source_note,
        requires_initial_approval=requires_initial_approval,
        requires_final_approval=requires_final_approval,
    )


def save_proposal(paths: VaultPaths, proposal: TradeProposal) -> tuple[Path, Path]:
    data_path = paths.proposals_data_dir / f"{proposal.proposal_id}.json"
    note_path = paths.proposals_note_dir / f"{proposal.proposal_id}.md"
    payload = asdict(proposal)
    write_json(data_path, payload)
    write_text(note_path, render_proposal_note(proposal))
    return data_path, note_path


def load_proposal(paths: VaultPaths, proposal_id: str) -> TradeProposal:
    payload = read_json(paths.proposals_data_dir / f"{proposal_id}.json")
    return TradeProposal(**payload)


def load_latest_passed_risk(paths: VaultPaths, proposal_id: str) -> dict[str, Any] | None:
    path = paths.risk_data_dir / f"{proposal_id}.json"
    if not path.exists():
        return None
    payload = read_json(path)
    if payload.get("status") != "pass":
        return None
    return payload


def load_approval(paths: VaultPaths, proposal_id: str, stage: str) -> dict[str, Any] | None:
    path = paths.approvals_data_dir / f"{proposal_id}--{stage}.json"
    if not path.exists():
        return None
    return read_json(path)


def load_review(paths: VaultPaths, proposal_id: str) -> dict[str, Any] | None:
    path = paths.reviews_data_dir / f"{proposal_id}.json"
    if not path.exists():
        return None
    return read_json(path)


def risk_check_record(proposal: TradeProposal, policy: RiskPolicy, state: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def add_check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "passed": passed, "detail": detail})

    add_check("asset-type", proposal.asset_type == "equity", f"asset type is {proposal.asset_type}")
    add_check("direction", proposal.direction == "buy" or policy.allow_short_sales, f"direction is {proposal.direction}")
    add_check(
        "order-type",
        proposal.order_type == "limit" or policy.allow_market_orders,
        f"order type is {proposal.order_type}",
    )
    add_check(
        "session",
        proposal.order_session == "regular" or policy.allow_after_hours,
        f"session is {proposal.order_session}",
    )
    add_check(
        "blocked-ticker",
        proposal.ticker not in {ticker.upper() for ticker in policy.blocked_tickers},
        f"ticker is {proposal.ticker}",
    )
    add_check(
        "trade-size",
        proposal.position_size_usd <= policy.max_trade_size_usd,
        f"trade size {proposal.position_size_usd:.2f} vs limit {policy.max_trade_size_usd:.2f}",
    )
    add_check(
        "buying-power",
        proposal.position_size_usd <= float(state["buying_power_usd"]),
        f"buying power is {float(state['buying_power_usd']):.2f}",
    )
    add_check(
        "trades-today",
        today_fill_count(state, policy.market_timezone) < policy.max_trades_per_day,
        f"filled trades today {today_fill_count(state, policy.market_timezone)} vs limit {policy.max_trades_per_day}",
    )

    current_account_value = max(account_value_usd(state), 0.01)
    current_total_exposure = total_long_exposure_usd(state)
    current_ticker_exposure = ticker_exposure_usd(state, proposal.ticker)
    projected_total_exposure = current_total_exposure + proposal.position_size_usd
    projected_ticker_exposure = current_ticker_exposure + proposal.position_size_usd
    projected_total_percent = round((projected_total_exposure / current_account_value) * 100, 2)
    projected_ticker_percent = round((projected_ticker_exposure / current_account_value) * 100, 2)

    add_check(
        "account-exposure",
        projected_total_percent <= policy.max_account_exposure_percent,
        f"projected total exposure {projected_total_percent:.2f}% vs limit {policy.max_account_exposure_percent:.2f}%",
    )
    add_check(
        "single-ticker-exposure",
        projected_ticker_percent <= policy.max_single_ticker_exposure_percent,
        (
            f"projected {proposal.ticker} exposure {projected_ticker_percent:.2f}% "
            f"vs limit {policy.max_single_ticker_exposure_percent:.2f}%"
        ),
    )

    status = "pass" if all(check["passed"] for check in checks) else "fail"
    return {
        "proposal_id": proposal.proposal_id,
        "ran_at": now_iso(),
        "status": status,
        "account_value_usd": round(current_account_value, 2),
        "projected_total_exposure_percent": projected_total_percent,
        "projected_ticker_exposure_percent": projected_ticker_percent,
        "checks": checks,
    }


def save_risk_check(paths: VaultPaths, proposal: TradeProposal, record: dict[str, Any]) -> tuple[Path, Path]:
    data_path = paths.risk_data_dir / f"{proposal.proposal_id}.json"
    note_path = paths.risk_note_dir / f"{proposal.proposal_id}.md"
    write_json(data_path, record)
    write_text(note_path, render_risk_note(proposal, record))
    return data_path, note_path


def create_approval_record(proposal: TradeProposal, stage: str, typed_phrase: str, approver: str) -> dict[str, Any]:
    expected = proposal.initial_approval_phrase() if stage == "initial" else proposal.final_approval_phrase()
    normalized_typed = " ".join(typed_phrase.strip().split())
    normalized_expected = " ".join(expected.strip().split())
    is_valid = normalized_typed == normalized_expected
    return {
        "proposal_id": proposal.proposal_id,
        "stage": stage,
        "created_at": now_iso(),
        "approver": approver,
        "typed_phrase": typed_phrase.strip(),
        "expected_phrase": expected,
        "is_valid": is_valid,
    }


def save_approval(paths: VaultPaths, proposal: TradeProposal, record: dict[str, Any]) -> tuple[Path, Path]:
    stage = record["stage"]
    data_path = paths.approvals_data_dir / f"{proposal.proposal_id}--{stage}.json"
    note_path = paths.approvals_note_dir / f"{proposal.proposal_id}--{stage}.md"
    write_json(data_path, record)
    write_text(note_path, render_approval_note(proposal, record))
    return data_path, note_path


def review_order(proposal: TradeProposal, state: dict[str, Any]) -> dict[str, Any]:
    reference_price = float(state["quotes"].get(proposal.ticker, proposal.limit_price))
    quantity = round(proposal.position_size_usd / proposal.limit_price, 6)
    delta_percent = round(((proposal.limit_price - reference_price) / reference_price) * 100, 2) if reference_price else 0.0
    warnings: list[str] = []
    if abs(delta_percent) > 3:
        warnings.append("limit price is more than 3% away from the mock reference quote")
    return {
        "proposal_id": proposal.proposal_id,
        "reviewed_at": now_iso(),
        "broker_mode": "mock",
        "status": "approved",
        "reference_price": round(reference_price, 2),
        "estimated_quantity": quantity,
        "estimated_notional_usd": round(proposal.position_size_usd, 2),
        "limit_delta_percent": delta_percent,
        "warnings": warnings,
    }


def save_review(paths: VaultPaths, proposal: TradeProposal, record: dict[str, Any]) -> tuple[Path, Path]:
    data_path = paths.reviews_data_dir / f"{proposal.proposal_id}.json"
    note_path = paths.reviews_note_dir / f"{proposal.proposal_id}.md"
    write_json(data_path, record)
    write_text(note_path, render_review_note(proposal, record))
    return data_path, note_path


def apply_fill_to_state(proposal: TradeProposal, state: dict[str, Any]) -> dict[str, Any]:
    quantity = round(proposal.position_size_usd / proposal.limit_price, 6)
    state["buying_power_usd"] = round(float(state["buying_power_usd"]) - proposal.position_size_usd, 2)
    existing = None
    for position in state["positions"]:
        if position["ticker"].upper() == proposal.ticker:
            existing = position
            break

    if existing is None:
        state["positions"].append(
            {
                "ticker": proposal.ticker,
                "quantity": quantity,
                "avg_price": proposal.limit_price,
                "last_price": float(state["quotes"].get(proposal.ticker, proposal.limit_price)),
            }
        )
    else:
        current_quantity = float(existing["quantity"])
        new_quantity = round(current_quantity + quantity, 6)
        total_cost = (current_quantity * float(existing["avg_price"])) + proposal.position_size_usd
        existing["quantity"] = new_quantity
        existing["avg_price"] = round(total_cost / new_quantity, 4)
        existing["last_price"] = float(state["quotes"].get(proposal.ticker, proposal.limit_price))

    order_id = f"MOCK-{timestamp_slug()}-{proposal.ticker}"
    order = {
        "order_id": order_id,
        "ticker": proposal.ticker,
        "status": "filled",
        "filled_at": now_iso(),
        "limit_price": proposal.limit_price,
        "notional_usd": proposal.position_size_usd,
        "quantity": quantity,
    }
    state["orders"].append(order)
    state["updated_at"] = now_iso()
    return order


def execute_order(paths: VaultPaths, proposal: TradeProposal) -> dict[str, Any]:
    policy = load_risk_policy(paths.policy_path)
    risk = load_latest_passed_risk(paths, proposal.proposal_id)
    if not risk:
        raise RuntimeError("proposal has not passed risk checks")

    if policy.require_initial_approval:
        initial = load_approval(paths, proposal.proposal_id, "initial")
        if not initial or not initial.get("is_valid"):
            raise RuntimeError("missing valid initial approval")

    if policy.require_final_approval:
        final = load_approval(paths, proposal.proposal_id, "final")
        if not final or not final.get("is_valid"):
            raise RuntimeError("missing valid final approval")

    review = load_review(paths, proposal.proposal_id)
    if not review or review.get("status") != "approved":
        raise RuntimeError("missing approved broker review")

    state = bootstrap_mock_state(paths)
    if proposal.position_size_usd > float(state["buying_power_usd"]):
        raise RuntimeError("buying power changed and is now too low for execution")

    order = apply_fill_to_state(proposal, state)
    write_json(paths.broker_state_path, state)
    execution = {
        "proposal_id": proposal.proposal_id,
        "executed_at": now_iso(),
        "broker_mode": "mock",
        "status": "filled",
        "order_id": order["order_id"],
        "filled_quantity": order["quantity"],
        "filled_notional_usd": order["notional_usd"],
        "limit_price": order["limit_price"],
        "buying_power_after_fill_usd": round(float(state["buying_power_usd"]), 2),
        "account_value_after_fill_usd": account_value_usd(state),
    }
    data_path = paths.executions_data_dir / f"{proposal.proposal_id}.json"
    note_path = paths.journal_note_dir / f"{proposal.proposal_id}.md"
    write_json(data_path, execution)
    write_text(note_path, render_journal_note(proposal, execution))
    return execution


def write_account_snapshot(paths: VaultPaths) -> tuple[dict[str, Any], Path, Path]:
    state = bootstrap_mock_state(paths)
    snapshot = {
        "generated_at": now_iso(),
        "account_id": state["account_id"],
        "buying_power_usd": round(float(state["buying_power_usd"]), 2),
        "account_value_usd": account_value_usd(state),
        "positions": state["positions"],
        "orders": state["orders"][-10:],
    }
    stamp = datetime.now(CHICAGO_TZ).strftime("%Y-%m-%d-%H%M%S")
    data_path = paths.snapshot_note_dir / f"account-status-{stamp}.json"
    note_path = paths.snapshot_note_dir / f"account-status-{stamp}.md"
    latest_note_path = paths.snapshot_note_dir / "latest-account-status.md"
    latest_json_path = paths.snapshot_note_dir / "latest-account-status.json"
    write_json(data_path, snapshot)
    write_json(latest_json_path, snapshot)
    note_content = render_snapshot_note(snapshot)
    write_text(note_path, note_content)
    write_text(latest_note_path, note_content)
    return snapshot, note_path, latest_note_path


def run_demo(paths: VaultPaths, reset: bool = True) -> dict[str, Any]:
    ensure_structure(paths)
    if reset:
        reset_managed_state(paths)
    bootstrap_mock_state(paths)
    policy = load_risk_policy(paths.policy_path)

    proposal = build_proposal(
        ticker="IBIT",
        position_size_usd=50.0,
        limit_price=42.0,
        thesis="Small starter position for a BTC-linked ETF while keeping single-trade risk capped.",
        invalidation="Cancel if the setup turns into a chase or if BTC thesis changes before execution.",
        time_horizon="2-10 days",
        confidence="medium",
        strategy_tag="vault-demo",
        source_note="02_Analyst/stocks/agentic-trading/_index.md",
        requires_initial_approval=policy.require_initial_approval,
        requires_final_approval=policy.require_final_approval,
    )
    save_proposal(paths, proposal)

    state = bootstrap_mock_state(paths)
    risk = risk_check_record(proposal, policy, state)
    save_risk_check(paths, proposal, risk)

    initial = create_approval_record(proposal, "initial", proposal.initial_approval_phrase(), "demo-user")
    save_approval(paths, proposal, initial)

    review = review_order(proposal, state)
    save_review(paths, proposal, review)

    final = create_approval_record(proposal, "final", proposal.final_approval_phrase(), "demo-user")
    save_approval(paths, proposal, final)

    execution = execute_order(paths, proposal)
    snapshot, _, latest_path = write_account_snapshot(paths)
    return {
        "proposal_id": proposal.proposal_id,
        "risk_status": risk["status"],
        "execution_status": execution["status"],
        "latest_snapshot_path": str(latest_path),
        "account_value_usd": snapshot["account_value_usd"],
    }


def render_frontmatter(title: str, extra: dict[str, Any]) -> str:
    lines = ["---", f"title: {title}"]
    for key, value in extra.items():
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def json_fence(payload: dict[str, Any]) -> str:
    return "```json\n" + json.dumps(payload, indent=2, sort_keys=True) + "\n```"


def render_proposal_note(proposal: TradeProposal) -> str:
    frontmatter = render_frontmatter(
        f"{proposal.proposal_id} proposal",
        {
            "type": "trade-proposal",
            "status": proposal.status,
            "ticker": proposal.ticker,
            "created_at": proposal.created_at,
        },
    )
    return "\n".join(
        [
            frontmatter,
            "",
            "# Trade Proposal",
            "",
            f"Buy `{proposal.ticker}` for `${proposal.position_size_usd:.2f}` using a `{proposal.order_type}` order at `${proposal.limit_price:.2f}`.",
            "",
            "## Thesis",
            "",
            proposal.thesis,
            "",
            "## Invalidation",
            "",
            proposal.invalidation,
            "",
            "## Guardrails",
            "",
            f"- Strategy tag: `{proposal.strategy_tag}`",
            f"- Time horizon: `{proposal.time_horizon}`",
            f"- Confidence: `{proposal.confidence}`",
            f"- Session: `{proposal.order_session}`",
            f"- Initial approval phrase: `{proposal.initial_approval_phrase()}`",
            f"- Final approval phrase: `{proposal.final_approval_phrase()}`",
            "",
            "## Proposal JSON",
            "",
            json_fence(asdict(proposal)),
        ]
    )


def render_risk_note(proposal: TradeProposal, record: dict[str, Any]) -> str:
    frontmatter = render_frontmatter(
        f"{proposal.proposal_id} risk check",
        {
            "type": "risk-check",
            "status": record["status"],
            "ticker": proposal.ticker,
            "ran_at": record["ran_at"],
        },
    )
    checks = "\n".join(
        f"- {'PASS' if check['passed'] else 'FAIL'} - `{check['name']}` - {check['detail']}" for check in record["checks"]
    )
    return "\n".join(
        [
            frontmatter,
            "",
            "# Risk Check",
            "",
            f"Verdict: `{record['status'].upper()}`",
            "",
            "## Key Metrics",
            "",
            f"- Account value: `${record['account_value_usd']:.2f}`",
            f"- Projected total exposure: `{record['projected_total_exposure_percent']:.2f}%`",
            f"- Projected `{proposal.ticker}` exposure: `{record['projected_ticker_exposure_percent']:.2f}%`",
            "",
            "## Checks",
            "",
            checks,
            "",
            "## Risk JSON",
            "",
            json_fence(record),
        ]
    )


def render_approval_note(proposal: TradeProposal, record: dict[str, Any]) -> str:
    frontmatter = render_frontmatter(
        f"{proposal.proposal_id} {record['stage']} approval",
        {
            "type": "trade-approval",
            "stage": record["stage"],
            "status": "valid" if record["is_valid"] else "invalid",
            "created_at": record["created_at"],
        },
    )
    return "\n".join(
        [
            frontmatter,
            "",
            "# Approval Record",
            "",
            f"- Proposal: `{proposal.proposal_id}`",
            f"- Stage: `{record['stage']}`",
            f"- Approver: `{record['approver']}`",
            f"- Valid: `{str(record['is_valid']).lower()}`",
            "",
            "## Typed Phrase",
            "",
            f"`{record['typed_phrase']}`",
            "",
            "## Expected Phrase",
            "",
            f"`{record['expected_phrase']}`",
            "",
            "## Approval JSON",
            "",
            json_fence(record),
        ]
    )


def render_review_note(proposal: TradeProposal, record: dict[str, Any]) -> str:
    frontmatter = render_frontmatter(
        f"{proposal.proposal_id} broker review",
        {
            "type": "broker-review",
            "status": record["status"],
            "reviewed_at": record["reviewed_at"],
        },
    )
    warning_lines = "\n".join(f"- {warning}" for warning in record["warnings"]) if record["warnings"] else "- none"
    return "\n".join(
        [
            frontmatter,
            "",
            "# Broker Review",
            "",
            f"- Broker mode: `{record['broker_mode']}`",
            f"- Status: `{record['status']}`",
            f"- Reference price: `${record['reference_price']:.2f}`",
            f"- Estimated quantity: `{record['estimated_quantity']}`",
            f"- Estimated notional: `${record['estimated_notional_usd']:.2f}`",
            f"- Limit delta: `{record['limit_delta_percent']:.2f}%`",
            "",
            "## Warnings",
            "",
            warning_lines,
            "",
            "## Review JSON",
            "",
            json_fence(record),
        ]
    )


def render_journal_note(proposal: TradeProposal, record: dict[str, Any]) -> str:
    frontmatter = render_frontmatter(
        f"{proposal.proposal_id} execution journal",
        {
            "type": "trade-journal",
            "status": record["status"],
            "executed_at": record["executed_at"],
        },
    )
    return "\n".join(
        [
            frontmatter,
            "",
            "# Execution Journal",
            "",
            f"- Proposal: `{proposal.proposal_id}`",
            f"- Ticker: `{proposal.ticker}`",
            f"- Order id: `{record['order_id']}`",
            f"- Status: `{record['status']}`",
            f"- Filled quantity: `{record['filled_quantity']}`",
            f"- Filled notional: `${record['filled_notional_usd']:.2f}`",
            f"- Limit price: `${record['limit_price']:.2f}`",
            f"- Buying power after fill: `${record['buying_power_after_fill_usd']:.2f}`",
            f"- Account value after fill: `${record['account_value_after_fill_usd']:.2f}`",
            "",
            "## Execution JSON",
            "",
            json_fence(record),
        ]
    )


def render_snapshot_note(snapshot: dict[str, Any]) -> str:
    frontmatter = render_frontmatter(
        "latest account status",
        {
            "type": "account-snapshot",
            "generated_at": snapshot["generated_at"],
            "account_id": snapshot["account_id"],
        },
    )
    position_lines = []
    for position in snapshot["positions"]:
        market_value = round(float(position["quantity"]) * float(position["last_price"]), 2)
        position_lines.append(
            f"- `{position['ticker']}` - qty `{position['quantity']}` - avg `${float(position['avg_price']):.2f}` "
            f"- last `${float(position['last_price']):.2f}` - value `${market_value:.2f}`"
        )
    if not position_lines:
        position_lines.append("- none")
    positions_text = "\n".join(position_lines)

    order_lines = []
    for order in snapshot["orders"][-5:]:
        order_lines.append(
            f"- `{order['order_id']}` - `{order['ticker']}` - `${float(order['notional_usd']):.2f}` - `{order['status']}`"
        )
    if not order_lines:
        order_lines.append("- none")
    orders_text = "\n".join(order_lines)

    return "\n".join(
        [
            frontmatter,
            "",
            "# Account Snapshot",
            "",
            f"- Account id: `{snapshot['account_id']}`",
            f"- Buying power: `${snapshot['buying_power_usd']:.2f}`",
            f"- Account value: `${snapshot['account_value_usd']:.2f}`",
            "",
            "## Positions",
            "",
            positions_text,
            "",
            "## Recent Orders",
            "",
            orders_text,
            "",
            "## Snapshot JSON",
            "",
            json_fence(snapshot),
        ]
    )


def command_init(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    if args.reset:
        reset_managed_state(paths)
    bootstrap_mock_state(paths)
    print(f"Initialized trading cockpit at {paths.app_dir}")
    return 0


def command_propose(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    policy = load_risk_policy(paths.policy_path)
    proposal = build_proposal(
        ticker=args.ticker,
        position_size_usd=args.usd,
        limit_price=args.limit,
        thesis=args.thesis,
        invalidation=args.invalidation,
        time_horizon=args.horizon,
        confidence=args.confidence,
        strategy_tag=args.strategy_tag,
        source_note=args.source_note,
        requires_initial_approval=policy.require_initial_approval,
        requires_final_approval=policy.require_final_approval,
    )
    _, note_path = save_proposal(paths, proposal)
    print(f"Created proposal {proposal.proposal_id}")
    print(note_path)
    return 0


def command_check(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    proposal = load_proposal(paths, args.proposal_id)
    policy = load_risk_policy(paths.policy_path)
    state = bootstrap_mock_state(paths)
    record = risk_check_record(proposal, policy, state)
    _, note_path = save_risk_check(paths, proposal, record)
    print(f"Risk check {record['status']} for {proposal.proposal_id}")
    print(note_path)
    return 0 if record["status"] == "pass" else 2


def command_approve(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    proposal = load_proposal(paths, args.proposal_id)
    record = create_approval_record(proposal, args.stage, args.phrase, args.approver)
    _, note_path = save_approval(paths, proposal, record)
    print(f"Approval {args.stage}: {'valid' if record['is_valid'] else 'invalid'}")
    print(note_path)
    return 0 if record["is_valid"] else 2


def command_review(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    proposal = load_proposal(paths, args.proposal_id)
    if not load_latest_passed_risk(paths, proposal.proposal_id):
        raise RuntimeError("proposal must pass risk checks before review")
    state = bootstrap_mock_state(paths)
    record = review_order(proposal, state)
    _, note_path = save_review(paths, proposal, record)
    print(f"Broker review {record['status']} for {proposal.proposal_id}")
    print(note_path)
    return 0


def command_execute(args: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    proposal = load_proposal(paths, args.proposal_id)
    record = execute_order(paths, proposal)
    snapshot, _, latest_note = write_account_snapshot(paths)
    print(f"Executed {proposal.proposal_id} as {record['order_id']}")
    print(f"Buying power after fill: ${snapshot['buying_power_usd']:.2f}")
    print(latest_note)
    return 0


def command_status(_: argparse.Namespace, paths: VaultPaths) -> int:
    ensure_structure(paths)
    snapshot, note_path, latest_note = write_account_snapshot(paths)
    print(f"Account value: ${snapshot['account_value_usd']:.2f}")
    print(f"Buying power: ${snapshot['buying_power_usd']:.2f}")
    print(note_path)
    print(latest_note)
    return 0


def command_demo(args: argparse.Namespace, paths: VaultPaths) -> int:
    result = run_demo(paths, reset=args.reset)
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Vault-native trading cockpit with a mock broker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create folders and seed the mock broker state")
    init_parser.add_argument("--reset", action="store_true", help="clear generated runtime and note outputs first")

    propose_parser = subparsers.add_parser("propose", help="create a structured trade proposal")
    propose_parser.add_argument("--ticker", required=True)
    propose_parser.add_argument("--usd", required=True, type=float)
    propose_parser.add_argument("--limit", required=True, type=float)
    propose_parser.add_argument("--thesis", required=True)
    propose_parser.add_argument("--invalidation", required=True)
    propose_parser.add_argument("--horizon", default="2-10 days")
    propose_parser.add_argument("--confidence", default="medium")
    propose_parser.add_argument("--strategy-tag", default="vault-test")
    propose_parser.add_argument("--source-note")

    check_parser = subparsers.add_parser("check", help="run deterministic risk checks for a proposal")
    check_parser.add_argument("--proposal-id", required=True)

    approve_parser = subparsers.add_parser("approve", help="save a typed approval phrase")
    approve_parser.add_argument("--proposal-id", required=True)
    approve_parser.add_argument("--stage", choices=["initial", "final"], required=True)
    approve_parser.add_argument("--phrase", required=True)
    approve_parser.add_argument("--approver", default="manual-user")

    review_parser = subparsers.add_parser("review", help="run a mock broker review for a proposal")
    review_parser.add_argument("--proposal-id", required=True)

    execute_parser = subparsers.add_parser("execute", help="place a mock order after approvals")
    execute_parser.add_argument("--proposal-id", required=True)

    subparsers.add_parser("status", help="write the latest account snapshot note")

    demo_parser = subparsers.add_parser("demo", help="run a full mock proposal-to-fill demo")
    demo_parser.add_argument("--reset", action="store_true", help="reset managed data before running the demo")

    return parser


def main(argv: list[str] | None = None, paths: VaultPaths | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    resolved_paths = paths or make_default_paths()

    handlers = {
        "init": command_init,
        "propose": command_propose,
        "check": command_check,
        "approve": command_approve,
        "review": command_review,
        "execute": command_execute,
        "status": command_status,
        "demo": command_demo,
    }

    try:
        return handlers[args.command](args, resolved_paths)
    except FileNotFoundError as error:
        print(f"Missing file: {error}", file=sys.stderr)
        return 1
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
