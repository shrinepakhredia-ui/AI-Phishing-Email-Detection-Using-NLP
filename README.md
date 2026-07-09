# 🛡 AI-Driven Phishing Email Detection Using NLP

An AI-powered cybersecurity application that detects phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**.

The application analyzes email content, identifies phishing indicators, evaluates potential security threats, performs URL analysis, generates AI-powered explanations, and provides a downloadable PDF security report through an interactive Streamlit interface.

# 🚀 Features

- 📧 AI-powered phishing email detection
- 🧠 Neural Network based email classification
- 🔤 Text preprocessing and cleaning
- 📑 TF-IDF feature extraction
- 📊 Confidence score prediction
- ⚠️ Risk score generation
- 🛡 Threat indicator analysis
- 🤖 Explainable AI insights
- 🌐 URL security analysis
- 📄 Downloadable PDF security report
- 🎨 Clean and responsive Streamlit interface

# 🛠 Tech Stack

| Category             | Technology                     |
| -------------------- | ------------------------------ |
| Programming Language | Python                         |
| Framework            | Streamlit                      |
| Machine Learning     | Scikit-learn                   |
| NLP                  | TF-IDF Vectorizer              |
| Model                | Neural Network (MLPClassifier) |
| Data Processing      | Pandas, NumPy                  |
| Model Serialization  | Joblib                         |
| PDF Generation       | ReportLab                      |

# 📂 Project Structure

```text
AI_Phishing_Email_Detection/
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│   └── styles.css
│
├── dataset/
│   └── Phishing_Email.csv
│
├── models/
│   ├── neural_network.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
│
├── modules/
│   ├── data_cleaning.py
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── model_development.py
│   ├── evaluation.py
│   ├── threat_analysis.py
│   ├── explainability.py
│   └── url_analysis.py
│
├── outputs/
│   └── plots/
│
└── utils/
    ├── ui.py
    └── report.py
```

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/shrinepakhredia-ui/AI-Phishing-Email-Detection-Using-NLP.git
```

Move into the project directory

```bash
cd AI-Phishing-Email-Detection-Using-NLP
```

Install all dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

# ▶️ How to Use

1. Launch the Streamlit application.
2. Paste the email content into the input box.
3. Click **Analyze Email**.
4. View:
   - Prediction Result
   - Confidence Score
   - Risk Score
   - Threat Report
   - AI Insights
   - URL Intelligence
5. Download the PDF Security Report.

## 👨‍💻 Author

**Shrine Pakhredia**

B.Tech – Artificial Intelligence & Machine Learning

GitHub: https://github.com/shrinepakhredia-ui
