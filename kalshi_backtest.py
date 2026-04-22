#!/usr/bin/env python3
"""
Kalshi Austin High Temp Backtest
Compares NOAA forecast accuracy vs Kalshi market pricing
"""

import os
import json
import hashlib
import hmac
import base64
from datetime import datetime, timedelta
import urllib.request
import urllib.parse
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

# Load credentials from env vars
API_KEY_ID = os.getenv("KALSHI_API_KEY_ID")
PRIVATE_KEY_PEM = os.getenv("KALSHI_PRIVATE_KEY")

if not API_KEY_ID or not PRIVATE_KEY_PEM:
    print("ERROR: Set KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY env vars")
    exit(1)

# Parse private key
private_key = RSA.import_key(PRIVATE_KEY_PEM)

def sign_request(method, path, body=""):
    """Sign a Kalshi API request with RSA-PSS"""
    timestamp = str(int(datetime.now(datetime.timezone.utc).timestamp() * 1000))

    # Signature payload: timestamp + method + path
    message = f"{timestamp}{method}{path}"
    if body:
        message += body

    # Sign with RSA-PSS
    h = SHA256.new(message.encode())
    signature = pss.new(private_key).sign(h)
    signature_b64 = base64.b64encode(signature).decode()

    return {
        "KALSHI-ACCESS-KEY": API_KEY_ID,
        "KALSHI-ACCESS-TIMESTAMP": timestamp,
        "KALSHI-ACCESS-SIGNATURE": signature_b64,
        "Content-Type": "application/json"
    }

def fetch_kalshi_markets():
    """Fetch settled Austin high temp markets from 2024"""
    print("[1/4] Fetching Kalshi Austin high temp markets...")

    # First test if API is reachable (no auth needed for this endpoint)
    try:
        with urllib.request.urlopen("https://api.kalshi.com/trade-api/v2/events", timeout=5) as response:
            print("   ✓ Kalshi API reachable")
    except Exception as e:
        print(f"   ✗ Kalshi API unreachable: {e}")
        print("   (Check network/VPN or try again later)")
        return []

    url = "https://api.kalshi.com/trade-api/v2/markets?parent_market_ticker=AUXT"
    path = "/trade-api/v2/markets?parent_market_ticker=AUXT"
    headers = sign_request("GET", path)

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        # Filter to settled markets
        settled = [m for m in data.get('markets', []) if m.get('settled')]
        print(f"   Found {len(settled)} settled markets")
        return settled[:50]  # Limit to 50 for testing
    except Exception as e:
        print(f"   ERROR fetching markets: {e}")
        return []

def fetch_open_meteo_temps():
    """Fetch Austin observed high temps from Open-Meteo"""
    print("[2/4] Fetching Open-Meteo Austin temps...")

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 30.27,
        "longitude": -97.74,
        "start_date": "2024-01-01",
        "end_date": datetime.now().strftime("%Y-%m-%d"),
        "daily": "temperature_2m_max",
        "timezone": "America/Chicago"
    }

    try:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(full_url) as response:
            data = json.loads(response.read().decode())

        temps = {}
        for date_str, temp_c in zip(data['daily']['time'], data['daily']['temperature_2m_max']):
            temp_f = (temp_c * 9/5) + 32
            temps[date_str] = temp_f

        print(f"   Got {len(temps)} daily high temps")
        return temps
    except Exception as e:
        print(f"   ERROR: {e}")
        return {}

def parse_kalshi_contract(market):
    """Extract settlement date and threshold from market title"""
    # Example title: "Will the high temperature in Austin be above 85°F on April 15?"
    title = market.get('title', '')
    ticker = market.get('ticker', '')

    try:
        # Rough parsing
        if 'above' in title.lower() or '≥' in title or '>=' in title:
            # Extract number
            import re
            match = re.search(r'(\d+)°?F?', title)
            threshold = int(match.group(1)) if match else None

            # Settlement date is usually in ticker or title
            # Format: KXHIGHTPHX20260419 -> 2026-04-19
            match = re.search(r'(\d{8})', ticker)
            if match:
                date_str = match.group(1)
                settlement_date = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}"
                return {'threshold': threshold, 'date': settlement_date, 'title': title}
    except:
        pass

    return None

def calculate_metrics(markets, temps):
    """Compare forecasts to actual outcomes"""
    print("[3/4] Analyzing edge...")

    correct = 0
    total = 0
    gaps = []

    for market in markets:
        contract = parse_kalshi_contract(market)
        if not contract:
            continue

        date = contract['date']
        threshold = contract['threshold']

        if date not in temps or not threshold:
            continue

        actual_temp = temps[date]
        result = market.get('result')

        # Did market settle correctly?
        if result == 'YES':
            predicted_yes = True
        elif result == 'NO':
            predicted_yes = False
        else:
            continue

        actual_yes = actual_temp > threshold

        if predicted_yes == actual_yes:
            correct += 1

        total += 1

        # Calculate gap: how far off was the crowd?
        gap = abs(actual_temp - threshold)
        gaps.append(gap)

    if total == 0:
        print("   No data matched")
        return {}

    accuracy = correct / total
    avg_gap = sum(gaps) / len(gaps) if gaps else 0

    print(f"   Accuracy: {accuracy:.1%} ({correct}/{total} correct)")
    print(f"   Avg temp gap: {avg_gap:.1f}°F")

    return {
        'accuracy': accuracy,
        'sample_size': total,
        'avg_gap': avg_gap
    }

def main():
    print("=== Kalshi Austin High Temp Backtest ===\n")

    markets = fetch_kalshi_markets()
    temps = fetch_open_meteo_temps()

    if not markets or not temps:
        print("FAILED: Could not fetch data")
        return

    metrics = calculate_metrics(markets, temps)

    print("\n[4/4] Results:")
    if metrics:
        print(f"\nSample size: {metrics['sample_size']} contracts")
        print(f"Kalshi accuracy: {metrics['accuracy']:.1%}")
        print(f"Avg forecast error: {metrics['avg_gap']:.1f}°F")
        print("\n⚠️  This is a basic backtest. Full analysis needs:")
        print("   - Filtering by time-to-settlement (24-48h forecasts)")
        print("   - Kalshi price vs NOAA probability comparison")
        print("   - Fee impact analysis")
    else:
        print("No results")

if __name__ == "__main__":
    main()
