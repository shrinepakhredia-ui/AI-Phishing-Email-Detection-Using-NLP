import os
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# Feature Engineering

def feature_engineering(df,
                        text_column="cleaned_text",
                        target_column="Email Type"):

    print("=" * 70)
    print("FEATURE ENGINEERING STARTED")
    print("=" * 70)

    try:

        # Separate Features and Target

        X = df[text_column]

        y = df[target_column]

        # Create Models Folder

        os.makedirs("models", exist_ok=True)

        # Label Encoding

        print("\nEncoding Target Labels...")

        label_encoder = LabelEncoder()

        y = label_encoder.fit_transform(y)

        joblib.dump(
            label_encoder,
            os.path.join("models", "label_encoder.pkl")
        )

        print("Label Encoder Saved Successfully.")

        print("\nLabel Mapping")

        for index, label in enumerate(label_encoder.classes_):
            print(f"{label}  -->  {index}")

        # TF-IDF Vectorization

        print("\nApplying TF-IDF Vectorizer...")

        tfidf = TfidfVectorizer(

            max_features=5000,

            stop_words=None,

            ngram_range=(1, 2)

        )

        X = tfidf.fit_transform(X)

        joblib.dump(
            tfidf,
            os.path.join("models", "tfidf_vectorizer.pkl")
        )

        print("TF-IDF Vectorizer Saved Successfully.")

        print(f"\nTotal Features Generated : {len(tfidf.get_feature_names_out())}")

        # Train Test Split

        print("\nSplitting Dataset...")

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        print(f"\nTraining Samples : {X_train.shape[0]}")
        print(f"Testing Samples  : {X_test.shape[0]}")

        print("\nFeature Engineering Completed Successfully.")

        return X_train, X_test, y_train, y_test

    except Exception as e:

        print(f"\nError in Feature Engineering : {e}")

        return None, None, None, None