import pandas as pd
import sqlite3
from pathlib import Path

# Create database folder
Path("data/db").mkdir(parents=True, exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect("data/db/bluestock_mf.db")

print("Connected to SQLite Database")

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/scheme_performance_cleaned.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Create dim_fund
dim_fund = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "benchmark",
        "risk_category",
    ]
]

# Rename columns to match schema
nav = nav.rename(columns={"date": "nav_date"})

# Load tables
dim_fund.to_sql("dim_fund", conn, if_exists="replace", index=False)
nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)
performance.to_sql("fact_performance", conn, if_exists="replace", index=False)
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)

print("Tables Loaded Successfully")

# Verify row counts
tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as count FROM {table}",
        conn
    )
    print(f"{table}: {count['count'][0]} rows")

conn.close()

print("Database Created: data/db/bluestock_mf.db")