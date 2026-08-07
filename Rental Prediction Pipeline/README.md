# 🚀 Final Model Pipeline

This folder contains the final trained machine learning model used for the Rental Price Prediction application.

## 📂 Files

- `Rental_Prediction_Pipeline.ipynb` — Final model training and pipeline notebook.
- `xgb_model.joblib` — Serialized final XGBoost model used for making rental price predictions.

## 🧠 Final Model

The final XGBoost model was trained after data preprocessing, feature engineering, model evaluation, and hyperparameter tuning.

The trained model was saved using **Joblib** so it can be loaded directly during API prediction without retraining the model.

## 🔄 Usage

```text
Input Property Details
        ↓
Preprocessing
        ↓
Final XGBoost Model
        ↓
Rental Price Prediction
