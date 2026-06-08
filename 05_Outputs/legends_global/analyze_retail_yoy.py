from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(r"C:\Users\shiva\obsidian\05_Outputs\legends_global")
INPUT_CSV = BASE_DIR / "mlb_retail_sales_2yr_cleaned.csv"


def write_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(BASE_DIR / filename, index=False)


def main() -> None:
    df = pd.read_csv(INPUT_CSV, parse_dates=["transaction_date"])
    df["event_date"] = df["transaction_date"].dt.date
    df["month"] = df["transaction_date"].dt.month

    season = (
        df.groupby("season")
        .agg(
            sales=("total_sales", "sum"),
            transactions=("transaction_id", "size"),
            units=("quantity_sold", "sum"),
            avg_transaction=("total_sales", "mean"),
            avg_item_price=("item_price", "mean"),
            event_dates=("event_date", "nunique"),
        )
        .reset_index()
    )
    season["sales_per_event_date"] = season["sales"] / season["event_dates"]
    season["transactions_per_event_date"] = season["transactions"] / season["event_dates"]
    season["units_per_event_date"] = season["units"] / season["event_dates"]
    season["units_per_transaction"] = season["units"] / season["transactions"]
    season["sales_per_unit"] = season["sales"] / season["units"]
    write_csv(season.round(4), "season_summary.csv")

    total_change = float(season.loc[season["season"] == 2024, "sales"].iloc[0] - season.loc[season["season"] == 2023, "sales"].iloc[0])

    for dim, filename in [
        ("item_type", "item_type_yoy.csv"),
        ("item_name", "item_name_yoy.csv"),
        ("store_zone", "store_zone_yoy.csv"),
        ("payment_method", "payment_method_yoy.csv"),
        ("weather_conditions", "weather_conditions_yoy.csv"),
    ]:
        summary = (
            df.groupby(["season", dim])
            .agg(
                sales=("total_sales", "sum"),
                transactions=("transaction_id", "size"),
                units=("quantity_sold", "sum"),
                avg_transaction=("total_sales", "mean"),
                avg_item_price=("item_price", "mean"),
            )
            .reset_index()
        )
        pivot = summary.pivot(index=dim, columns="season")
        pivot.columns = [f"{metric}_{season}" for metric, season in pivot.columns]
        pivot = pivot.reset_index()
        pivot["sales_change"] = pivot["sales_2024"] - pivot["sales_2023"]
        pivot["sales_change_pct"] = pivot["sales_change"] / pivot["sales_2023"]
        pivot["transactions_change"] = pivot["transactions_2024"] - pivot["transactions_2023"]
        pivot["units_change"] = pivot["units_2024"] - pivot["units_2023"]
        pivot["share_of_total_change_pct"] = pivot["sales_change"] / total_change * 100
        write_csv(pivot.round(4).sort_values("sales_change", ascending=False), filename)

    monthly = (
        df.groupby(["season", "month"])
        .agg(
            sales=("total_sales", "sum"),
            transactions=("transaction_id", "size"),
            units=("quantity_sold", "sum"),
            event_dates=("event_date", "nunique"),
        )
        .reset_index()
    )
    monthly["sales_per_event_date"] = monthly["sales"] / monthly["event_dates"]
    monthly["transactions_per_event_date"] = monthly["transactions"] / monthly["event_dates"]
    monthly["avg_transaction"] = monthly["sales"] / monthly["transactions"]
    monthly_pivot = monthly.pivot(index="month", columns="season")
    monthly_pivot.columns = [f"{metric}_{season}" for metric, season in monthly_pivot.columns]
    monthly_pivot = monthly_pivot.reset_index()
    monthly_pivot["sales_per_event_date_change"] = (
        monthly_pivot["sales_per_event_date_2024"] - monthly_pivot["sales_per_event_date_2023"]
    )
    monthly_pivot["sales_per_event_date_pct"] = (
        monthly_pivot["sales_per_event_date_change"] / monthly_pivot["sales_per_event_date_2023"]
    )
    write_csv(monthly_pivot.round(4), "monthly_event_date_yoy.csv")

    zone_item = (
        df.groupby(["season", "store_zone", "item_type"])
        .agg(sales=("total_sales", "sum"))
        .reset_index()
    )
    zone_item_pivot = zone_item.pivot(index=["store_zone", "item_type"], columns="season", values="sales").reset_index()
    zone_item_pivot["sales_change"] = zone_item_pivot[2024] - zone_item_pivot[2023]
    zone_item_pivot["sales_change_pct"] = zone_item_pivot["sales_change"] / zone_item_pivot[2023]
    zone_item_pivot = zone_item_pivot.rename(columns={2023: "sales_2023", 2024: "sales_2024"})
    write_csv(zone_item_pivot.round(4).sort_values("sales_change", ascending=False), "zone_item_type_yoy.csv")

    caveats = [
        "Analysis caveats:",
        "- store_zone is the preferred location dimension for submission-ready analysis.",
        "- store_id appears in all five store zones, so it does not behave like a fixed physical location identifier.",
        "- transaction calendar date is the preferred event-level time grain.",
        "- game_id appears across many dates within a season and should not be treated as a unique event key for date-based analysis.",
        "- transaction hours are concentrated between 00:00 and 03:00, so time-of-day analysis is likely synthetic and not submission-ready.",
    ]
    (BASE_DIR / "analysis_caveats.txt").write_text("\n".join(caveats), encoding="utf-8")


if __name__ == "__main__":
    main()
