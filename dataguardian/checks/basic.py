def analyze_columns(df, target=None):
    """
    Analyze column types in dataset
    """
    print("📌 Column Analysis:")

    num_cols = list(df.select_dtypes(include=["int64", "float64"]).columns)
    cat_cols = list(df.select_dtypes(include=["object" , "category"]).columns)

    if target and target in num_cols:
        num_cols.remove(target)

    print(f"🔢 Numerical Columns ({len(num_cols)}): {num_cols}")
    print(f"🔤 Categorical Columns ({len(cat_cols)}): {cat_cols}")

    print()