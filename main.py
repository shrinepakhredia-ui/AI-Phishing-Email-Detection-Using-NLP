from modules.data_collection import (
    load_dataset,
    display_dataset,
    dataset_shape,
    dataset_columns,
    dataset_information,
    missing_values,
    duplicate_values,
    statistical_summary,
    dataset_summary
)
from modules.data_cleaning import clean_dataset

from modules.feature_engineering import feature_engineering

from modules.model_development import train_models

from modules.evaluation import evaluate_models


# Main Function

def main():

    print("\n" + "=" * 70)
    print("      AI-Driven Phishing Email Detection Using NLP")
    print("=" * 70)

    # Dataset Path
    dataset_path = "dataset/Phishing_Email.csv"

    # DATA COLLECTION

    print("\n[PHASE 1] DATA COLLECTION\n")

    df = load_dataset(dataset_path)

    if df is None:
        print("\nDataset Loading Failed.")
        print("Project Terminated.")
        return

    display_dataset(df)
    dataset_shape(df)
    dataset_columns(df)
    dataset_information(df)
    missing_values(df)
    duplicate_values(df)
    statistical_summary(df)
    dataset_summary(df)

    print("\nData Collection Completed Successfully.")

    # DATA CLEANING

    print("\n[PHASE 2] DATA CLEANING\n")

    df = clean_dataset(
        df,
        text_column="Email Text"
    )

    print("\nData Cleaning Completed Successfully.")

    # FEATURE ENGINEERING

    print("\n[PHASE 3] FEATURE ENGINEERING\n")

    X_train, X_test, y_train, y_test = feature_engineering(
        df,
        text_column="cleaned_text",
        target_column="Email Type"
    )

    print("\nFeature Engineering Completed Successfully.")

    # MODEL DEVELOPMENT

    print("\n[PHASE 4] MODEL DEVELOPMENT\n")

    trained_models = train_models(
        X_train,
        y_train
    )

    print("\nModel Development Completed Successfully.")

    # MODEL EVALUATION

    print("\n[PHASE 5] MODEL EVALUATION\n")

    evaluate_models(
        trained_models,
        X_test,
        y_test
    )

    print("\nModel Evaluation Completed Successfully.")

    # Project Completed

    print("\nBest Model Successfully Selected.")

    print("\n" + "=" * 70)
    print("PROJECT EXECUTED SUCCESSFULLY")
    print("=" * 70)

    print("\nThank You!\n")


# Driver Code

if __name__ == "__main__":
    main()