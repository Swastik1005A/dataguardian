def check_missing(df):
    """
    Check for missing values in dataset
    """
    print("📊 Missing Values:")

    missing = df.isnull().sum()
    total = len(df)

    found = False

    for col, val in missing.items():
        if val > 0:
            found = True
            percent = (val / total) * 100
            print(f"⚠ {col}: {val} ({percent:.2f}%)")

    if not found:
        print("✔ No missing values")

    print()