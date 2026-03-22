def check_leakage(df, target):
    """
    Check for data leakage by correlation with target
    """
    print("🧪 Data Leakage Check:")

    if target is None or target not in df.columns:
        print("⚠ No valid target provided\n")
        return

    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if target not in numeric_df.columns:
        print("⚠ Target not numeric → skipping leakage check\n")
        return

    corr = numeric_df.corr()[target].drop(target)

    leakage_features = corr[abs(corr) > 0.9]

    if not leakage_features.empty:
        for col, val in leakage_features.items():
            print(f"⚠ Possible leakage: '{col}' highly correlated with target ({val:.2f})")
    else:
        print("✔ No strong leakage indicators")

    print()