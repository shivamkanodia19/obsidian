from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(r"C:\Users\shiva\obsidian")
SOURCE_CSV = ROOT / "01_Source" / "internships" / "legends_hospitality_merch_assessment" / "mlb_retail_sales_2yr.csv"
OUT_DIR = ROOT / "05_Outputs" / "research-analysis" / "legends-merch-assessment-2026-05-07"
ARTIFACTS_DIR = OUT_DIR / "artifacts"
CHARTS_DIR = OUT_DIR / "charts"


def clean_data() -> pd.DataFrame:
    df = pd.read_csv(SOURCE_CSV)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df["item_type"] = df["item_name"].str.strip().replace({"Jersy": "Jersey"})
    df["month_num"] = df["transaction_date"].dt.month
    df["month"] = df["transaction_date"].dt.strftime("%b")

    # The case prompt asks for two full seasons. The file also contains 276 malformed
    # rows with season=2022 but game_id values from 2023; exclude them from YoY.
    df = df[df["season"].isin([2023, 2024])].copy()
    return df


def overall_metrics(df: pd.DataFrame) -> pd.DataFrame:
    metrics = (
        df.groupby("season")
        .agg(
            revenue=("total_sales", "sum"),
            transactions=("transaction_id", "nunique"),
            units=("quantity_sold", "sum"),
            avg_line_sale=("total_sales", "mean"),
            avg_units_line=("quantity_sold", "mean"),
            avg_item_price=("item_price", "mean"),
            games=("game_id", "nunique"),
        )
        .reset_index()
    )
    metrics["revenue_per_game"] = metrics["revenue"] / metrics["games"]
    metrics["transactions_per_game"] = metrics["transactions"] / metrics["games"]
    metrics["units_per_transaction"] = metrics["units"] / metrics["transactions"]
    metrics["sales_per_transaction"] = metrics["revenue"] / metrics["transactions"]
    return metrics


def yoy_table(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    grouped = (
        df.groupby(["season", dimension])
        .agg(
            revenue=("total_sales", "sum"),
            units=("quantity_sold", "sum"),
            transactions=("transaction_id", "count"),
        )
        .reset_index()
    )
    pivot = grouped.pivot(index=dimension, columns="season")
    out = pd.DataFrame(
        {
            "2023 Revenue": pivot["revenue"][2023],
            "2024 Revenue": pivot["revenue"][2024],
            "2023 Units": pivot["units"][2023],
            "2024 Units": pivot["units"][2024],
            "2023 Transactions": pivot["transactions"][2023],
            "2024 Transactions": pivot["transactions"][2024],
        }
    ).reset_index()
    out["Revenue Growth $"] = out["2024 Revenue"] - out["2023 Revenue"]
    out["Revenue Growth %"] = out["2024 Revenue"] / out["2023 Revenue"] - 1
    out["Unit Growth %"] = out["2024 Units"] / out["2023 Units"] - 1
    out["2024 Share %"] = out["2024 Revenue"] / out["2024 Revenue"].sum()
    out["2023 Sales / Txn"] = out["2023 Revenue"] / out["2023 Transactions"]
    out["2024 Sales / Txn"] = out["2024 Revenue"] / out["2024 Transactions"]
    out["Sales / Txn Growth %"] = out["2024 Sales / Txn"] / out["2023 Sales / Txn"] - 1
    return out


def monthly_table(df: pd.DataFrame) -> pd.DataFrame:
    month_order = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
    grouped = (
        df.groupby(["season", "month_num", "month"])
        .agg(revenue=("total_sales", "sum"), transactions=("transaction_id", "count"))
        .reset_index()
    )
    grouped["month"] = pd.Categorical(grouped["month"], categories=month_order, ordered=True)
    grouped = grouped.sort_values(["month_num", "season"]).reset_index(drop=True)
    return grouped[["season", "month", "revenue", "transactions"]]


def zone_category_table(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["store_zone", "item_type", "season"])["total_sales"]
        .sum()
        .reset_index()
        .pivot_table(index=["store_zone", "item_type"], columns="season", values="total_sales", fill_value=0)
        .reset_index()
    )
    grouped["Growth $"] = grouped[2024] - grouped[2023]
    grouped["Growth %"] = grouped[2024] / grouped[2023] - 1
    grouped = grouped.rename(columns={2023: "2023 Revenue", 2024: "2024 Revenue"})
    return grouped.sort_values(["store_zone", "Growth $"], ascending=[True, False]).reset_index(drop=True)


def data_quality_notes(df: pd.DataFrame) -> dict:
    raw = pd.read_csv(SOURCE_CSV)
    season_counts = raw["season"].value_counts().sort_index().to_dict()
    item_values = sorted(raw["item_name"].unique().tolist())
    store_zone_counts = raw[raw["season"].isin([2023, 2024])].groupby("store_id")["store_zone"].nunique()
    return {
        "raw_row_count": int(len(raw)),
        "clean_row_count": int(len(df)),
        "season_counts_raw": {str(k): int(v) for k, v in season_counts.items()},
        "excluded_rows": int(len(raw) - len(df)),
        "excluded_reason": "Excluded malformed 2022 rows because the case asks for two full seasons and those rows use 2023 game IDs.",
        "item_name_standardization": {
            "strip_whitespace": True,
            "rename_map": {"Jersy": "Jersey"},
            "raw_item_values": item_values,
        },
        "store_id_stability_issue": {
            "stores_with_multiple_zones": int((store_zone_counts > 1).sum()),
            "note": "store_id is not stable across zones, so location analysis uses store_zone.",
        },
    }


