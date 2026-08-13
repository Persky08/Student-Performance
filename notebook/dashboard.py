import streamlit as st
import requests

st.title("Student Performance Prediction Dashboard")

st.write("Enter student details below to predict the final grade.")

# Input fields
reason = st.selectbox("Reason for choosing school", ["course", "home", "reputation", "other"])
schoolsup = st.selectbox("School Support", ["yes", "no"])
G1 = st.slider("G1 (First Period Grade)", 0, 20, 10)
G2 = st.slider("G2 (Second Period Grade)", 0, 20, 10)
absences = st.slider("Absences", 0, 100, 5)
age = st.slider("Age", 10, 22, 16)
famrel = st.slider("Family Relationship Quality (1 = very bad, 5 = excellent)", 1, 5, 3)
health = st.slider("Health Status (1 = very bad, 5 = excellent)", 1, 5, 3)

if st.button("Predict Final Grade"):
    payload = {
        "reason": reason,
        "schoolsup": schoolsup,
        "G1": G1,
        "G2": G2,
        "absences": absences,
        "age": age,
        "famrel": famrel,
        "health": health
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        result = response.json()

        st.success(f"Predicted Final Grade: {result['predicted_final_grade']:.2f}")

    except Exception as e:
        st.error("Could not connect to the API. Make sure the Docker container is running.")
        st.error(e)
