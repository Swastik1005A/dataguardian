def check_duplicates(df):
    """
    Check for duplicate rows in dataset
    """
    print("🔁 Duplicate Rows:")

    dup_count = df.duplicated().sum()

    if dup_count > 0:
        print(f"⚠ Found {dup_count} duplicate rows")
    else:
        print("✔ No duplicate rows")

    print()