# 🛡️ ScamShield — AI-Powered Scam Detector

> Real-time scam detection & AI-powered explanation engine using NLP and Gen AI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![ML](https://img.shields.io/badge/ML-Random%20Forest%20%2B%20TF--IDF-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-yellow)

---

## 📌 About
ScamShield is a chatbot that detects whether a message is a scam using 
Machine Learning (Random Forest + TF-IDF) with a FastAPI backend 
and a dark-themed chat frontend.

---

## 🚀 Features
- 🔍 Real-time scam message detection
- 🤖 ML-powered classification (Random Forest + TF-IDF)
- 💡 Google Gemini AI explanations
- 📊 Live risk score (0–100)
- ⚡ FastAPI backend with instant response

---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| ML Model | Random Forest + TF-IDF |
| Backend | FastAPI (Python) |
| Frontend | HTML, CSS, JavaScript |
| Gen AI | Google Gemini API |
| Data | Labelled SMS/message dataset |

---

## 📁 Project Structure

```
ScamShield-Chatbot/
├── backend/
│   ├── __init__.py
│   ├── main.py        # FastAPI app
│   ├── model.py       # Prediction logic
│   └── schemas.py     # Pydantic I/O schemas
├── data/
│   └── messages.csv   # Labelled training dataset
├── model/
│   ├── scam_detector.joblib
│   └── vectorizer.joblib
├── frontend/
│   └── index.html     # Chatbot UI
├── train_model.py     # Train and save the model
├── requirements.txt
└── README.md
```

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python train_model.py
```

### 3. Start the backend
```bash
uvicorn backend.main:app --reload
```

### 4. Open the frontend
Open `frontend/index.html` in your browser.

---

## 👩‍💻 Developed By
**Chahat Jain** — Department of Artificial Intelligence & Machine Learning

*Project Competition — Building Intelligent Chatbot*
