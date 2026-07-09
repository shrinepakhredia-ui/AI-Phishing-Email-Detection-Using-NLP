import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# Evaluate All Trained Models

def evaluate_models(trained_models, X_test, y_test):

    print("=" * 70)
    print("MODEL EVALUATION STARTED")
    print("=" * 70)

    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)

    results = []

    best_model = ""
    best_accuracy = 0

    for model_name, model in trained_models.items():

        print("\n" + "-" * 70)
        print(f"Evaluating : {model_name}")
        print("-" * 70)

        try:

            # Prediction
            y_pred = model.predict(X_test)

            # Metrics
            accuracy = accuracy_score(y_test, y_pred)

            precision = precision_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            )

            recall = recall_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            )

            f1 = f1_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            )

            results.append({

                "Model": model_name,
                "Accuracy": round(accuracy, 4),
                "Precision": round(precision, 4),
                "Recall": round(recall, 4),
                "F1 Score": round(f1, 4)

            })

            print(f"Accuracy  : {accuracy:.4f}")
            print(f"Precision : {precision:.4f}")
            print(f"Recall    : {recall:.4f}")
            print(f"F1 Score  : {f1:.4f}")

            print("\nClassification Report\n")

            print(

                classification_report(

                    y_test,

                    y_pred,

                    target_names=[
                        "Safe Email",
                        "Phishing Email"
                    ],

                    zero_division=0

                )

            )

            # Confusion Matrix

            cm = confusion_matrix(
                y_test,
                y_pred
            )

            plt.figure(figsize=(6,5))

            sns.heatmap(

                cm,

                annot=True,

                fmt="d",

                cmap="Blues",

                xticklabels=[
                    "Safe Email",
                    "Phishing Email"
                ],

                yticklabels=[
                    "Safe Email",
                    "Phishing Email"
                ]

            )

            plt.title(f"{model_name} Confusion Matrix")

            plt.xlabel("Predicted")

            plt.ylabel("Actual")

            plt.tight_layout()

            filename = (
                model_name
                .lower()
                .replace(" ", "_")
            )

            plt.savefig(

                os.path.join(

                    "outputs",

                    "plots",

                    f"{filename}_confusion_matrix.png"

                )

            )

            plt.close()

            if accuracy > best_accuracy:

                best_accuracy = accuracy

                best_model = model_name

        except Exception as e:

            print(f"Error while evaluating {model_name}")
            print(e)

    # Save Comparison Table

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="Accuracy",
        ascending=False
    )

    result_df.to_csv(

        os.path.join(
            "outputs",
            "model_comparison.csv"
        ),

        index=False

    )

    # Accuracy Comparison Graph

    plt.figure(figsize=(8,5))

    plt.bar(

        result_df["Model"],

        result_df["Accuracy"]

    )

    plt.title("Model Accuracy Comparison")

    plt.xlabel("Models")

    plt.ylabel("Accuracy")

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig(

        os.path.join(

            "outputs",

            "plots",

            "model_accuracy_comparison.png"

        )

    )

    plt.close()

    # Display Results

    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)

    print(result_df)

    print("\n" + "=" * 70)
    print(f"BEST MODEL : {best_model}")
    print(f"BEST ACCURACY : {best_accuracy:.4f}")
    print("=" * 70)

    print("\nResults Saved Successfully.")

    print("\nEvaluation Completed Successfully.")