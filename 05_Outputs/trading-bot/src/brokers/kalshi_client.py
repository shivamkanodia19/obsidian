"""
Kalshi API client wrapper.

Authentication: RSA key-based (KALSHI-ACCESS-KEY + KALSHI-ACCESS-SIGNATURE).
- Public endpoints (GET /markets, GET /markets/{ticker}): no auth required
- Authenticated endpoints (POST /portfolio/orders, GET /portfolio): require key + signature

To use authenticated endpoints:
  KALSHI_API_KEY_ID=your-key-id
  KALSHI_PRIVATE_KEY_PATH=/path/to/private_key.pem
  KALSHI_ENVIRONMENT=production  (or demo)
  KALSHI_BASE_URL=https://trading-api.kalshi.com/trade-api/v2  (production)
              or  https://demo-api.kalshi.co/trade-api/v2  (demo)
"""

from __future__ import annotations

import base64
import time
from pathlib import Path
from typing import Any

import httpx

from ..agents.schemas import KalshiMarketScan, OrderTicket, OrderSide
from ..config import get_settings
from ..utils.logging import get_logger
from .broker_interfaces import BrokerInterface

logger = get_logger(__name__)


def _load_private_key(path: str):
    """Load RSA private key from PEM file. Returns None if path empty."""
    if not path:
        return None
    try:
        from cryptography.hazmat.primitives.serialization import load_pem_private_key
        key_bytes = Path(path).read_bytes()
        return load_pem_private_key(key_bytes, password=None)
    except Exception as e:
        logger.error(f"Failed to load Kalshi private key from {path}: {e}")
        return None


def _sign_request(private_key, timestamp_ms: int, method: str, path: str) -> str:
    """
    Kalshi signature: base64(RSA-PSS-SHA256(timestamp_ms + method.upper() + path))
    path should not include query params.
    """
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding

    message = f"{timestamp_ms}{method.upper()}{path}".encode()
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH),
        hashes.SHA256(),
    )
    return base64.b64encode(signature).decode()


