import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Duplicates Removed:", before - after)

# Forward fill missing NAV values within each fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Check invalid NAV values
invalid_nav = (df["nav"] <= 0).sum()

print("Invalid NAV Count:", invalid_nav)

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("File Saved: data/processed/nav_history_cleaned.csv")