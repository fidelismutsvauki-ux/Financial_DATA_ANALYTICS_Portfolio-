# Financial Data Analytics Portfolio — Synthetic Loan Portfolio

**Author:** Fidelis Mutsvauki  
**Focus:** Python, SQL, data quality, exploratory analysis, portfolio reporting

## Project overview
This project demonstrates an end-to-end analysis of a small loan portfolio using a fully synthetic dataset. It explores disbursement patterns, product mix, branch performance and illustrative default rates.

> **Important:** Every record is simulated for demonstration. This is not customer data, employer data, or evidence of real lending decisions. The risk score and default flag are synthetic teaching variables.

## Questions explored
1. How is the portfolio distributed by loan product and branch?
2. What are the monthly disbursement volumes and principal amounts?
3. How do illustrative default rates vary by product and branch?
4. Are there missing values, duplicate loan IDs, or invalid numeric values?

## Repository structure
- `data/synthetic_loan_portfolio.csv` — 300 synthetic loan records.
- `src/analysis.py` — data validation, summary tables and visualisations.
- `sql/portfolio_queries.sql` — SQL examples for common portfolio questions.
- `requirements.txt` — Python dependencies.

## Run locally
```bash
python -m pip install -r requirements.txt
python src/analysis.py
```
The script writes summary CSV files and PNG charts to an `outputs/` directory.

## Methods
- Pandas data loading and validation
- Duplicate and missing-value checks
- Grouped summaries and monthly aggregation
- Default-rate calculation
- Matplotlib visualisation

## Interpretation notes
The simulated default rates are designed only to demonstrate analytical methods. They should not be used to infer actual credit risk, estimate loss rates, or support lending decisions.

## Skills demonstrated
Python • pandas • SQL • data cleaning • exploratory data analysis • financial reporting • visualisation
