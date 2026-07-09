import streamlit as st
import joblib
import numpy as np

from modules.threat_analysis import calculate_risk_score, get_risk_level
from modules.explainability import generate_explanation
from modules.url_analysis import analyze_urls
from modules.data_cleaning import clean_text

from utils.ui import load_css, show_header
from utils.report import generate_pdf_report


# PAGE CONFIGURATION

st.set_page_config(
    page_title="AI-Driven Phishing Email Detection",
    page_icon="📧",
    layout="wide"
)

# LOAD TRAINED MODELS

try:

    model = joblib.load("models/neural_network.pkl")

    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

    encoder = joblib.load("models/label_encoder.pkl")

except Exception as e:

    st.error(f"Error Loading Models : {e}")

    st.stop()


load_css()

show_header()



st.divider()

# EMAIL INPUT

st.subheader("📧 Email Content")

email_text = st.text_area(
    "",
    height=280,
    placeholder="Paste the email content here for security analysis..."
)

# PREDICTION

if st.button("🛡 Analyze Email", use_container_width=True):

    if email_text.strip() == "":

        st.warning("Please Enter Email Text.")

    else:

        with st.spinner("Analyzing Email..."):

            cleaned = clean_text(email_text)

            vector = vectorizer.transform([cleaned])

            prediction = model.predict(vector)

            probability = model.predict_proba(vector)

            confidence = np.max(probability) * 100

            result = encoder.inverse_transform(prediction)[0]

            risk_score, reasons = calculate_risk_score(email_text)

            risk_level = get_risk_level(risk_score)

            explanations = generate_explanation(email_text)

            url_results = analyze_urls(email_text)

            pdf_report = generate_pdf_report(
                prediction=result,
                confidence=confidence,
                risk_score=risk_score,
                risk_level=risk_level,
                reasons=reasons,
                explanations=explanations,
                url_results=url_results
            )



        st.divider()

        st.subheader("Prediction Result")

        if result == "Safe Email":

            st.success("✅ Safe Email")

        else:

            st.error("🚨 Phishing Email")


        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🎯 Confidence",
                f"{confidence:.2f}%"
            )
            st.progress(confidence / 100)

        with col2:
            st.metric(
                "⚠ Risk Score",
                f"{risk_score}/100"
            )
            st.progress(risk_score / 100)

        with col3:
            st.metric(
                "🛡 Risk Level",
                risk_level
            )


        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🛡 Threat Report",
                "🤖 AI Insights",
                "🌐 URL Intelligence",
                "ℹ️ About"
            ]
        )


        with tab1:

            st.subheader("Threat Indicators")

            if reasons:

                for reason in reasons:

                    st.warning("⚠ " + reason)

            else:

                st.success(
                    "No major threat indicators detected."
                )


        with tab2:

            st.subheader("AI Reasoning")

            for item in explanations:

                st.info(
                    "✓ " + item
                )


        with tab3:

            st.subheader("URL Security Analysis")

            if url_results:

                for item in url_results:

                    st.write(
                        f"🔗 {item['url']}"
                    )

                    st.metric(
                        "URL Risk Score",
                        f"{item['score']}/100"
                    )


                    for reason in item["reasons"]:

                        st.warning(reason)

            else:

                st.info(
                    "No URLs detected in email."
                )

        with tab4:

            st.subheader("About This Project")

            st.markdown("""
        ### AI-Driven Phishing Email Detection Using NLP

        This application detects phishing emails using Natural Language Processing
        and Machine Learning.

        ### Technology Stack

        - Python
        - Streamlit
        - Scikit-learn
        - TF-IDF Vectorizer
        - Neural Network

        ### Key Features

        - AI-based Email Classification
        - Threat Analysis
        - Explainable AI
        - URL Intelligence
        - Risk Score Generation

        ### Detection Pipeline

        Email ➜ Text Cleaning ➜ TF-IDF ➜ Neural Network ➜ Threat Analysis ➜ URL Intelligence ➜ Final Report
        """)


        st.divider()

        st.subheader("💡 Security Recommendation")

        if result == "Safe Email":

            st.success(
                """
        ✅ This email appears to be safe.

        • Verify unknown senders.
        • Avoid downloading unexpected attachments.
        • Stay cautious while clicking links.
        """
            )

        else:

            st.error(
                """
        ⚠ This email appears to be a phishing attempt.

        • Do not click suspicious links.
        • Never share passwords or OTPs.
        • Verify the sender's identity.
        • Report the email if required.
        """
            )

        st.divider()

        st.download_button(
            label="📄 Download Security Report",
            data=pdf_report,
            file_name="Phishing_Email_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )


# FOOTER

st.caption(
"""
🛡 Developed with Python • Streamlit • NLP • TF-IDF • Neural Network

© 2026 AI-Driven Phishing Email Detection Project
"""
)