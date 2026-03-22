import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_heatmap(df):
    """
    Plot heatmap of missing values
    """
    plt.figure()
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.tight_layout()
    plt.show()


def plot_numeric_distributions(df):
    """
    Plot distributions of numeric columns
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()


def plot_boxplots(df):
    """
    Plot boxplots for numeric columns
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.show()


def plot_violin(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        plt.figure()
        sns.violinplot(x=df[col])
        plt.title(f"Violin Plot of {col}")
        plt.tight_layout()
        plt.show()


def plot_correlation_heatmap(df):
    """
    Plot correlation heatmap for numeric columns
    """
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if numeric_df.shape[1] < 2:
        print("⚠ Not enough numerical columns")
        return

    corr = numeric_df.corr()

    plt.figure()
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_pairplot(df):
    """
    Plot pairplot for numeric columns
    """
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if numeric_df.shape[1] > 1:
        sns.pairplot(numeric_df)
        plt.show()


def plot_scatter(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for i in range(len(numeric_cols)):
        for j in range(i):
            plt.figure()
            sns.scatterplot(x=df[numeric_cols[i]], y=df[numeric_cols[j]])
            plt.title(f"{numeric_cols[i]} vs {numeric_cols[j]}")
            plt.tight_layout()
            plt.show()


def plot_categorical_counts(df):
    """
    Plot count plots for categorical columns
    """
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in cat_cols:
        plt.figure()
        sns.countplot(x=df[col])
        plt.title(f"Count Plot of {col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def plot_target_distribution(df, target):
    """
    Plot distribution of target variable
    """
    if target is None or target not in df.columns:
        print("⚠ Invalid target")
        return

    plt.figure()
    sns.countplot(x=df[target])
    plt.title(f"Target Distribution ({target})")
    plt.tight_layout()
    plt.show()


def plot_line_trend(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) >= 2:
        plt.figure()
        plt.plot(df[numeric_cols[0]], df[numeric_cols[1]])
        plt.title(f"Line Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
        plt.tight_layout()
        plt.show()


def plot_all(df, target=None):
    """
    Generate full visualization suite
    """
    print("📊 Generating Full Visualization Suite...")

    plot_missing_heatmap(df)
    plot_numeric_distributions(df)
    plot_boxplots(df)
    plot_correlation_heatmap(df)
    if len(df) <= 5000:
        plot_pairplot(df)
    plot_categorical_counts(df)
    plot_target_distribution(df, target)

    print("✅ Visualization Complete")