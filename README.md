📄 AI Document Risk & Compliance Classifier

An ML-powered document classification system that analyzes business documents, predicts their risk level, provides confidence scores, and flags uncertain documents for manual review.

Low Risk • Medium Risk • High Risk • Manual Review

🚀 Overview

The AI Document Risk & Compliance Classifier is a machine-learning application designed to automatically analyze business documents and classify them into different risk categories.

The system accepts PDF and DOCX documents, extracts their textual content, processes the text using TF-IDF, and uses a Logistic Regression classifier to predict the document's risk level.

When the model is uncertain about a prediction, the document is automatically flagged for manual review.

Key idea

Document
   ↓
Text Extraction
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Machine Learning Model
   ↓
Risk Prediction
   ↓
Confidence Score
   ↓
 ┌─────────────────────────┐
 │ Confidence ≥ 70%        │ → Automatic Classification
 │ Confidence < 70%        │ → Manual Review
 └─────────────────────────┘


 ✨ Features
📑 Multi-format Document Support
PDF document processing
DOCX document processing
Automatic text extraction
🤖 Machine Learning Classification
TF-IDF text vectorization
Logistic Regression classifier
Three risk categories:
🟢 Low
🟡 Medium
🔴 High
🎯 Confidence-based Review

The system uses a 70% confidence threshold.
Confidence ≥ 70%
        ↓
Automatic Classification

Confidence < 70%
        ↓
Manual Review
This helps prevent uncertain predictions from being treated as definitive classifications.

🔍 Explainable AI

The application identifies important terms contributing to the model's classification.

This provides users with additional insight into which textual features influenced the prediction.

Note: these terms are model features, not proof that a document is objectively risky.

📊 Interactive Dashboard

The Streamlit interface displays:

Predicted risk
Confidence score
Class probabilities
Important terms
Extracted document text
Manual review status


🧠 Machine Learning Pipeline
             PDF / DOCX
                  │
                  ▼
          Text Extraction
                  │
                  ▼
         Text Preprocessing
                  │
                  ▼
        TF-IDF Vectorization
                  │
                  ▼
        Logistic Regression
                  │
                  ▼
        Risk Classification
                  │
          ┌───────┴────────┐
          ▼                ▼
    Confidence ≥ 70%   Confidence < 70%
          │                │
          ▼                ▼
    Auto Classification  Manual Review


    🛠️ Tech Stack
    | Technology          | Purpose                 |
| ------------------- | ----------------------- |
| Python              | Core programming        |
| Pandas              | Dataset processing      |
| Scikit-learn        | Machine learning        |
| TF-IDF              | Text feature extraction |
| Logistic Regression | Risk classification     |
| PyMuPDF             | PDF text extraction     |
| python-docx         | DOCX text extraction    |
| Joblib              | Model serialization     |
| Streamlit           | Web interface           |
| Git                 | Version control         |
| GitHub              | Source-code hosting     |


📁 Project Structure
AI-Document-Risk-Classifier/
│
├── data/
│   ├── processed/
│   │   └── documents.csv
│   └── raw/
│
├── models/
│   ├── risk_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── sample_documents/
│
├── src/
│   ├── generate_dataset.py
│   ├── predict.py
│   ├── text_extractor.py
│   └── train_model.py
│
├── app.py
├── test_prediction.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation

Clone the repository:
git clone https://github.com/amlekartanmay/AI-Document-Risk-Classifier.git

Move into the project directory:
cd AI-Document-Risk-Classifier

Create a virtual environment:
python -m venv venv

Activate it on Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

▶️ Run the Application

Start Streamlit:

streamlit run app.py

The application will open in your browser.

Upload a PDF or DOCX document and the application will:
Upload Document
       ↓
Extract Text
       ↓
Analyze Document
       ↓
Predict Risk
       ↓
Display Confidence
       ↓
Automatic Classification / Manual Review


🧪 Train the Model

The training script can be executed using:

python src/train_model.py

The trained model and vectorizer are saved in:

models/
├── risk_classifier.pkl
└── tfidf_vectorizer.pkl


📊 Model Configuration

The project uses TF-IDF with unigram and bigram features.

TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=10000,
    ngram_range=(1, 2),
    sublinear_tf=True
)

The classifier uses Logistic Regression:

LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)


📈 Model Evaluation

The model is evaluated using:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

Example format:

Accuracy: XX%

              precision    recall    f1-score

High             XX        XX          XX
Medium           XX        XX          XX
Low              XX        XX          XX

Replace XX with the actual results produced by train_model.py. Do not use example values as actual model performance.


🗂️ Dataset

The current development dataset contains synthetically generated business-document examples representing:

Low Risk
Medium Risk
High Risk

The dataset is intended for development, testing, and demonstration.

It is not a validated real-world compliance dataset.


🔐 Privacy & Security

Uploaded documents may contain confidential or personally identifiable information.

For production deployment, additional security measures would be required, including:

Encryption at rest
Secure file storage
Authentication and authorization
Secure document deletion
Access control
Audit logging
Data retention policies
API security
PII protection


⚠️ Limitations

This project is currently a prototype.

The predictions depend heavily on the training data and model features.

The system:

Does not provide legal advice
Does not guarantee regulatory compliance
May produce incorrect classifications
Has not been validated for production compliance decisions
Uses a synthetic development dataset
Should not replace qualified human review

The manual-review mechanism is intended to reduce reliance on low-confidence predictions, not eliminate classification errors.


💡 Potential Use Cases

The architecture could be adapted for:

Business document screening
Contract pre-screening
Compliance document triage
Policy document classification
Vendor document screening
Internal document auditing
Financial document categorization
Legal-document pre-screening

Actual production use would require domain-specific datasets, validation, security controls, and appropriate human oversight.


🔮 Future Improvements
 Transformer-based embeddings
 BERT / RoBERTa classification
 RAG-based compliance analysis
 OCR support for scanned PDFs
 Document similarity search
 Compliance rule engine
 SHAP-based explainability
 Human-in-the-loop feedback
 Model retraining pipeline
 REST API
 Database integration
 Authentication & authorization
 Audit logging
 Cloud deployment
 Docker support
 Industry-specific classification models


 🖥️ Application Preview

Add screenshots of your Streamlit application here.

Dashboard

Risk Prediction

Explainable Prediction

Create a screenshots/ folder in the repository and place your screenshots there.


📌 Example Workflow

1. User uploads a document
              ↓
2. Application extracts document text
              ↓
3. Text is converted into TF-IDF features
              ↓
4. Logistic Regression predicts risk
              ↓
5. Model calculates class probabilities
              ↓
6. Confidence is evaluated
              ↓
       ┌──────┴──────┐
       ▼             ▼
   ≥ 70%            < 70%
       │             │
       ▼             ▼
 Automatic         Manual
Classification     Review


🎓 Project Relevance

This project demonstrates practical implementation of:

Natural Language Processing
Text Classification
Machine Learning
Feature Engineering
Explainable AI
Human-in-the-loop ML
Document Processing
Python Development
Streamlit Application Development
Git & GitHub Version Control


👨‍💻 Author
Tanmay Amlekar

B.Tech — Computer Science & Engineering

GitHub:
https://github.com/amlekartanmay


⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.

