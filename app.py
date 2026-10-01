import streamlit as st
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Height to Weight Prediction")

st.write(
    "Enter your height and the trained Machine Learning model "
    "will predict the corresponding weight."
)

# User input
height = st.number_input(
    "Enter Height (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0,
    step=1.0
)

if st.button("Predict Weight"):

    # Same column name used during training
    input_data = pd.DataFrame({
        "Height": [height]
    })

    # Same preprocessing used during training
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    st.success(
        f"Predicted Weight: {prediction[0]:.2f} kg"
    )