def write_artifacts(df: pd.DataFrame) -> dict:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    overall = overall_metrics(df)
    category = yoy_table(df, "item_type").sort_values("Revenue Growth $", ascending=False).reset_index(drop=True)
    zone = yoy_table(df, "store_zone").sort_values("Revenue Growth $", ascending=False).reset_index(drop=True)
    monthly = monthly_table(df)
    zone_category = zone_category_table(df)
    quality = data_quality_notes(df)

    df.to_csv(ARTIFACTS_DIR / "cleaned_transactions.csv", index=False)
    overall.to_csv(ARTIFACTS_DIR / "overall_metrics.csv", index=False)
    category.to_csv(ARTIFACTS_DIR / "category_yoy.csv", index=False)
    zone.to_csv(ARTIFACTS_DIR / "zone_yoy.csv", index=False)
    monthly.to_csv(ARTIFACTS_DIR / "monthly_revenue.csv", index=False)
    zone_category.to_csv(ARTIFACTS_DIR / "zone_category_growth.csv", index=False)
    (ARTIFACTS_DIR / "data_quality.json").write_text(json.dumps(quality, indent=2), encoding="utf-8")

    insight_pack = {
        "overall_2023_revenue": float(overall.loc[overall["season"] == 2023, "revenue"].iloc[0]),
        "overall_2024_revenue": float(overall.loc[overall["season"] == 2024, "revenue"].iloc[0]),
        "overall_growth_pct": float(
            overall.loc[overall["season"] == 2024, "revenue"].iloc[0]
            / overall.loc[overall["season"] == 2023, "revenue"].iloc[0]
            - 1
        ),
        "top_category_growth": category.head(3).to_dict(orient="records"),
        "bottom_category_growth": category.tail(3).to_dict(orient="records"),
        "top_zone_growth": zone.head(2).to_dict(orient="records"),
        "bottom_zone_growth": zone.tail(3).to_dict(orient="records"),
        "best_zone_category_moves": zone_category.sort_values("Growth $", ascending=False).head(5).to_dict(orient="records"),
        "worst_zone_category_moves": zone_category.sort_values("Growth $").head(5).to_dict(orient="records"),
    }
    (ARTIFACTS_DIR / "insight_pack.json").write_text(json.dumps(insight_pack, indent=2), encoding="utf-8")
    return {
        "overall": overall,
        "category": category,
        "zone": zone,
        "monthly": monthly,
        "zone_category": zone_category,
    }


def style_axes(ax: plt.Axes) -> None:
    ax.set_facecolor("#FAFAF7")
    ax.grid(axis="x", color="#D8D4CC", linewidth=0.8, alpha=0.6)
    ax.grid(axis="y", visible=False)
    for spine in ax.spines.values():
        spine.set_visible(False)


def build_charts(tables: dict) -> None:
    sns.set_theme(style="whitegrid")
    palette = {
        "navy": "#143642",
        "gold": "#D8A225",
        "green": "#2D6A4F",
        "red": "#B23A48",
        "sand": "#EDE6D6",
        "slate": "#4F5D75",
    }

    monthly = tables["monthly"].copy()
    fig, ax = plt.subplots(figsize=(9, 4.8))
    for season, color in [(2023, palette["slate"]), (2024, palette["navy"])]:
        season_data = monthly[monthly["season"] == season]
        ax.plot(season_data["month"], season_data["revenue"], marker="o", linewidth=2.5, label=str(season), color=color)
    ax.set_title("Monthly Merchandise Revenue Trend", fontsize=14, weight="bold", color=palette["navy"])
    ax.set_xlabel("")
    ax.set_ylabel("Revenue ($)")
    ax.legend(frameon=False)
    ax.ticklabel_format(style="plain", axis="y")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "monthly_revenue_trend.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    category = tables["category"].copy().sort_values("2024 Revenue")
    fig, ax = plt.subplots(figsize=(9, 5.2))
    y = range(len(category))
    ax.barh([v - 0.18 for v in y], category["2023 Revenue"], height=0.34, color=palette["sand"], label="2023")
    ax.barh([v + 0.18 for v in y], category["2024 Revenue"], height=0.34, color=palette["gold"], label="2024")
    ax.set_yticks(list(y))
    ax.set_yticklabels(category["item_type"])
    ax.set_title("Revenue by Merchandise Category", fontsize=14, weight="bold", color=palette["navy"])
    ax.set_xlabel("Revenue ($)")
    ax.legend(frameon=False)
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "category_revenue_comparison.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    zone = tables["zone"].copy().sort_values("Revenue Growth $")
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    colors = [palette["green"] if v >= 0 else palette["red"] for v in zone["Revenue Growth $"]]
    ax.barh(zone["store_zone"], zone["Revenue Growth $"], color=colors)
    ax.axvline(0, color="#6B7280", linewidth=1)
    ax.set_title("Revenue Growth by Stadium Zone", fontsize=14, weight="bold", color=palette["navy"])
    ax.set_xlabel("2024 vs. 2023 Revenue Change ($)")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "zone_growth.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    zone_category = tables["zone_category"].copy()
    heatmap = zone_category.pivot(index="store_zone", columns="item_type", values="Growth $")
    heatmap = heatmap.loc[sorted(heatmap.index), sorted(heatmap.columns)]
    fig, ax = plt.subplots(figsize=(10, 4.8))
    sns.heatmap(
        heatmap,
        cmap=sns.diverging_palette(12, 145, as_cmap=True),
        center=0,
        linewidths=0.5,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Revenue Change ($)"},
        ax=ax,
    )
    ax.set_title("Zone-by-Category Growth Heatmap", fontsize=14, weight="bold", color=palette["navy"])
    ax.set_xlabel("")
    ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "zone_category_heatmap.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    df = clean_data()
    tables = write_artifacts(df)
    build_charts(tables)
    print(f"Artifacts written to: {OUT_DIR}")


if __name__ == "__main__":
    main()
