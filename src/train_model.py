import os

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split


# ==========================================================
# CONFIGURATION
# ==========================================================

DATA_PATH = "data/processed/documents.csv"

MODEL_DIRECTORY = "models"

VECTORIZER_PATH = os.path.join(
    MODEL_DIRECTORY,
    "tfidf_vectorizer.pkl"
)

MODEL_PATH = os.path.join(
    MODEL_DIRECTORY,
    "risk_classifier.pkl"
)


# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 60)
print("AI DOCUMENT RISK CLASSIFIER - MODEL TRAINING")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"\nTotal documents: {len(df)}")

print("\nClass distribution:")
print(df["risk"].value_counts())


# ==========================================================
# REMOVE EMPTY RECORDS
# ==========================================================

df = df.dropna(
    subset=["text", "risk"]
)

df["text"] = df["text"].astype(str)


# ==========================================================
# FEATURES AND TARGET
# ==========================================================

X = df["text"]

y = df["risk"]


# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining documents:", len(X_train))
print("Testing documents:", len(X_test))


# ==========================================================
# TF-IDF
# ==========================================================

print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=10000,
    ngram_range=(1, 2),
    sublinear_tf=True
)


X_train_tfidf = vectorizer.fit_transform(
    X_train
)

X_test_tfidf = vectorizer.transform(
    X_test
)


print(
    "TF-IDF feature count:",
    X_train_tfidf.shape[1]
)


# ==========================================================
# TRAIN MODEL
# ==========================================================

print("\nTraining Logistic Regression model...")

model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)

model.fit(
    X_train_tfidf,
    y_train
)


# ==========================================================
# PREDICTION
# ==========================================================

predictions = model.predict(
    X_test_tfidf
)


# ==========================================================
# ACCURACY
# ==========================================================

accuracy = accuracy_score(
    y_test,
    predictions
)


print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(
    f"\nAccuracy: {accuracy:.2%}"
)


# ==========================================================
# CLASSIFICATION REPORT
# ==========================================================

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ==========================================================
# CONFUSION MATRIX
# ==========================================================

labels = [
    "high",
    "medium",
    "low"
]

matrix = confusion_matrix(
    y_test,
    predictions,
    labels=labels
)


print("\nConfusion Matrix:")

print(
    pd.DataFrame(
        matrix,
        index=labels,
        columns=labels
    )
)


# ==========================================================
# SAVE MODEL
# ==========================================================

os.makedirs(
    MODEL_DIRECTORY,
    exist_ok=True
)


joblib.dump(
    vectorizer,
    VECTORIZER_PATH
)


joblib.dump(
    model,
    MODEL_PATH
)


print("\n" + "=" * 60)
print("MODEL SAVED")
print("=" * 60)

print(
    f"\nVectorizer:\n{VECTORIZER_PATH}"
)

print(
    f"\nClassifier:\n{MODEL_PATH}"
)