-- Synthetic loan portfolio analysis queries
-- Assumed table name: loan_portfolio. Data is simulated only.

-- 1. Overall portfolio
SELECT COUNT(*) AS loan_count,
       ROUND(SUM(principal_usd), 2) AS total_principal_usd,
       ROUND(AVG(principal_usd), 2) AS average_loan_usd
FROM loan_portfolio;

-- 2. Product mix
SELECT product, COUNT(*) AS loan_count,
       ROUND(SUM(principal_usd), 2) AS total_principal_usd
FROM loan_portfolio
GROUP BY product
ORDER BY total_principal_usd DESC;

-- 3. Branch performance
SELECT branch, COUNT(*) AS loan_count,
       ROUND(SUM(principal_usd), 2) AS total_principal_usd
FROM loan_portfolio
GROUP BY branch
ORDER BY total_principal_usd DESC;

-- 4. Illustrative default rate by product
SELECT product, COUNT(*) AS loan_count,
       ROUND(100.0 * AVG(default_flag), 2) AS illustrative_default_rate_pct
FROM loan_portfolio
GROUP BY product
ORDER BY illustrative_default_rate_pct DESC;

-- 5. Monthly disbursements (date stored as YYYY-MM-DD)
SELECT SUBSTR(disbursement_date, 1, 7) AS month,
       COUNT(*) AS loan_count,
       ROUND(SUM(principal_usd), 2) AS total_principal_usd
FROM loan_portfolio
GROUP BY SUBSTR(disbursement_date, 1, 7)
ORDER BY month;

-- 6. Duplicate loan IDs
SELECT loan_id, COUNT(*) AS occurrences
FROM loan_portfolio
GROUP BY loan_id
HAVING COUNT(*) > 1;

-- All risk scores and default flags are fictional teaching variables.
