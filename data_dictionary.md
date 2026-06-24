# Data Dictionary

## dim_fund

| Column        | Data Type | Description                        |
| ------------- | --------- | ---------------------------------- |
| amfi_code     | INTEGER   | Unique AMFI scheme code            |
| scheme_name   | TEXT      | Name of mutual fund scheme         |
| fund_house    | TEXT      | Asset Management Company (AMC)     |
| category      | TEXT      | Fund category (Equity, Debt, etc.) |
| sub_category  | TEXT      | Specific fund type                 |
| plan          | TEXT      | Direct or Regular plan             |
| benchmark     | TEXT      | Benchmark index                    |
| risk_category | TEXT      | Risk classification                |

## fact_nav

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | INTEGER   | AMFI scheme code |
| nav_date  | DATE      | NAV date         |
| nav       | REAL      | Net Asset Value  |

## fact_transactions

| Column             | Data Type | Description              |
| ------------------ | --------- | ------------------------ |
| investor_id        | TEXT      | Unique investor ID       |
| transaction_date   | DATE      | Transaction date         |
| amfi_code          | INTEGER   | Fund code                |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption |
| amount_inr         | REAL      | Transaction amount       |
| state              | TEXT      | Investor state           |
| city               | TEXT      | Investor city            |
| city_tier          | TEXT      | Tier classification      |
| age_group          | TEXT      | Investor age group       |
| gender             | TEXT      | Investor gender          |
| annual_income_lakh | REAL      | Annual income in lakhs   |
| payment_mode       | TEXT      | Payment method           |
| kyc_status         | TEXT      | Verified or Pending      |

## fact_performance

| Column            | Data Type | Description                 |
| ----------------- | --------- | --------------------------- |
| amfi_code         | INTEGER   | Fund code                   |
| return_1yr_pct    | REAL      | 1-Year Return (%)           |
| return_3yr_pct    | REAL      | 3-Year Return (%)           |
| return_5yr_pct    | REAL      | 5-Year Return (%)           |
| alpha             | REAL      | Alpha metric                |
| beta              | REAL      | Beta metric                 |
| sharpe_ratio      | REAL      | Risk-adjusted return        |
| sortino_ratio     | REAL      | Downside-risk return metric |
| expense_ratio_pct | REAL      | Fund expense ratio          |

## fact_aum

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| fund_house     | TEXT      | AMC name          |
| date           | DATE      | Reporting date    |
| aum_lakh_crore | REAL      | AUM in lakh crore |
| aum_crore      | REAL      | AUM in crore      |
| num_schemes    | INTEGER   | Number of schemes |


# Source References

| Dataset                      | Source                                                                |
| ---------------------------- | --------------------------------------------------------------------- |
| 01_fund_master.csv           | Bluestock Capstone Dataset (derived from AMFI India mutual fund data) |
| 02_nav_history.csv           | AMFI India / mfapi.in NAV historical data                             |
| 03_aum_by_fund_house.csv     | AMFI Industry AUM reports                                             |
| 04_monthly_sip_inflows.csv   | AMFI Monthly SIP Reports                                              |
| 05_category_inflows.csv      | AMFI Category-wise Fund Flow Reports                                  |
| 06_industry_folio_count.csv  | AMFI Folio Statistics                                                 |
| 07_scheme_performance.csv    | Mutual Fund Performance Dataset                                       |
| 08_investor_transactions.csv | Simulated Investor Transaction Dataset (Capstone Project)             |
| 09_portfolio_holdings.csv    | Mutual Fund Portfolio Disclosure Data                                 |
| 10_benchmark_indices.csv     | NSE/BSE Benchmark Index Data                                          |

## Database

Database: SQLite

File: bluestock_mf.db

Tables:

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* fact_aum
