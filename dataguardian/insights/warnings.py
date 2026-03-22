def generate_warnings(df):
    """
    Generate smart warnings for dataset
    """
    warnings = []

    # 1. High cardinality
    for col in df.columns:
        unique_ratio = df[col].nunique() / len(df)
        if unique_ratio > 0.95 and "id" in col.lower():
            warnings.append(f"'{col}' is likely an ID column")

    # 2. Constant columns
    for col in df.columns:
        if df[col].nunique() == 1:
            warnings.append(f"'{col}' has only one unique value → useless feature")

    # Print nicely
    print("🧠 Smart Warnings:")
    if warnings:
        for w in warnings:
            print(f"⚠ {w}")
    else:
        print("✔ No major issues detected")

    print()

    return warnings