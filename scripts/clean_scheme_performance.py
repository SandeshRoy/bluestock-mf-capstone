import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Check for duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Duplicates Removed:", before - after)

# Numeric columns to validate
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Missing values check
print("\nMissing Values:")
print(df[numeric_cols].isnull().sum())

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1)
    | (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

# Save cleaned dataset
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print(
    "File Saved: data/processed/scheme_performance_cleaned.csv"
)