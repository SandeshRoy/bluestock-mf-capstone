-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by fund
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transaction count by state
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Total investment by state
SELECT state,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense ratio below 1%
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 funds by Sharpe Ratio
SELECT amfi_code,
       sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 7. Average return by risk grade
SELECT risk_grade,
       AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY risk_grade;

-- 8. Total AUM by fund house
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 9. Transaction type distribution
SELECT transaction_type,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Top 5 funds by 3-Year Return
SELECT amfi_code,
       return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;