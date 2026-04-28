# backend/model.py
import joblib
import numpy as np
import re
import httpx

# Load trained components
try:
    model = joblib.load("model/scam_detector.joblib")
    vectorizer = joblib.load("model/vectorizer.joblib")
except Exception as e:
    raise RuntimeError(f"Failed to load model or vectorizer: {e}")

# Common scam indicators to detect and report
SCAM_INDICATORS = [
    (r'\b(won|winner|prize|reward|congratulations)\b', "Claims of winning prizes"),
    (r'\b(urgent|immediately|act now|limited time|expires)\b', "Creates false urgency"),
    (r'\b(click here|verify now|confirm your|update your)\b', "Suspicious call-to-action"),
    (r'\b(free|guaranteed|no experience|100%)\b', "Unrealistic promises"),
    (r'\b(bank|paypal|amazon|netflix|google|irs|social security)\b', "Impersonates trusted brand/authority"),
    (r'\b(password|account|credit card|social security|personal details)\b', "Requests sensitive information"),
    (r'(http[s]?://|www\.)\S+', "Contains suspicious link"),
    (r'\$[\d,]+', "Mentions large monetary amounts"),
    (r'\b(lottery|inheritance|grant|refund|cashback)\b', "Too-good-to-be-true financial offer"),
]

def detect_indicators(message: str) -> list:
    found = []
    for pattern, label in SCAM_INDICATORS:
        if re.search(pattern, message, re.IGNORECASE):
            found.append(label)
    return found

def generate_ai_explanation(message, risk, risk_percentage, indicators):
    try:
        indicator_text = ", ".join(indicators) if indicators else "none"
        prompt = f"""You are ScamShield. Analyze this message in 2-3 sentences.
Message: "{message}"
Risk: {"HIGH - likely scam" if risk == "high" else "LOW - likely safe"}
Risk Score: {risk_percentage}%
Red flags: {indicator_text}
Give a short friendly explanation of whether this is a scam and why."""

        response = httpx.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            params={"key": "AIzaSyAnL1qEuvh_R-RL_zyrAc5nrrh6jTWTAGM"},
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=10.0
        )
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception:
        if risk == "high":
            return f"This message shows strong scam signs with {risk_percentage}% risk. Do not click any links or share personal information."
        else:
            return f"This message appears legitimate with only {risk_percentage}% risk. No major scam patterns detected."
def predict_message(message: str) -> dict:
    vectorized = vectorizer.transform([message])
    prediction = model.predict(vectorized)[0]
    proba_arr = model.predict_proba(vectorized)[0]
    classes = model.classes_

    high_idx = list(classes).index("high") if "high" in classes else 0
    high_proba = proba_arr[high_idx]

    confidence = float(np.max(proba_arr))
    risk_percentage = round(high_proba * 100, 1)
    indicators = detect_indicators(message)

    # GenAI explanation from Claude
    reason = generate_ai_explanation(message, prediction, risk_percentage, indicators)

    return {
        "risk": prediction,
        "confidence": round(confidence, 2),
        "reason": reason,
        "risk_percentage": risk_percentage,
        "indicators": indicators,
    }
