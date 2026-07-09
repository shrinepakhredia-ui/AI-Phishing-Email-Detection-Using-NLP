from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def generate_pdf_report(
    prediction,
    confidence,
    risk_score,
    risk_level,
    reasons,
    explanations,
    url_results
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==========================================================
    # Title
    # ==========================================================

    elements.append(
        Paragraph(
            "<font size=22><b>AI-Driven Phishing Email Detection</b></font>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "<font size=14>Security Assessment Report</font>",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 0.3 * inch))

    # ==========================================================
    # Executive Summary
    # ==========================================================

    if prediction == "Safe Email":

        summary = f"""
        The submitted email was analyzed using an NLP-based phishing
        detection model and has been classified as
        <b>Safe Email</b> with a confidence score of
        <b>{confidence:.2f}%</b>.
        No major phishing indicators were identified.
        """

    else:

        summary = f"""
        The submitted email was analyzed using an NLP-based phishing
        detection model and has been classified as
        <b>Phishing Email</b> with a confidence score of
        <b>{confidence:.2f}%</b>.

        Multiple phishing indicators were detected.
        Users are advised not to interact with this email.
        """

    elements.append(
        Paragraph("<b>Executive Summary</b>", styles["Heading1"])
    )

    elements.append(
        Paragraph(summary, styles["BodyText"])
    )

    elements.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # Analysis Summary
    # ==========================================================

    elements.append(
        Paragraph("<b>Analysis Summary</b>", styles["Heading1"])
    )

    table_data = [

        ["Parameter", "Result"],

        ["Prediction", prediction],

        ["Confidence", f"{confidence:.2f}%"],

        ["Risk Score", f"{risk_score}/100"],

        ["Risk Level", risk_level]

    ]

    table = Table(
        table_data,
        colWidths=[2.5 * inch, 3.2 * inch]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F62FE")),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),

        ("ALIGN", (0, 0), (-1, -1), "CENTER")

    ]))

    elements.append(table)

    elements.append(Spacer(1, 0.3 * inch))

    # ==========================================================
    # Threat Report
    # ==========================================================

    elements.append(
        Paragraph("<b>Threat Indicators</b>", styles["Heading1"])
    )

    if reasons:

        for reason in reasons:

            elements.append(
                Paragraph(f"• {reason}", styles["BodyText"])
            )

    else:

        elements.append(
            Paragraph(
                "No significant threat indicators detected.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # AI Insights
    # ==========================================================

    elements.append(
        Paragraph("<b>AI Insights</b>", styles["Heading1"])
    )

    if explanations:

        for item in explanations:

            elements.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )

    else:

        elements.append(
            Paragraph(
                "No AI insights available.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # URL Intelligence
    # ==========================================================

    elements.append(
        Paragraph("<b>URL Intelligence</b>", styles["Heading1"])
    )

    if url_results:

        for url in url_results:

            elements.append(
                Paragraph(
                    f"<b>URL:</b> {url['url']}",
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    f"<b>Risk Score:</b> {url['score']}/100",
                    styles["BodyText"]
                )
            )

            for reason in url["reasons"]:

                elements.append(
                    Paragraph(
                        f"• {reason}",
                        styles["BodyText"]
                    )
                )

            elements.append(Spacer(1, 10))

    else:

        elements.append(
            Paragraph(
                "No URLs detected in the submitted email.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # Security Recommendation
    # ==========================================================

    elements.append(
        Paragraph("<b>Security Recommendations</b>", styles["Heading1"])
    )

    if prediction == "Safe Email":

        recommendations = [

            "Continue verifying unknown senders.",

            "Avoid downloading unexpected attachments.",

            "Remain cautious before clicking external links."

        ]

    else:

        recommendations = [

            "Do NOT click suspicious links.",

            "Never share passwords or OTPs.",

            "Verify the sender before responding.",

            "Report the email to your organization.",

            "Delete the email if confirmed malicious."

        ]

    for item in recommendations:

        elements.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.3 * inch))

    # ==========================================================
    # Footer
    # ==========================================================

    elements.append(
        Paragraph(
            "<b>Generated By</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "AI-Driven Phishing Email Detection Using NLP",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated on : {datetime.now().strftime('%d %B %Y | %I:%M %p')}",
            styles["Italic"]
        )
    )

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf