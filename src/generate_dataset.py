import os
import random
import pandas as pd


random.seed(42)


# ==========================================================
# LOW-RISK DOCUMENT COMPONENTS
# ==========================================================

low_subjects = [
    "The monthly team meeting",
    "The internal project meeting",
    "The employee training session",
    "The office maintenance schedule",
    "The department newsletter",
    "The weekly project update",
    "The staff communication",
    "The office event",
    "The routine administrative process",
    "The employee orientation program",
    "The internal communication",
    "The quarterly planning meeting",
]

low_actions = [
    "is scheduled for Monday morning",
    "will take place next week",
    "contains routine administrative information",
    "provides general information to employees",
    "contains the latest project updates",
    "provides information about upcoming activities",
    "describes the standard operating schedule",
    "contains general organizational information",
    "provides instructions for routine office activities",
    "summarizes regular departmental activities",
]

low_details = [
    "Employees can contact the administration team for further information.",
    "The information is intended for internal organizational use.",
    "Employees should follow the normal office procedures.",
    "The department will communicate any future schedule changes.",
    "The meeting agenda will be shared with participants.",
    "Employees may contact their supervisor with routine questions.",
    "The document contains general operational information.",
    "The schedule may be updated according to organizational requirements.",
]


# ==========================================================
# MEDIUM-RISK DOCUMENT COMPONENTS
# ==========================================================

medium_subjects = [
    "The supplier agreement",
    "The employee policy",
    "The procurement document",
    "The service agreement",
    "The employment contract",
    "The financial procedure",
    "The vendor documentation",
    "The internal security policy",
    "The customer service agreement",
    "The business contract",
    "The operational policy",
    "The compliance procedure",
]

medium_actions = [
    "contains specific contractual obligations",
    "requires management approval",
    "defines financial responsibilities",
    "contains conditions that must be reviewed",
    "requires supporting documentation",
    "defines responsibilities for the involved parties",
    "contains terms related to business operations",
    "requires compliance with internal procedures",
    "contains requirements for the supplier",
    "defines approval and authorization procedures",
]

medium_details = [
    "The responsible department should review the document before approval.",
    "Failure to provide the required documentation may delay the process.",
    "Management approval is required before implementation.",
    "The terms should be reviewed by the appropriate business team.",
    "The department must verify the required information before proceeding.",
    "The organization should maintain appropriate records for this process.",
    "Any changes to the agreement require appropriate authorization.",
    "The document should be reviewed according to internal procedures.",
]


# ==========================================================
# HIGH-RISK DOCUMENT COMPONENTS
# ==========================================================

high_subjects = [
    "The customer information document",
    "The confidential business agreement",
    "The data processing agreement",
    "The financial information document",
    "The privacy-related agreement",
    "The sensitive customer record",
    "The information security document",
    "The confidential employee record",
    "The regulated data document",
    "The customer data agreement",
    "The confidential financial report",
    "The sensitive information policy",
]

high_actions = [
    "contains confidential customer information",
    "contains sensitive personal data",
    "contains personally identifiable information",
    "contains confidential financial information",
    "defines restrictions on sensitive information",
    "contains information that requires restricted access",
    "addresses unauthorized disclosure of information",
    "contains sensitive business information",
    "contains protected customer records",
    "requires strict access controls",
]

high_details = [
    "Unauthorized personnel must not access or disclose the information.",
    "Personal data must be protected from unauthorized access.",
    "Sensitive information must only be shared with authorized personnel.",
    "Unauthorized disclosure may create significant compliance concerns.",
    "Access to the information must be restricted and monitored.",
    "The organization must implement appropriate security controls.",
    "Confidential information must not be transferred to unauthorized parties.",
    "The document requires careful review of privacy and security obligations.",
    "Sensitive records must be securely stored and appropriately protected.",
]


# ==========================================================
# GENERATOR
# ==========================================================

def generate_documents(subjects, actions, details, risk, count):

    documents = []

    for _ in range(count):

        subject = random.choice(subjects)
        action = random.choice(actions)
        detail = random.choice(details)

        text = f"{subject} {action}. {detail}"

        documents.append({
            "text": text,
            "risk": risk
        })

    return documents


# ==========================================================
# CREATE DATASET
# ==========================================================

documents = []

documents.extend(
    generate_documents(
        low_subjects,
        low_actions,
        low_details,
        "low",
        120
    )
)

documents.extend(
    generate_documents(
        medium_subjects,
        medium_actions,
        medium_details,
        "medium",
        120
    )
)

documents.extend(
    generate_documents(
        high_subjects,
        high_actions,
        high_details,
        "high",
        120
    )
)


# Shuffle dataset

random.shuffle(documents)


# ==========================================================
# SAVE
# ==========================================================

output_directory = "data/processed"

os.makedirs(output_directory, exist_ok=True)

output_file = os.path.join(
    output_directory,
    "documents.csv"
)

df = pd.DataFrame(documents)

df.to_csv(
    output_file,
    index=False
)


print("=" * 50)
print("DATASET GENERATED")
print("=" * 50)

print(f"Total documents: {len(df)}")

print("\nClass distribution:")

print(df["risk"].value_counts())

print("\nSaved to:")

print(output_file)