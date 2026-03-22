import numpy as np


def detect_outliers(df, target=None):
    """
    Detect outliers using IQR method
    """
    print("📈 Outlier Detection (IQR method):")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        if col == target:
            continue
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        if len(outliers) > 0:
            print(f"⚠ {col}: {len(outliers)} outliers")
    
    print()