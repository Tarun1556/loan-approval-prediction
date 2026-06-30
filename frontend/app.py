import streamlit as st
import pickle
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "backend" / "model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("🏦 Loan Approval Prediction System")
st.markdown("Enter applicant details to predict loan approval.")
st.sidebar.header("Model Information")
st.sidebar.write("Algorithm: Random Forest")
st.sidebar.write("Features:")
st.sidebar.write("- Annual Income")
st.sidebar.write("- CIBIL Score")
st.sidebar.write("- Loan Amount")
st.markdown("---")
st.caption("Built using Python, Scikit-Learn and Streamlit")

income = st.number_input("Annual Income", min_value=0)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=750
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

if st.button("Predict"):

    data = np.array([[income, cibil_score, loan_amount]])

    prediction = model.predict(data)

    if prediction[0] == 0:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")