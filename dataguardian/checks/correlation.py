import numpy as np


def check_correlation(df):
    """
    Check for high correlations between numeric columns
    """
    print("📊 Correlation Analysis:")

    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if numeric_df.shape[1] < 2:
        print("⚠ Not enough numerical columns for correlation\n")
        return

    corr_matrix = numeric_df.corr()

    high_corr = []

    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            val = corr_matrix.iloc[i, j]

            if abs(val) > 0.85:
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]

                high_corr.append((col1, col2, val))

    if high_corr:
        for c1, c2, v in high_corr:
            print(f"⚠ High correlation: {c1} ↔ {c2} ({v:.2f})")
    else:
        print("✔ No strong correlations")

    print()