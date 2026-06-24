import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Duplicates Removed:", before - after)

# Validate amount > 0
invalid_amounts = (df["amount_inr"] <= 0).sum()
print("Invalid Amount Count:", invalid_amounts)

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print(
    "File Saved: data/processed/investor_transactions_cleaned.csv"
)