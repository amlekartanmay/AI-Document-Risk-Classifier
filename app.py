import os
import streamlit as st

from src.text_extractor import extract_text
from src.predict import predict_risk


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Document Risk Classifier",
    page_icon="🔐",
    layout="wide"
)


# ==========================================================
# HEADER
# ==========================================================

st.title("🔐 AI Document Risk & Compliance Classifier")

st.write(
    "Upload a business document to automatically classify "
    "its potential risk level and identify documents that "
    "may require manual review."
)

st.divider()


# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📄 Upload PDF or DOCX document",
    type=["pdf", "docx"],
    help="Upload a text-based PDF or Microsoft Word document."
)


# ==========================================================
# FILE PROCESSING
# ==========================================================

if uploaded_file is not None:

    # ------------------------------------------------------
    # Create upload folder
    # ------------------------------------------------------

    os.makedirs(
        "sample_documents",
        exist_ok=True
    )


    # ------------------------------------------------------
    # Create safe file path
    # ------------------------------------------------------

    file_path = os.path.join(
        "sample_documents",
        uploaded_file.name
    )


    # ------------------------------------------------------
    # Save uploaded file
    # ------------------------------------------------------

    try:

        with open(file_path, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )

    except Exception as e:

        st.error(
            f"Could not save uploaded file: {e}"
        )

        st.stop()


    # ------------------------------------------------------
    # Extract document text
    # ------------------------------------------------------

    try:

        text = extract_text(
            file_path
        )

    except Exception as e:

        st.error(
            f"Error extracting document text: {e}"
        )

        st.stop()


    # ------------------------------------------------------
    # Check extracted text
    # ------------------------------------------------------

    if not text or not text.strip():

        st.warning(
            "⚠️ No readable text was found in this document."
        )

        st.info(
            "If this is a scanned PDF, OCR will be required."
        )

        st.stop()


    # ======================================================
    # DOCUMENT INFORMATION
    # ======================================================

    st.success(
        f"✅ Document uploaded: **{uploaded_file.name}**"
    )

    st.divider()


    # ======================================================
    # EXTRACTED TEXT
    # ======================================================

    st.subheader(
        "📄 Extracted Document Text"
    )

    with st.expander(
        "Click to view extracted text"
    ):

        st.text_area(
            "Document Content",
            text,
            height=300
        )


    # ======================================================
    # AI PREDICTION
    # ======================================================

    st.divider()

    st.subheader(
        "🤖 AI Risk Analysis"
    )


    try:

        result = predict_risk(
            text
        )

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )

        st.stop()


    # ------------------------------------------------------
    # Get prediction values
    # ------------------------------------------------------

    risk = result["risk"]

    confidence = result["confidence"]

    status = result["review_status"]

    probabilities = result["probabilities"]


    # ======================================================
    # MAIN RESULTS
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Risk Level",
            risk.upper()
        )


    with col2:

        st.metric(
            "Confidence",
            f"{confidence:.2%}"
        )


    with col3:

        st.metric(
            "Review Status",
            status
        )


    # ======================================================
    # RISK MESSAGE
    # ======================================================

    st.divider()


    if status == "MANUAL REVIEW":

        st.warning(
            "⚠️ The model confidence is below the configured "
            "threshold. Manual review is recommended."
        )

    elif risk.lower() == "high":

        st.error(
            "🚨 High-risk document detected. "
            "Manual review is recommended."
        )

    elif risk.lower() == "medium":

        st.warning(
            "⚠️ Medium-risk document detected. "
            "Additional review may be appropriate."
        )

    elif risk.lower() == "low":

        st.success(
            "✅ Low-risk classification."
        )


    # ======================================================
    # CLASS PROBABILITIES
    # ======================================================

    st.divider()

    st.subheader(
        "📊 Class Probabilities"
    )


    probability_col1, probability_col2, probability_col3 = (
        st.columns(3)
    )


    low_probability = probabilities.get(
        "low",
        0
    )

    medium_probability = probabilities.get(
        "medium",
        0
    )

    high_probability = probabilities.get(
        "high",
        0
    )


    with probability_col1:

        st.metric(
            "🟢 Low Risk",
            f"{low_probability:.2%}"
        )


    with probability_col2:

        st.metric(
            "🟡 Medium Risk",
            f"{medium_probability:.2%}"
        )


    with probability_col3:

        st.metric(
            "🔴 High Risk",
            f"{high_probability:.2%}"
        )


    # ======================================================
    # PROBABILITY BAR CHART
    # ======================================================

    probability_data = {
        "Low": low_probability,
        "Medium": medium_probability,
        "High": high_probability
    }

    st.bar_chart(
        probability_data
    )


    # ======================================================
    # DOCUMENT SUMMARY
    # ======================================================

    st.divider()

    st.subheader(
        "📋 Analysis Summary"
    )


    summary_col1, summary_col2 = st.columns(2)


    with summary_col1:

        st.write(
            f"**Document:** {uploaded_file.name}"
        )

        st.write(
            f"**Characters extracted:** {len(text):,}"
        )


    with summary_col2:

        st.write(
            f"**Predicted Risk:** {risk.upper()}"
        )

        st.write(
            f"**Model Confidence:** {confidence:.2%}"
        )


    # ======================================================
    # REVIEW DECISION
    # ======================================================

    st.divider()

    st.subheader(
        "🔎 Review Decision"
    )


    if status == "MANUAL REVIEW":

        st.warning(
            "This document has been flagged for manual review "
            "because the model confidence is below 70%."
        )

    else:

        st.success(
            "The model confidence is above the configured "
            "threshold."
        )


    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.divider()

    st.info(
        "ℹ️ This system provides automated document screening "
        "and does not constitute legal or regulatory advice."
    )


# ==========================================================
# NO FILE UPLOADED
# ==========================================================

else:

    st.info(
        "👆 Upload a PDF or DOCX document to begin analysis."
    )