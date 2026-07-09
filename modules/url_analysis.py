import re
from urllib.parse import urlparse


SUSPICIOUS_DOMAIN_WORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "payment",
    "confirm"
]


def extract_urls(text):

    urls = re.findall(
        r'https?://\S+',
        text
    )

    return urls



def analyze_url(url):

    score = 0
    reasons = []


    parsed = urlparse(url)

    domain = parsed.netloc.lower()


    # HTTPS check

    if not url.startswith("https"):

        score += 25

        reasons.append(
            "Non-HTTPS connection detected"
        )


    # Suspicious keywords

    found_words = []

    for word in SUSPICIOUS_DOMAIN_WORDS:

        if word in domain:

            found_words.append(word)


    if found_words:

        score += 30

        reasons.append(
            f"Suspicious domain keywords: {', '.join(found_words)}"
        )


    # Hyphen check

    if domain.count("-") >= 2:

        score += 15

        reasons.append(
            "Multiple hyphens detected in domain"
        )


    # Long URL

    if len(url) > 75:

        score += 15

        reasons.append(
            "Unusually long URL"
        )


    if score > 100:

        score = 100


    return score, reasons



def analyze_urls(text):

    urls = extract_urls(text)

    results = []


    for url in urls:

        score, reasons = analyze_url(url)

        results.append(
            {
                "url": url,
                "score": score,
                "reasons": reasons
            }
        )


    return results