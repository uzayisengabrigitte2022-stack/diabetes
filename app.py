import pickle
import pandas as pd
import streamlit as st

# -------------------------------
# Load the trained model
# -------------------------------
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

# -------------------------------
# Prediction function
# -------------------------------
def diabete_data_prediction(weight, stress_level, blood_glucose, bmi):
    # Create DataFrame from input with only trained features
    new_data = pd.DataFrame([{
        'weight': weight,
        'stress_level': stress_level,
        'blood_glucose': blood_glucose,
        'bmi': bmi
    }])
    
    # Predict diabetes
    predicted_diabete = loaded_model.predict(new_data)
    
    return predicted_diabete[0]

# -------------------------------
# Main Streamlit app
# -------------------------------
def main():
    st.title("Diabetes Prediction App")
    st.write("Enter patient details to predict diabetes risk:")

    # Input fields for all features
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=77.7, step=0.1)
    stress_level = st.number_input("Stress Level (1-10)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    blood_glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=0.0, max_value=500.0, value=186.0, step=0.1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=22.0, step=0.1)

    # Predict button
    if st.button("Predict Diabetes"):
        # Call the prediction function
        prediction = diabete_data_prediction(weight, stress_level, blood_glucose, bmi)
        
        # Display result
        if prediction == 1 or prediction == 'Diabetes':
            st.error("The patient is predicted to have Diabetes ✅")
        else:
            st.success("The patient is predicted to NOT have Diabetes ✅")

# -------------------------------
# Run the app
# -------------------------------
if __name__ == "__main__":
    main()

