# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Load dataset
df = pd.read_csv("data/messages.csv")

X = df["message"]
y = df["label"]

# Vectorization
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train with class balancing
model = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/scam_detector.joblib")
joblib.dump(vectorizer, "model/vectorizer.joblib")
print("Model trained and saved successfully.")
