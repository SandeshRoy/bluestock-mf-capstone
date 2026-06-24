import pandas as pd
from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)

datasets = [
    ("01_fund_master.csv", None),
    ("03_aum_by_fund_house.csv", ["date"]),
    ("04_monthly_sip_inflows.csv", ["month"]),
    ("05_category_inflows.csv", ["month"]),
    ("06_industry_folio_count.csv", ["month"]),
    ("09_portfolio_holdings.csv", ["portfolio_date"]),
    ("10_benchmark_indices.csv", ["date"])
]

for filename, date_cols in datasets:

    file_path = f"data/raw/{filename}"

    df = pd.read_csv(file_path)

    print(f"\nProcessing {filename}")
    print("Original Shape:", df.shape)

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print("Duplicates Removed:", before - after)

    if date_cols:
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])

    output_name = filename.replace(
        ".csv",
        "_cleaned.csv"
    )

    output_path = f"data/processed/{output_name}"

    df.to_csv(
        output_path,
        index=False
    )

    print("Saved:", output_name)

print("\nAll remaining datasets cleaned successfully!")