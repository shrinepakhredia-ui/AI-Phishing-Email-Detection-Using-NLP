def generate_explanation(text):

    text = text.lower()

    explanations = []


    credential_words = [
        "password",
        "login",
        "credential",
        "username",
        "account"
    ]


    urgency_words = [
        "urgent",
        "immediately",
        "as soon as possible",
        "final warning",
        "action required"
    ]


    security_words = [
        "verify",
        "security",
        "suspended",
        "update",
        "confirm"
    ]


    detected_credentials = [
        word for word in credential_words
        if word in text
    ]


    detected_urgency = [
        word for word in urgency_words
        if word in text
    ]


    detected_security = [
        word for word in security_words
        if word in text
    ]


    if detected_credentials:

        explanations.append(
            f"Credential related terms detected: {', '.join(detected_credentials)}"
        )


    if detected_urgency:

        explanations.append(
            f"Urgency pattern detected: {', '.join(detected_urgency)}"
        )


    if detected_security:

        explanations.append(
            f"Security manipulation keywords detected: {', '.join(detected_security)}"
        )


    if "http" in text or "www" in text:

        explanations.append(
            "External link detected"
        )


    if not explanations:

        explanations.append(
            "No major phishing indicators detected"
        )


    return explanations