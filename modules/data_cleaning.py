import re
import string
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("corpora/omw-1.4")
except LookupError:
    nltk.download("omw-1.4")


# Initialize NLP Resources

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Clean Single Email

def clean_text(text):

    # Handle Missing Values
    if pd.isna(text):
        return ""

    text = str(text).lower()

    # Remove HTML Tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|https\S+|www\S+", " ", text)

    # Remove Email Addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove Numbers
    text = re.sub(r"\d+", " ", text)

    # Remove Punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenization
    words = text.split()

    cleaned_words = []

    for word in words:

        if word not in stop_words:

            cleaned_words.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(cleaned_words)


# Clean Complete Dataset

def clean_dataset(df, text_column):

    print("=" * 70)
    print("DATA CLEANING STARTED")
    print("=" * 70)

    before_rows = len(df)

    df = df.dropna(subset=[text_column]).copy()

    after_rows = len(df)

    print(f"\nMissing Records Removed : {before_rows - after_rows}")

    df.reset_index(drop=True, inplace=True)

    df["cleaned_text"] = df[text_column].apply(clean_text)

    print("\nText Cleaning Completed Successfully.")

    print("\nSample Cleaned Data\n")

    print(df[[text_column, "cleaned_text"]].head())

    print("\nData Cleaning Completed Successfully.")

    return df