import joblib


# ==========================================================
# LOAD MODEL
# ==========================================================

MODEL_PATH = "models/risk_classifier.pkl"

VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


model = joblib.load(
    MODEL_PATH
)

vectorizer = joblib.load(
    VECTORIZER_PATH
)


# ==========================================================
# CONFIGURATION
# ==========================================================

CONFIDENCE_THRESHOLD = 0.70


# ==========================================================
# PREDICTION
# ==========================================================

def predict_risk(text):

    # Convert document to TF-IDF
    text_vector = vectorizer.transform(
        [text]
    )


    # Prediction
    prediction = model.predict(
        text_vector
    )[0]


    # Probability for every class
    probabilities = model.predict_proba(
        text_vector
    )[0]


    # Class names
    classes = model.classes_


    # Create probability dictionary
    class_probabilities = {
        class_name: float(probability)
        for class_name, probability
        in zip(classes, probabilities)
    }


    # Highest probability
    confidence = max(
        probabilities
    )


    # Manual review decision
    if confidence < CONFIDENCE_THRESHOLD:

        review_status = "MANUAL REVIEW"

    else:

        review_status = "AUTOMATIC CLASSIFICATION"


    return {

        "risk": prediction,

        "confidence": float(
            confidence
        ),

        "review_status": review_status,

        "probabilities": class_probabilities

    }