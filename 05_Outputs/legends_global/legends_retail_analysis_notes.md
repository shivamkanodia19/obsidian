# Legends Global Retail Analysis Notes

## Scope
- Dataset used: `mlb_retail_sales_2yr_cleaned.csv`
- Seasons analyzed: `2023` and `2024`
- Revenue field used as provided: `total_sales`

## Important Data Caveats
- Use `store_zone` for location analysis in the final submission.
- Do not use `store_id` as the primary location field in the final story. Each `store_id` appears in all five `store_zone` values, so it does not behave like a fixed physical location.
- Use transaction calendar date as the event-level time grain if you need per-game style analysis.
- Do not use `game_id` for time-based event analysis. Each `game_id` appears across many dates in the same season.
- Avoid time-of-day analysis. Transaction hours are concentrated between `00:00` and `03:00`, which suggests synthetic timestamps.

## Top-Line Performance
- 2024 sales were `$2,740,585.90` versus `$2,722,361.35` in 2023.
- Year-over-year sales growth was `$18,224.55`, or `+0.67%`.
- Transactions increased from `24,398` to `24,677` (`+279`, `+1.14%`).
- Units sold increased from `60,903` to `61,327` (`+424`, `+0.70%`).
- Average transaction value declined from `$111.58` to `$111.06` (`-$0.52`, `-0.47%`).
- Growth was driven by slightly more transactions, not by bigger baskets.

## Category Insights
- `Apparel` remained the core business, representing about `74%` of total sales in both years.
- Apparel grew by `$19,688.75`, which was more than `100%` of total net revenue growth because declines in other categories offset part of the gain.
- `Drinkware` was the second-best growth category, up `$4,126.74` (`+2.36%`).
- `Headwear` was the biggest drag, down `$6,133.80` (`-1.98%`).
- At the item level, the strongest contributors were:
  - `T-shirt`: `+$11,859.76` (`+3.49%` sales growth)
  - `Jersey`: `+$10,077.27`
  - `Mug`: `+$4,126.74`
- The weakest item was `Cap`, down `$6,133.80`.
- `Hoodie` was slightly down in revenue (`-$2,248.28`) despite staying a large category, which suggests stable demand but weaker monetization or mix.

## Location Insights
- `Lower Concourse` was the clear growth engine:
  - 2023 sales: `$533,723.30`
  - 2024 sales: `$556,574.27`
  - Change: `+$22,850.97` (`+4.28%`)
- Lower Concourse contributed about `125%` of total net revenue growth, meaning it more than offset declines elsewhere.
- `Main Concourse` also grew, but modestly: `+$7,574.41` (`+1.37%`).
- Three zones declined year over year:
  - `Club Level`: `-$6,003.20`
  - `Outfield`: `-$3,467.71`
  - `Upper Deck`: `-$2,729.92`
- The biggest zone-level driver was `Lower Concourse Apparel`, which grew by `$25,514.22`.
- The biggest zone-level drag was `Club Level Headwear`, which fell by `$5,239.18`.

## Seasonal / Timing Insights
- Using event date as the game proxy, 2024 outperformed 2023 on revenue per event date in:
  - `April` (`+4%`)
  - `May` (`+3%`)
  - `June` (`+5%`)
  - `September` (`+7%`)
- 2024 underperformed in:
  - `July` (`-6%`)
  - `August` (`-5%`)
  - `October` (`-3%`)
- The strongest monthly swing was `September Apparel`, which increased by `$29,733.52`.
- The weakest monthly swing was `July Apparel`, which declined by `$25,707.00`.
- This suggests the merchandising program was stronger early and late in the season, but softer during the mid-season peak months.

## Submission-Ready Findings
1. Overall YoY growth was positive but modest, so the story is not "retail transformation succeeded everywhere." The stronger story is that growth was narrow and concentrated.
2. Apparel is the franchise's clear strength and should anchor the SWOT `Strengths` section.
3. Lower Concourse is the strongest location opportunity because it was the only zone that materially expanded the business.
4. Headwear is the clearest underperforming category and should appear in both `Weaknesses` and `Threats`.
5. Mid-season softness in July and August suggests an opportunity for seasonal promotions, inventory rebalancing, or refreshed assortments during the heart of the season.

## Recommended Story Angle
- Use `store_zone`, not `store_id`, in the final visuals.
- Use an answer-first executive summary:
  - overall growth was small
  - growth was carried by apparel and Lower Concourse
  - several zones declined despite overall revenue being up
  - next season should focus on replicating Lower Concourse wins, lifting headwear, and addressing mid-season softness
