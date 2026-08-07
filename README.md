# 🏠 Rental Price Prediction

An end-to-end machine learning project that predicts the estimated monthly rental price of a residential property based on location, property characteristics, amenities, and tenant preferences.

## 🚀 Live Demo

🔗 **[Try the Rental Price Prediction App](https://rental-prediction-3.onrender.com)**

---

## 📌 About the Project

Finding a suitable rental price can be challenging because rental prices depend on several factors such as location, property size, BHK, furnishing, amenities, accessibility, and property age.

This project uses machine learning to learn patterns from rental property data and estimate the monthly rental price based on the details provided by the user.

The main objective was to build a complete end-to-end machine learning project rather than stopping at model training. The workflow covers data preparation, feature engineering, model training, hyperparameter tuning, model evaluation, API development, user interface creation, and cloud deployment.

---

## ✨ What the Application Does

Users can provide details such as:

- City
- City Tier
- Property Type
- BHK
- Property Size
- Bathrooms
- Balconies
- Furnishing Status
- Floor
- Total Floors
- Property Age
- Parking Availability
- Lift Availability
- Security Availability
- Gym Availability
- Swimming Pool Availability
- Power Backup
- Metro Connectivity
- Distance from City Centre
- Tenant Preference

The application processes these inputs and provides an estimated monthly rental price.

---

## 🧠 Machine Learning Workflow

The project follows a complete machine learning workflow:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Missing Value Handling
5. Feature Engineering
6. Categorical Feature Encoding
7. Multicollinearity Analysis
8. Model Training
9. Model Comparison
10. Hyperparameter Tuning
11. Cross-Validation
12. Model Evaluation
13. Final Model Selection
14. Model Serialization using Joblib
15. FastAPI Integration
16. Streamlit Interface
17. Cloud Deployment

---

## 🤖 Machine Learning Model

Different machine learning approaches were explored and evaluated during the project.

After model comparison and hyperparameter tuning, the final model was selected based on its performance on the evaluation data.

The final model achieved an **R² score of approximately 98.62%** on the evaluation dataset.

### Evaluation Metrics

The model was evaluated using:

- R² Score
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

---

## 🔌 FastAPI

The trained machine learning model is integrated with a FastAPI REST API.

The API:

- Accepts property information as JSON input
- Validates incoming data using Pydantic
- Converts the input into the format required by the model
- Generates a rental price prediction
- Returns the predicted rental price as a JSON response



## 🎯 Project Goal

The goal of this project was to build a complete **end-to-end machine learning application** that goes beyond model training.

This project demonstrates how a machine learning model can be taken from:

**Data → Model → API → Web Interface → Deployment**

Through this project, I gained practical experience in data preprocessing, machine learning, model evaluation, API development, Streamlit integration, and cloud deployment.

---

## 👨‍💻 Author

**Rohith S**

BE Computer Science & Engineering Student

Passionate about **Data Science, Machine Learning, AI, and building real-world ML applications.**

🔗 **Live Project:** https://rental-prediction-3.onrender.com
