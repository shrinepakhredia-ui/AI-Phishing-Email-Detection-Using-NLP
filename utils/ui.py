import streamlit as st


def load_css():

    with open("assets/styles.css") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


def show_header():

    st.title("🛡 AI-Driven Phishing Email Detection")

    st.markdown("""
Analyze suspicious emails using Artificial Intelligence,
Natural Language Processing (NLP), and Machine Learning
to identify phishing attacks and generate a detailed
security assessment.
""")

    st.divider()