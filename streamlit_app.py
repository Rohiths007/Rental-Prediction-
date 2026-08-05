import streamlit as st
import requests

st.set_page_config(
    page_title="Rental Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Rental Price Prediction")
st.write("Enter property details to estimate the monthly rental price.")

# -----------------------------
# Property Details
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox(
        "City",
        ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"]
    )

    city_tier = st.selectbox(
        "City Tier",
        [1, 2, 3]
    )

    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Independent House", "Villa", "Studio", "PG/Co-living"]
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=10,
        value=2
    )

    size_sqft = st.number_input(
        "Size (sqft)",
        min_value=100,
        max_value=10000,
        value=1000
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    balconies = st.number_input(
        "Balconies",
        min_value=0,
        max_value=10,
        value=1
    )

    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )

    floor = st.number_input(
        "Floor",
        min_value=0,
        max_value=100,
        value=3
    )

    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=100,
        value=5
    )

with col2:

    age_of_property_years = st.number_input(
        "Age of Property (Years)",
        min_value=0,
        max_value=100,
        value=5
    )

    has_parking = st.selectbox(
        "Parking Available?",
        ["Yes", "No"]
    )

    has_lift = st.selectbox(
        "Lift Available?",
        ["Yes", "No"]
    )

    has_security = st.selectbox(
        "Security Available?",
        ["Yes", "No"]
    )

    has_gym = st.selectbox(
        "Gym Available?",
        ["Yes", "No"]
    )

    has_pool = st.selectbox(
        "Swimming Pool?",
        ["Yes", "No"]
    )

    has_power_backup = st.selectbox(
        "Power Backup?",
        ["Yes", "No"]
    )

    near_metro = st.selectbox(
        "Near Metro?",
        ["Yes", "No"]
    )

    distance_to_city_center_km = st.number_input(
        "Distance from City Centre (km)",
        min_value=0.0,
        max_value=100.0,
        value=5.0
    )

    tenant_preference = st.selectbox(
        "Tenant Preference",
        ["Family", "Bachelor", "Anyone"]
    )


# -----------------------------
# Convert Yes / No → 1 / 0
# -----------------------------

def yes_no(value):
    return 1 if value == "Yes" else 0


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Rent", use_container_width=True):

    data = {
        "city": city,
        "city_tier": city_tier,
        "property_type": property_type,
        "bhk": bhk,
        "size_sqft": size_sqft,
        "bathrooms": bathrooms,
        "balconies": balconies,
        "furnishing": furnishing,
        "floor": floor,
        "total_floors": total_floors,
        "age_of_property_years": age_of_property_years,
        "has_parking": yes_no(has_parking),
        "has_lift": yes_no(has_lift),
        "has_security": yes_no(has_security),
        "has_gym": yes_no(has_gym),
        "has_pool": yes_no(has_pool),
        "has_power_backup": yes_no(has_power_backup),
        "near_metro": yes_no(near_metro),
        "distance_to_city_center_km": distance_to_city_center_km,
        "tenant_preference": tenant_preference
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction successful!")

            predicted_rent = result["predicted_rent"]

            st.metric(
                "Estimated Monthly Rent",
                f"₹{predicted_rent:,.0f}"
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI server is not running. "
            "Please start FastAPI first."
        )