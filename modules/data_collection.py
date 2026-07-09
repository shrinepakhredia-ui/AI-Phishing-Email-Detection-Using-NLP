import pandas as pd

# Load Dataset

def load_dataset(path):

    """
    Load the dataset from the given path.

    Parameters:
        path (str): Dataset Path

    Returns:
        DataFrame
    """

    try:

        # Read Dataset
        df = pd.read_csv(path, encoding="utf-8")

        # Remove unwanted index column if present
        if "Unnamed: 0" in df.columns:
            df.drop(columns=["Unnamed: 0"], inplace=True)

        print("=" * 70)
        print("DATASET LOADED SUCCESSFULLY")
        print("=" * 70)

        return df

    except FileNotFoundError:

        print("ERROR : Dataset file not found.")
        return None

    except pd.errors.EmptyDataError:

        print("ERROR : Dataset is empty.")
        return None

    except Exception as e:

        print(f"ERROR : {e}")
        return None


# Display Dataset

def display_dataset(df):

    print("\n" + "=" * 70)
    print("FIRST FIVE RECORDS")
    print("=" * 70)

    print(df.head())


# Dataset Shape

def dataset_shape(df):

    print("\n" + "=" * 70)
    print("DATASET SHAPE")
    print("=" * 70)

    rows, columns = df.shape

    print(f"Rows    : {rows}")
    print(f"Columns : {columns}")


# Column Names

def dataset_columns(df):

    print("\n" + "=" * 70)
    print("COLUMN NAMES")
    print("=" * 70)

    for index, column in enumerate(df.columns, start=1):

        print(f"{index}. {column}")


# Dataset Information

def dataset_information(df):

    print("\n" + "=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    df.info()


# Missing Values

def missing_values(df):

    print("\n" + "=" * 70)
    print("MISSING VALUES")
    print("=" * 70)

    print(df.isnull().sum())


# Duplicate Values

def duplicate_values(df):

    print("\n" + "=" * 70)
    print("DUPLICATE RECORDS")
    print("=" * 70)

    print(f"Duplicate Rows : {df.duplicated().sum()}")


# Statistical Summary

def statistical_summary(df):

    print("\n" + "=" * 70)
    print("STATISTICAL SUMMARY")
    print("=" * 70)

    print(df.describe(include="all"))


# Dataset Summary

def dataset_summary(df):

    print("\n" + "=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    print(f"Total Records : {len(df)}")
    print(f"Total Columns : {len(df.columns)}")

    print("\nTarget Class Distribution\n")

    print(df["Email Type"].value_counts())

    print("\nPercentage Distribution\n")

    print(
        (
            df["Email Type"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
            .astype(str)
            + " %"
        )
    )