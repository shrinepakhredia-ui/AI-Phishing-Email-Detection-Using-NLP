# ============================================================
# Threat Analysis Module
# AI-Driven Phishing Email Detection
# ============================================================

import re


# Suspicious phishing keywords

SUSPICIOUS_KEYWORDS = [
    "verify",
    "account",
    "password",
    "login",
    "bank",
    "urgent",
    "click",
    "update",
    "confirm",
    "security",
    "suspended",
    "payment",
    "credential"
]


# Urgency indicators

URGENCY_WORDS = [
    "urgent",
    "immediately",
    "as soon as possible",
    "within 24 hours",
    "action required",
    "final warning"
]


def detect_keywords(text):

    found = []

    text = text.lower()

    for word in SUSPICIOUS_KEYWORDS:

        if word in text:
            found.append(word)

    return found



def detect_urgency(text):

    found = []

    text = text.lower()

    for word in URGENCY_WORDS:

        if word in text:
            found.append(word)

    return found



def detect_links(text):

    urls = re.findall(
        r'https?://\S+',
        text
    )

    return urls



def calculate_risk_score(text):

    score = 0

    reasons = []


    keywords = detect_keywords(text)

    urgency = detect_urgency(text)

    links = detect_links(text)


    if keywords:

        score += 30

        reasons.append(
            f"Suspicious keywords detected: {', '.join(keywords)}"
        )


    if urgency:

        score += 25

        reasons.append(
            "Urgent action language detected"
        )


    if links:

        score += 25

        reasons.append(
            "External links detected"
        )


    if len(text) > 1000:

        score += 10

        reasons.append(
            "Long email content detected"
        )


    if score > 100:

        score = 100


    return score, reasons

def get_risk_level(score):

    if score >= 75:
        return "🔴 High Risk"

    elif score >= 40:
        return "🟠 Medium Risk"

    else:
        return "🟢 Low Risk"