from pathlib import Path
import pandas as pd

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

risk_file = BASE_DIR / "reports" / "var_cvar_report.csv"
performance_file = BASE_DIR / "data" / "processed" / "scheme_performance_cleaned.csv"

# ======================================================
# Load datasets
# ======================================================

risk = pd.read_csv(risk_file)
performance = pd.read_csv(performance_file)

# ======================================================
# Rename column if needed
# ======================================================

if "return_3yr_pct" in performance.columns:
    performance.rename(columns={"return_3yr_pct": "return_pct"}, inplace=True)

# ======================================================
# Merge datasets
# ======================================================

recommend = pd.merge(
    performance,
    risk,
    on="amfi_code",
    how="inner"
)

# ======================================================
# Risk Category
# ======================================================

def risk_grade(var95):
    if var95 > -0.01:
        return "Low"
    elif var95 > -0.02:
        return "Moderate"
    else:
        return "High"

recommend["risk_grade"] = recommend["VaR_95"].apply(risk_grade)

# ======================================================
# Sort by Return
# ======================================================

recommend = recommend.sort_values(
    "return_pct",
    ascending=False
)

# ======================================================
# Display Top 3 Funds for Each Risk Grade
# ======================================================

print("\n========== FUND RECOMMENDATIONS ==========\n")

for grade in ["Low", "Moderate", "High"]:
    print(f"\n{grade.upper()} RISK\n")

    cols = [
        "scheme_name",
        "return_pct",
        "VaR_95",
        "CVaR_95"
    ]

    print(
        recommend[recommend["risk_grade"] == grade][cols]
        .head(3)
        .to_string(index=False)
    )

# ======================================================
# Save Recommendation Report
# ======================================================

output_file = BASE_DIR / "reports" / "fund_recommendations.csv"

recommend.to_csv(output_file, index=False)

print("\nSaved Successfully:")
print(output_file)