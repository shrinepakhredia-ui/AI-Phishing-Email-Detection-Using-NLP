# ============================================================
# Project : AI-Driven Phishing Email Detection Using NLP
# Deployment : Streamlit
# ============================================================

import streamlit as st
import joblib
import numpy as np

from modules.threat_analysis import calculate_risk_score, get_risk_level
from modules.data_cleaning import clean_text


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI-Driven Phishing Email Detection",
    page_icon="📧",
    layout="centered"
)


# ============================================================
# LOAD TRAINED MODELS
# ============================================================

try:

    model = joblib.load("models/neural_network.pkl")

    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

    encoder = joblib.load("models/label_encoder.pkl")

except Exception as e:

    st.error(f"Error Loading Models : {e}")

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("📧 AI-Driven Phishing Email Detection Using NLP")

st.markdown(
"""
This application predicts whether an email is **Safe**
or **Phishing** using Natural Language Processing and
Machine Learning.
"""
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Project Information")

st.sidebar.write("**Algorithm :** Neural Network")

st.sidebar.write("**Feature Extraction :** TF-IDF")

st.sidebar.write("**Dataset :** Phishing_Email.csv")

st.sidebar.write("**Language :** Python")

st.sidebar.write("**Framework :** Streamlit")


# ============================================================
# EMAIL INPUT
# ============================================================

email_text = st.text_area(

    "Enter Email Text",

    height=250,

    placeholder="Paste Email Content Here..."

)


# ============================================================
# PREDICTION
# ============================================================

if st.button("🔍 Detect Email", use_container_width=True):

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

        st.divider()

        st.subheader("Prediction Result")

        if result == "Safe Email":

            st.success("✅ Safe Email")

        else:

            st.error("🚨 Phishing Email")

        st.metric(

            "Confidence Score",

            f"{confidence:.2f}%"

        )

        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )
        
        risk_level = get_risk_level(risk_score)

        st.subheader("Risk Classification")

        st.write(risk_level)


        st.subheader("Threat Analysis")


        if reasons:

            for reason in reasons:

                st.warning(reason)

        else:

            st.info(
                "No major threat indicators detected."
            )




# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
"""
Developed using Python, Streamlit,
TF-IDF and Machine Learning.
"""
)