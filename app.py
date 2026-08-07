from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import pandas as pd
import joblib

app = FastAPI(
    title="Rental Price Prediction API",
    description="API for predicting monthly rental prices",
    version="1.0.0"
)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "details": exc.errors()
        }
    )
# Load model
model = joblib.load("xgb_model.joblib")


# -----------------------------
# Pydantic Input Schema
# -----------------------------

class RentalInput(BaseModel):

    city: str
    city_tier: int = Field(ge=1, le=3)

    property_type: str

    bhk: int = Field(ge=1, le=10)
    size_sqft: float = Field(gt=0)
    bathrooms: int = Field(ge=1, le=10)
    balconies: int = Field(ge=0, le=10)

    furnishing: str

    floor: int = Field(ge=0)
    total_floors: int = Field(ge=1)

    age_of_property_years: int = Field(ge=0)

    has_parking: int = Field(ge=0, le=1)
    has_lift: int = Field(ge=0, le=1)
    has_security: int = Field(ge=0, le=1)
    has_gym: int = Field(ge=0, le=1)
    has_pool: int = Field(ge=0, le=1)
    has_power_backup: int = Field(ge=0, le=1)
    near_metro: int = Field(ge=0, le=1)

    distance_to_city_center_km: float = Field(ge=0)

    tenant_preference: str


# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Rental Price Prediction API is running"
    }


# -----------------------------
# Prediction Route
# -----------------------------

@app.post("/predict")
def predict_rent(data: RentalInput):

    # Convert Pydantic object → Dictionary
    input_data = data.model_dump()

    # Dictionary → DataFrame
    input_df = pd.DataFrame([input_data])

    # Prediction
    prediction = model.predict(input_df)

    predicted_rent = float(prediction[0])

    return {
        "predicted_rent": round(predicted_rent, 2)
    }