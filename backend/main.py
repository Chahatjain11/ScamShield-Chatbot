# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import TextInput, TextOutput
from backend.model import predict_message

app = FastAPI(
    title="ScamShield API",
    description="AI-powered scam detection for messages",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ScamShield API is running"}

@app.post("/analyze-text", response_model=TextOutput)
def analyze_text(input_data: TextInput):
    result = predict_message(input_data.message)
    return result
