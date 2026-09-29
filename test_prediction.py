from src.predict import predict_risk


test_documents = [

    """
    The department meeting is scheduled for Monday morning.
    Employees can contact the administration team for further
    information about the meeting.
    """,

    """
    The supplier agreement contains specific contractual
    obligations and requires management approval before
    implementation.
    """,

    """
    The document contains confidential customer information
    and sensitive personal data. Unauthorized personnel must
    not access or disclose this information.
    """
]


print("=" * 60)
print("AI DOCUMENT RISK CLASSIFIER TEST")
print("=" * 60)


for index, text in enumerate(
    test_documents,
    start=1
):

    result = predict_risk(text)

    print(f"\nDocument {index}")
    print("-" * 40)

    print(
        "Risk:",
        result["risk"].upper()
    )

    print(
        "Confidence:",
        f"{result['confidence']:.2%}"
    )

    print(
        "Review Status:",
        result["review_status"]
    )