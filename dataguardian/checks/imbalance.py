def check_imbalance(df, target):
    """
    Check for class imbalance in target variable
    """
    print("⚖️ Target Imbalance Check:")

    if target is None or target not in df.columns:
        print("⚠ No valid target provided\n")
        return

    counts = df[target].value_counts(normalize=True) * 100

    for cls, pct in counts.items():
        print(f"{cls}: {pct:.2f}%")

    # Detect imbalance
    if len(counts) == 2:
        if counts.max() > 80:
            print("⚠ Imbalance detected (one class > 80%)")

    print()