class KalshiClient(BrokerInterface):

    def __init__(self) -> None:
        self._settings = get_settings()
        self._base_url = self._settings.kalshi_base_url
        self._env = self._settings.kalshi_environment
        self._key_id = self._settings.kalshi_api_key_id
        self._private_key = _load_private_key(self._settings.kalshi_private_key_path)

    def _is_authenticated(self) -> bool:
        return bool(self._key_id and self._private_key)

    def _auth_headers(self, method: str, path: str) -> dict[str, str]:
        """Build Kalshi RSA auth headers for a request.

        Kalshi signs the full URL path including the /trade-api/v2 prefix,
        not just the endpoint path. Extract the path component from base_url
        and prepend it to the endpoint path before signing.
        """
        if not self._is_authenticated():
            raise RuntimeError(
                "Kalshi authentication not configured. "
                "Set KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH."
            )
        # base_url is e.g. https://api.elections.kalshi.com/trade-api/v2
        # full signing path must be /trade-api/v2/portfolio/balance
        from urllib.parse import urlparse
        base_path = urlparse(self._base_url).path.rstrip("/")
        full_path = base_path + path
        ts = int(time.time() * 1000)
        sig = _sign_request(self._private_key, ts, method, full_path)
        return {
            "KALSHI-ACCESS-KEY": self._key_id,
            "KALSHI-ACCESS-TIMESTAMP": str(ts),
            "KALSHI-ACCESS-SIGNATURE": sig,
            "Content-Type": "application/json",
        }

    def get_name(self) -> str:
        return f"kalshi_{self._env}"

    def is_live(self) -> bool:
        return self._env == "production"

    def get_quote(self, asset_or_market: str) -> dict[str, Any]:
        """
        Fetch public market data for a Kalshi ticker.
        No authentication required for public market endpoints.
        """
        try:
            url = f"{self._base_url}/markets/{asset_or_market}"
            with httpx.Client(timeout=10.0) as client:
                resp = client.get(url)
                resp.raise_for_status()
                data = resp.json()
                market = data.get("market", data)
                return {
                    "bid": market.get("yes_bid", None),
                    "ask": market.get("yes_ask", None),
                    "last": market.get("last_price", None),
                    "volume": market.get("volume", None),
                    "open_interest": market.get("open_interest", None),
                    "close_time": market.get("close_time", None),
                    "status": market.get("status", None),
                    "raw": market,
                }
        except httpx.HTTPError as e:
            logger.error(f"Kalshi API error for {asset_or_market}: {e}")
            return {"error": str(e), "bid": None, "ask": None, "last": None, "volume": None}

    def get_markets(self, series_ticker: str | None = None, limit: int = 50) -> list[KalshiMarketScan]:
        """
        Fetch list of active markets, optionally filtered by series.
        Public endpoint — no auth required.
        """
        try:
            params: dict[str, Any] = {"limit": limit, "status": "open"}
            if series_ticker:
                params["series_ticker"] = series_ticker

            with httpx.Client(timeout=15.0) as client:
                resp = client.get(f"{self._base_url}/markets", params=params)
                resp.raise_for_status()
                markets_data = resp.json().get("markets", [])

            results = []
            for m in markets_data:
                results.append(KalshiMarketScan(
                    ticker=m.get("ticker", ""),
                    title=m.get("title", ""),
                    yes_price=m.get("yes_bid"),
                    no_price=m.get("no_bid"),
                    volume=m.get("volume"),
                    open_interest=m.get("open_interest"),
                    notes=m.get("subtitle", ""),
                ))
            return results
        except httpx.HTTPError as e:
            logger.error(f"Kalshi market scan error: {e}")
            return []

    def get_balance(self) -> dict[str, Any]:
        """
        Fetch account balance. Requires auth.
        Returns: {'balance': int, 'payout': int} — Kalshi uses cents.
        """
        path = "/portfolio/balance"
        headers = self._auth_headers("GET", path)
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(f"{self._base_url}{path}", headers=headers)
            resp.raise_for_status()
            return resp.json()

    def get_positions(self) -> list[dict[str, Any]]:
        """
        Fetch open positions. Requires auth.
        Returns list of position dicts from Kalshi.
        """
        path = "/portfolio/positions"
        headers = self._auth_headers("GET", path)
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(f"{self._base_url}{path}", headers=headers)
            resp.raise_for_status()
            return resp.json().get("market_positions", [])

    def submit_order(self, ticket: OrderTicket) -> dict[str, Any]:
        """
        Submit an authenticated order to Kalshi.

        Requires:
        - KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH set in env
        - ticket.asset_type == PREDICTION_MARKET
        - ticket.side must be YES or NO (Kalshi convention)
        - allow_live_trading=true in settings

        The order is LIMIT by default (Kalshi supports limit and market).
        All prices in cents (Kalshi convention: 1-99 cents for yes contracts).
        """
        settings = get_settings()
        if not settings.allow_live_trading:
            raise RuntimeError(
                "Live trading is disabled. Set ALLOW_LIVE_TRADING=true to enable. "
                "This requires manual configuration change — not settable via API."
            )

        if not self._is_authenticated():
            raise RuntimeError(
                "Kalshi credentials not configured. "
                "Set KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH."
            )

        # Validate side is Kalshi-compatible
        if ticket.side not in (OrderSide.YES, OrderSide.NO):
            raise ValueError(
                f"Kalshi orders require side=YES or side=NO. Got: {ticket.side}. "
                "Equity-style BUY/SELL is not valid for prediction markets."
            )

        path = "/portfolio/orders"
        headers = self._auth_headers("POST", path)

        # Kalshi price is in cents (integer 1-99)
        try:
            price_cents = int(float(ticket.limit_price) * 100) if ticket.limit_price else None
        except (TypeError, ValueError):
            raise ValueError(f"Cannot parse limit_price '{ticket.limit_price}' as a decimal probability.")

        payload = {
            "ticker": ticket.asset_or_market,
            "action": "buy",
            "side": ticket.side.value,               # "yes" or "no"
            "type": ticket.order_type.value,         # "limit" or "market"
            "count": ticket.quantity,
            "client_order_id": ticket.id,
        }
        if price_cents is not None:
            if ticket.side == OrderSide.YES:
                payload["yes_price"] = price_cents
            else:
                payload["no_price"] = price_cents

        logger.info(f"Submitting Kalshi order: {payload}")

        with httpx.Client(timeout=15.0) as client:
            resp = client.post(
                f"{self._base_url}{path}",
                headers=headers,
                json=payload,
            )
            resp.raise_for_status()
            result = resp.json()

        logger.info(f"Kalshi order accepted: {result.get('order', {}).get('order_id', 'unknown')}")
        return result
