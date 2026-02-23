from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Independent R&D: Loading the localized brain artifact [cite: 2026-02-23]
model = joblib.load('models/fraud_detector_v1.pkl')

@app.get("/")
def read_root():
    return {
        "status": "Independent R&D Fraud Detection API Online",
        "phase": 9,
        "environment": "Native Linux"
    }

@app.get("/predict")
def predict_fraud():
    # Independent R&D: Simulating a real-time transaction request [cite: 2026-02-23]
    df = pd.read_csv('input-data/raw/balanced_creditcard.csv')
    sample = df.sample(1).drop('Class', axis=1)
    
    prediction = model.predict(sample)[0]
    result = "FRAUD" if prediction == 1 else "NORMAL"
    
    return {
        "prediction": result,
        "model_version": "v1.0"
    }
