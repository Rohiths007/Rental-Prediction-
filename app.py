from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(title="Rental Price Prediction API")

# Load trained pipeline
model = joblib.load("xgb_model.joblib")


@app.get("/")
def home():
    return {
        "message": "Rental Price Prediction API is running"
    }


@app.post("/predict")
def predict(data: dict):

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_rent": float(prediction)
    }