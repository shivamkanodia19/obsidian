from __future__ import annotations

from pathlib import Path

import pandas as pd


INPUT_PATH = Path(r"C:\Users\shiva\Downloads\mlb_retail_sales_2yr.csv")
OUTPUT_DIR = Path(r"C:\Users\shiva\obsidian\05_Outputs\legends_global")
OUTPUT_CSV = OUTPUT_DIR / "mlb_retail_sales_2yr_cleaned.csv"
SUMMARY_TXT = OUTPUT_DIR / "mlb_retail_sales_2yr_cleaning_summary.txt"


ITEM_NAME_MAP = {
    "Cap": "Cap",
    "Foam Finger": "Foam Finger",
    "Hoodie": "Hoodie",
    "Jersey": "Jersey",
    "Jersy": "Jersey",
    "Keychain": "Keychain",
    "Keychain ": "Keychain",
    "Mug": "Mug",
    "T-shirt": "T-shirt",
}

ITEM_TYPE_MAP = {
    "Cap": "Headwear",
    "Foam Finger": "Novelty",
    "Hoodie": "Apparel",
    "Jersey": "Apparel",
    "Keychain": "Accessories",
    "Mug": "Drinkware",
    "T-shirt": "Apparel",
}


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_PATH)
    df["_source_row_number"] = range(1, len(df) + 1)

    source_rows = len(df)
    source_transaction_ids = df["transaction_id"].nunique()

    # Trim text fields so category and dimension values group consistently.
    object_columns = df.select_dtypes(include="object").columns
    for column in object_columns:
        df[column] = df[column].astype(str).str.strip()

    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="raise")

    removed_2022_rows = int((df["season"] == 2022).sum())
    df = df[df["season"] != 2022].copy()

    df["item_name"] = df["item_name"].map(ITEM_NAME_MAP).fillna(df["item_name"])
    df["item_type"] = df["item_name"].map(ITEM_TYPE_MAP).fillna("Other")

    duplicate_transaction_mask = df["transaction_id"].duplicated(keep=False)
    duplicate_transaction_count = int(duplicate_transaction_mask.sum())

    # Keep the earliest source row for deterministic deduping.
    df = df.sort_values(["transaction_id", "_source_row_number"]).drop_duplicates(subset=["transaction_id"], keep="first")
    rows_removed = source_rows - removed_2022_rows - len(df)

    df = df.sort_values(["season", "transaction_date", "transaction_id"]).reset_index(drop=True)

    # Standardize the timestamp format for easier import into BI tools.
    df["transaction_date"] = df["transaction_date"].dt.strftime("%Y-%m-%d %H:%M:%S")

    ordered_columns = [
        "transaction_id",
        "transaction_date",
        "season",
        "game_id",
        "store_id",
        "store_zone",
        "item_name",
        "item_type",
        "item_price",
        "quantity_sold",
        "total_sales",
        "payment_method",
        "weather_conditions",
    ]
    df = df[ordered_columns]

    df.to_csv(OUTPUT_CSV, index=False)

    summary_lines = [
        "Plain-English summary:",
        "This cleaned file keeps only the two assignment seasons: 2023 and 2024.",
        "Any row that originally had season = 2022 was removed rather than corrected.",
        "After removing those 2022 rows, duplicate transaction_id rows were removed by keeping one row per transaction_id.",
        "The final file was then standardized and sorted by season, transaction_date, and transaction_id.",
        "",
        f"Source rows: {source_rows}",
        f"Cleaned rows: {len(df)}",
        f"Original unique transaction IDs: {source_transaction_ids}",
        f"Rows removed because original season was 2022: {removed_2022_rows}",
        f"Rows removed due to duplicate transaction IDs: {rows_removed}",
        f"Rows involved in duplicate transaction ID collisions: {duplicate_transaction_count}",
        f"Cleaned unique transaction IDs: {df['transaction_id'].nunique()}",
        f"Row count check: {source_rows} source rows - {removed_2022_rows} removed 2022 rows - {rows_removed} removed duplicates = {len(df)} cleaned rows",
        "Why cleaned rows equal cleaned unique transaction IDs: after dropping the 2022 rows, transaction_id deduplication was the only remaining row-removal step.",
        "All other cleaning steps standardized values without dropping rows.",
        f"Seasons after cleaning: {', '.join(map(str, sorted(df['season'].unique())))}",
        "",
        "Transformations applied in order:",
        "1. Trimmed whitespace from text fields for consistent grouping.",
        "2. Parsed transaction_date and exported it in YYYY-MM-DD HH:MM:SS format.",
        f"3. Removed {removed_2022_rows} rows where the original season value was 2022 so the final dataset contains only the two assignment seasons.",
        "4. Standardized item_name values: Jersy -> Jersey and Keychain with trailing space -> Keychain.",
        "5. Added item_type based on item_name.",
        f"6. Removed {rows_removed} duplicate rows by keeping one row per transaction_id.",
        "7. Sorted the final CSV by season, transaction_date, and transaction_id for readability.",
        "",
        "Item type mapping:",
    ]
    summary_lines.extend(
        f"- {item_name}: {item_type}" for item_name, item_type in sorted(ITEM_TYPE_MAP.items(), key=lambda x: x[0])
    )
    SUMMARY_TXT.write_text("\n".join(summary_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
