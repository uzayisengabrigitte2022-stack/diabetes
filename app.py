# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 19:30:25 2025

@author: user
"""

import pickle
import pandas as pd
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('diabetes_data.sav', 'rb'))

# Prediction function
def diabete_data_prediction(weight, stress_level, blood_glucose, bmi, risk_score):
    # Create DataFrame from input
    new_data = pd.DataFrame([{
        'weight': 70,
        'stress_level': 5,
        'blood_glucose': 160,
        'bmi': 28
    }])
    print(new_data)
    
    # Predict diabete
    predicted_diabete = loaded_model.predict(new_data)
    
    # Return the prediction
    return predicted_diabete[0]

# Main Streamlit app
def main():
    st.title("diabete Prediction")

    # Input fields for all features
weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
stress_level = st.number_input("Stress Level (1-10)", min_value=0.0, max_value=10.0, value=5.0)
blood_glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=0.0, max_value=500.0, value=120.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=25.0)
            # Create a DataFrame for prediction
if st.button("Predict Diabetes"):
    # Indented block starts here
    

    input_data = pd.DataFrame([{
        'weight': weight,
        'stress_level': stress_level,
        'blood_glucose': blood_glucose,
        'bmi': bmi
    }])
    
    prediction = loaded_model.predict(input_data)[0]

    if prediction == 1 or prediction == 'Diabetes':
        st.error("The patient is predicted to have Diabetes ")
    else:
        st.success("The patient is predicted to NOT have Diabetes ")

if __name__ == "__main__":
    main()
