import pandas as pd

from dataguardian.checks.missing import check_missing
from dataguardian.checks.duplicates import check_duplicates
from dataguardian.checks.basic import analyze_columns
from dataguardian.checks.imbalance import check_imbalance
from dataguardian.checks.correlation import check_correlation
from dataguardian.checks.leakage import check_leakage
from dataguardian.checks.outliers import detect_outliers
from dataguardian.insights.warnings import generate_warnings
from dataguardian.core.scoring import calculate_score
from dataguardian.visualization.plots import plot_all


def diagnose(df, target=None, report=False, visualize=False):
    """
    Run full data diagnosis
    """
    print("\n" + "="*50)
    print("🔍 DataGuardian Report")
    print("="*50)

    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}\n")

    analyze_columns(df, target)

    check_missing(df)
    check_duplicates(df)

    check_imbalance(df, target)

    check_correlation(df)
    check_leakage(df, target)

    detect_outliers(df, target)

    warnings = generate_warnings(df)

    # Score
    score, issues = calculate_score(df, target)

    print("📊 Data Health Score:", score)
    for issue in issues:
        print(" -", issue)

    print("="*50)
    print("✅ Diagnosis Complete")
    print("="*50 + "\n")

    if visualize:
        plot_all(df, target)

    if report:
        from dataguardian.report.html_report import generate_html_report
        results = {
            'shape': df.shape,
            'columns': list(df.columns),
            'score': score,
            'warnings': warnings
        }
        generate_html_report(results)