---
title: Sunrise Bakery Capstone Answers - 2026-06-04
description: Completed finance case answer sheet with assumptions, valuation math, and recommendation
last_updated: 2026-06-04
---

# Sunrise Bakery Capstone Answers

This write-up uses the information in:

- `C:\Users\shiva\Downloads\Capstone Case.pdf`
- `C:\Users\shiva\Downloads\Exhibit 1.pdf`
- `C:\Users\shiva\Downloads\Exhibit 2.pdf`
- `C:\Users\shiva\Downloads\_d13412e6bd5d65c191103a0d3e241323_Spreadsheet-Template.xls`

## Key assumptions

- Cost of debt quoted in the case is the pre-tax borrowing rate: `4.50%`.
- WACC uses the after-tax cost of debt: `4.50% x (1 - 30%) = 3.15%`.
- Cost of equity uses CAPM: `3.0% + 0.80 x 5.5% = 7.40%`.
- Terminal value at year 6 includes both:
  - oven salvage value: `$140,000`
  - recovery of project working capital: `$14,175`
- Total terminal cash flow at year 6: `$154,175`.
- ROIC is the only material ambiguity in the template.
- Most likely template interpretation:
  - average forecasted net income / average net fixed assets for years 1 through 6
  - average net fixed assets = `(315,000 + 280,000 + 245,000 + 210,000 + 175,000 + 140,000) / 6 = 227,500`
  - ROIC = `67,200 / 227,500 = 29.54%`
- Conservative alternate interpretation:
  - include year 0 and year 6 net fixed assets in the average
  - average net fixed assets = `(350,000 + 140,000) / 2 = 245,000`
  - ROIC = `67,200 / 245,000 = 27.43%`

## Answers

1. Cost of debt: `4.50%` pre-tax.
   After-tax cost of debt used in WACC: `3.15%`.

2. Cost of equity:
   `3.0% + (0.80 x 5.5%) = 7.40%`

3. WACC:
   `0.75 x 7.40% + 0.25 x 4.50% x (1 - 30%) = 6.3375%`
   Rounded WACC: `6.34%`

4. Cost of capital to evaluate the oven purchase:
   `WACC = 6.34%`

5. Annual depreciation expense:
   `10% x 350,000 = 35,000`
   Annual depreciation: `$35,000` each year for years 1 through 6.

6. After-tax net income by year:

| Year | Net Income |
| --- | ---: |
| 1 | $56,000 |
| 2 | $61,600 |
| 3 | $67,200 |
| 4 | $72,800 |
| 5 | $72,800 |
| 6 | $72,800 |

7. Working capital and change in working capital:

Working capital = Other Current Assets - Current Liabilities

| Year | Working Capital | Change in WC |
| --- | ---: | ---: |
| 0 | $15,000 | $15,000 |
| 1 | $14,325 | -$675 |
| 2 | $14,275 | -$50 |
| 3 | $14,225 | -$50 |
| 4 | $14,175 | -$50 |
| 5 | $14,175 | $0 |
| 6 | $14,175 | $0 |

Note: the full `$14,175` of working capital is recovered separately in terminal value at year 6.

8. Terminal value at the end of year 6:

- Oven salvage value: `$140,000`
- Working capital recovery: `$14,175`
- Total terminal value: `$154,175`

9. Free cash flows:

FCF = Net Income + Depreciation - Change in WC - Capital Expenditures + Terminal Value

| Year | Free Cash Flow |
| --- | ---: |
| 0 | -$365,000 |
| 1 | $91,675 |
| 2 | $96,650 |
| 3 | $102,250 |
| 4 | $107,850 |
| 5 | $107,800 |
| 6 | $261,975 |

10. IRR:
    `21.94%`

11. NPV using WACC = `6.3375%`:
    `$236,545.58`

12. Payback period:

- Cumulative cash flow turns positive during year 4.
- Fractional payback:
  `3 + (74,425 / 107,850) = 3.69 years`

13. Return on invested capital:

- Average forecasted net income:
  `(56,000 + 61,600 + 67,200 + 72,800 + 72,800 + 72,800) / 6 = 67,200`
- Most likely template answer:
  average net fixed assets for years 1 through 6
  `= (315,000 + 280,000 + 245,000 + 210,000 + 175,000 + 140,000) / 6 = 227,500`
- ROIC:
  `67,200 / 227,500 = 29.54%`
- If your instructor includes year 0 in average invested capital instead, ROIC would be `27.43%`.

14. Recommendation:

Yes, Sunrise Bakery should purchase the new oven.

Why:

- NPV is strongly positive: `$236,545.58`
- IRR of `21.94%` is far above the `6.34%` WACC
- Payback is about `3.69 years`
- ROIC is attractive under either interpretation: `29.54%` or `27.43%`

## Short justification for question 4

The correct discount rate is the firm's `WACC`, not just the cost of equity, because the project appears to have similar operating risk to Sunrise's existing business and the purchase is not expected to change the firm's overall target capital structure.
