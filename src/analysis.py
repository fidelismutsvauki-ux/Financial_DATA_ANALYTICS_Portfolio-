"""Exploratory analysis of the synthetic loan portfolio."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_loan_portfolio.csv"
OUT = ROOT / "outputs"

def main():
    df = pd.read_csv(DATA)
    df["disbursement_date"] = pd.to_datetime(df["disbursement_date"], errors="coerce")
    OUT.mkdir(exist_ok=True)

    checks = pd.DataFrame({
        "check": ["rows", "duplicate_loan_ids", "missing_cells",
                  "invalid_principal", "invalid_default_flags"],
        "result": [len(df), df["loan_id"].duplicated().sum(),
                   df.isna().sum().sum(), (df["principal_usd"] <= 0).sum(),
                   (~df["default_flag"].isin([0, 1])).sum()]
    })
    checks.to_csv(OUT/"data_quality_checks.csv", index=False)

    product = df.groupby("product").agg(
        loan_count=("loan_id", "count"),
        total_principal_usd=("principal_usd", "sum"),
        average_loan_usd=("principal_usd", "mean"),
        illustrative_default_rate=("default_flag", "mean")
    ).reset_index()
    product.to_csv(OUT/"summary_by_product.csv", index=False)

    branch = df.groupby("branch").agg(
        loan_count=("loan_id", "count"),
        total_principal_usd=("principal_usd", "sum"),
        illustrative_default_rate=("default_flag", "mean")
    ).reset_index()
    branch.to_csv(OUT/"summary_by_branch.csv", index=False)

    monthly = df.assign(month=df["disbursement_date"].dt.to_period("M").astype(str))
    monthly = monthly.groupby("month").agg(
        loan_count=("loan_id", "count"),
        total_principal_usd=("principal_usd", "sum")
    ).reset_index()
    monthly.to_csv(OUT/"monthly_disbursements.csv", index=False)

    p = product.sort_values("total_principal_usd")
    plt.figure(figsize=(9, 5))
    plt.barh(p["product"], p["total_principal_usd"])
    plt.title("Total Disbursed Principal by Loan Product")
    plt.xlabel("Principal (USD)")
    plt.tight_layout()
    plt.savefig(OUT/"principal_by_product.png", dpi=160)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["total_principal_usd"], marker="o")
    plt.title("Monthly Loan Disbursements")
    plt.xlabel("Month")
    plt.ylabel("Principal (USD)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUT/"monthly_disbursements.png", dpi=160)
    plt.close()

    print(f"Analysed {len(df)} synthetic loans.")
    print(checks.to_string(index=False))
    print(f"Outputs saved in {OUT}")

if __name__ == "__main__":
    main()
