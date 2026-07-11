import streamlit as st


def load_css():

    with open("assets/styles.css") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


def show_header():

    col1, col2 = st.columns([12, 1])

    with col1:

        st.title("🛡 AI-Driven Phishing Email Detection")

        st.markdown(
            """
Analyze suspicious emails using **Artificial Intelligence**, **Natural Language Processing (NLP)**, and **Machine Learning** to identify phishing attacks and generate a detailed security assessment.
"""
        )

    with col2:

        with st.popover("ℹ️"):

            st.markdown("""
### 🛡 About This Project

This application detects phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**.

---

### 🚀 Technology Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorizer
- Neural Network (MLPClassifier)
- ReportLab

---

### ✨ Features

- AI-powered Email Classification
- Threat Indicator Analysis
- Explainable AI
- URL Security Analysis
- Risk Score Generation
- Downloadable PDF Report

###  👨‍💻 Developer:** Shrine Pakhredia\n\n"
    "[GitHub Repository](https://github.com/shrinepakhredia-ui/AI-Phishing-Email-Detection-Using-NLP)"
""")

