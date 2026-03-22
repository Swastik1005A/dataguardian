def calculate_score(df, target=None):
    """
    Calculate data health score based on issues
    """
    score = 100
    issues = []

    # Missing values penalty
    missing_ratio = df.isnull().sum().sum() / (df.shape[0] * df.shape[1])
    if missing_ratio > 0:
        penalty = int(missing_ratio * 100)
        score -= penalty
        issues.append(f"Missing data penalty: -{penalty}")

    # Duplicate penalty
    dup_ratio = df.duplicated().sum() / len(df)
    if dup_ratio > 0:
        penalty = int(dup_ratio * 50)
        score -= penalty
        issues.append(f"Duplicate penalty: -{penalty}")

    # High correlation penalty
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    if numeric_df.shape[1] > 1:
        corr_matrix = numeric_df.corr()
        high_corr_count = 0
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if abs(corr_matrix.iloc[i, j]) > 0.9:
                    high_corr_count += 1
        if high_corr_count > 0:
            penalty = high_corr_count * 5
            score -= penalty
            issues.append(f"High correlation penalty: -{penalty}")

    # Leakage penalty
    if target and target in df.columns and df[target].dtype in ['int64', 'float64']:
        numeric_df = df.select_dtypes(include=["int64", "float64"])
        if target in numeric_df.columns:
            corr_with_target = numeric_df.corr()[target].drop(target)
            leakage_count = (abs(corr_with_target) > 0.9).sum()
            if leakage_count > 0:
                penalty = leakage_count * 10
                score -= penalty
                issues.append(f"Data leakage penalty: -{penalty}")

    score = max(score, 0)

    return score, issues