---
title: latest account status
type: account-snapshot
generated_at: 2026-06-07T16:19:34-05:00
account_id: mock-agentic-001
---

# Account Snapshot

- Account id: `mock-agentic-001`
- Buying power: `$400.00`
- Account value: `$497.08`

## Positions

- `QQQM` - qty `0.25` - avg `$186.00` - last `$188.10` - value `$47.02`
- `IBIT` - qty `1.190476` - avg `$42.00` - last `$42.05` - value `$50.06`

## Recent Orders

- `MOCK-20260607T161933-IBIT` - `IBIT` - `$50.00` - `filled`

## Snapshot JSON

```json
{
  "account_id": "mock-agentic-001",
  "account_value_usd": 497.08,
  "buying_power_usd": 400.0,
  "generated_at": "2026-06-07T16:19:34-05:00",
  "orders": [
    {
      "filled_at": "2026-06-07T16:19:33-05:00",
      "limit_price": 42.0,
      "notional_usd": 50.0,
      "order_id": "MOCK-20260607T161933-IBIT",
      "quantity": 1.190476,
      "status": "filled",
      "ticker": "IBIT"
    }
  ],
  "positions": [
    {
      "avg_price": 186.0,
      "last_price": 188.1,
      "quantity": 0.25,
      "ticker": "QQQM"
    },
    {
      "avg_price": 42.0,
      "last_price": 42.05,
      "quantity": 1.190476,
      "ticker": "IBIT"
    }
  ]
}
```
