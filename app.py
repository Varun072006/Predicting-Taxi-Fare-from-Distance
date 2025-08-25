import streamlit as st
import numpy as np
import pickle  

with open("taxi_fare_model.sav", "rb") as f:
    model = pickle.load(f)

st.title("🚕 Taxi Fare Prediction")

distance = st.number_input("Enter Distance (km):", min_value=0.0, value=15.0, step=0.5)

if st.button("Predict Fare"):
    predicted_fare = model.predict([[distance]])[0]
    st.success(f"Predicted Fare for {distance} km: ₹ {predicted_fare:.2f}")