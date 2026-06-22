import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = data_path.glob("*.csv")

for file in csv_files:
    print("\n" + "=" * 50)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("=" * 50)

# Fund Master Exploration
print("\n" + "=" * 50)
print("FUND MASTER ANALYSIS")
print("=" * 50)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Grades:")
print(fund_master["risk_category"].unique())

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

missing_codes = (
    set(fund_master["amfi_code"])
    - set(nav_history["amfi_code"])
)

print("\nAMFI Code Validation")
if len(missing_codes) == 0:
    print("✅ All AMFI codes from fund_master exist in nav_history")
else:
    print("❌ Missing Codes:", missing_codes)