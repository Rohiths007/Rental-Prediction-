# 🏠 Rental Price Prediction

An end-to-end Machine Learning project that predicts rental prices using property, location, and amenity-related features.

The project covers the complete workflow from data preprocessing and model training to model saving, FastAPI deployment, and a Streamlit user interface.

---

## 🚀 Project Overview

The goal of this project is to build a machine learning system that can estimate the rental price of a property based on different property characteristics.

The project includes:

- Data preprocessing and feature engineering
- Categorical feature encoding
- Numerical feature handling
- Machine Learning model training
- Hyperparameter tuning
- Model evaluation
- XGBoost model deployment
- FastAPI REST API
- Streamlit interactive interface
- Databricks ML pipeline
- Saved `.joblib` model for inference

---

## 🧠 Machine Learning Pipeline

The overall workflow is:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train / Test Split
     ↓
Preprocessing
     ↓
Categorical Encoding
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Best XGBoost Model
     ↓
Save Model (.joblib)
     ↓
FastAPI
     ↓
Streamlit Interface
