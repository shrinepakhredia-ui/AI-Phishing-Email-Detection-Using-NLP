import os
import time
import joblib
import warnings

from sklearn.exceptions import ConvergenceWarning

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier


# Ignore Neural Network Convergence Warning
warnings.filterwarnings(
    "ignore",
    category=ConvergenceWarning
)


# Train Machine Learning Models

def train_models(X_train, y_train):

    print("=" * 70)
    print("MODEL DEVELOPMENT STARTED")
    print("=" * 70)

    os.makedirs("models", exist_ok=True)

    models = {

        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            random_state=42
        ),

        "Naive Bayes": MultinomialNB(),

        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        ),

        "Neural Network": MLPClassifier(
            hidden_layer_sizes=(100,),
            max_iter=300,
            random_state=42,
            early_stopping=True,
            validation_fraction=0.1
        )

    }

    trained_models = {}

    print("\nTraining Started...\n")

    for model_name, model in models.items():

        print("-" * 70)
        print(f"Training : {model_name}")

        try:

            start_time = time.time()

            model.fit(X_train, y_train)

            end_time = time.time()

            training_time = end_time - start_time

            trained_models[model_name] = model

            filename = (
                model_name
                .lower()
                .replace(" ", "_")
                + ".pkl"
            )

            joblib.dump(
                model,
                os.path.join("models", filename)
            )

            print(f"Training Time : {training_time:.2f} Seconds")
            print(f"{model_name} Saved Successfully.\n")

        except Exception as e:

            print(f"Error while training {model_name}")
            print(e)
            print()

    print("=" * 70)
    print("ALL MODELS TRAINED SUCCESSFULLY")
    print("=" * 70)

    return trained_models