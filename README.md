<div align="center">

# 🛡 AI-Driven Phishing Email Detection Using NLP

### AI-Powered Cybersecurity Tool for Detecting Phishing Emails using Natural Language Processing & Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-success)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Why This Project?](#-why-this-project)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Detection Pipeline](#-detection-pipeline)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Model Performance](#-model-performance)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

# 📖 Project Overview

**AI-Driven Phishing Email Detection Using NLP** is an intelligent cybersecurity application that detects phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**.

The application analyzes email content, identifies phishing indicators, performs URL security analysis, generates Explainable AI insights, calculates risk scores, and exports a professional PDF security report through an interactive Streamlit dashboard.

---

# 🎯 Why This Project?

Phishing emails remain one of the most common cybersecurity threats, often tricking users into revealing sensitive information such as passwords, banking details, and personal credentials.

This project demonstrates how Machine Learning and NLP can automatically detect phishing attempts, explain why an email is suspicious, analyze embedded URLs, and generate a complete security assessment.

---

# ✨ Key Features

- 📧 AI-powered phishing email detection
- 🧠 Neural Network based classification
- 🔤 Text preprocessing & cleaning
- 📑 TF-IDF feature extraction
- 📊 Confidence score prediction
- ⚠️ Dynamic risk score generation
- 🛡 Threat indicator detection
- 🤖 Explainable AI (XAI)
- 🌐 URL Intelligence & Security Analysis
- 📄 Downloadable PDF Security Report
- 🎨 Interactive Streamlit Dashboard
- ⚡ Modular and scalable architecture

---

# 🏗 Project Architecture

```text
                  Email Input
                       │
                       ▼
               Text Cleaning
                       │
                       ▼
            TF-IDF Vectorization
                       │
                       ▼
        Neural Network Classifier
                       │
        ┌────────┬───────────┬───────────┐
        ▼        ▼           ▼
 Threat Analysis  AI Insights  URL Intelligence
        └────────┬───────────┘
                 ▼
        Security Recommendation
                 ▼
         PDF Report Generation
```

---

# 📊 Detection Pipeline

```text
Email Input
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Feature Extraction
      │
      ▼
Neural Network Prediction
      │
      ▼
Threat Analysis
      │
      ▼
Explainable AI
      │
      ▼
URL Security Analysis
      │
      ▼
Risk Assessment
      │
      ▼
Security Recommendation
      │
      ▼
PDF Report Generation
```

---

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

---

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

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/shrinepakhredia-ui/AI-Phishing-Email-Detection-Using-NLP.git
```

### Move into Project

```bash
cd AI-Phishing-Email-Detection-Using-NLP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

# ▶️ How to Use

1. Launch the Streamlit application.
2. Paste the email content.
3. Click **Analyze Email**.
4. Review the generated:
   - Prediction Result
   - Confidence Score
   - Risk Score
   - Threat Report
   - AI Insights
   - URL Intelligence
   - Security Recommendation
5. Download the PDF Security Report.

---

# 📈 Model Performance

The project was trained using multiple Machine Learning algorithms. The Neural Network model was selected for deployment based on its overall performance.

| Model               | Status                    |
| ------------------- | ------------------------- |
| Logistic Regression | Evaluated                 |
| Naive Bayes         | Evaluated                 |
| Random Forest       | Evaluated                 |
| **Neural Network**  | ✅ Final Deployment Model |

---

# 📸 Screenshots

> Screenshots will be added after deployment.

- 🏠 Home Dashboard
- 📊 Prediction Result
- 🛡 Threat Analysis
- 🤖 AI Insights
- 🌐 URL Intelligence
- 📄 PDF Security Report

---

# 🚀 Future Enhancements

- Gmail / Outlook Integration
- Browser Extension
- REST API
- BERT / Transformer Models
- Multi-language Email Detection
- Cloud Deployment
- Real-time Email Monitoring

---

# 👨‍💻 Author

**Shrine Pakhredia**

**B.Tech – Artificial Intelligence & Machine Learning**

🔗 GitHub: https://github.com/shrinepakhredia-ui

---

<div align="center">

⭐ If you found this project useful, consider giving it a Star.

</div>
