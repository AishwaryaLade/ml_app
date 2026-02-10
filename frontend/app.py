import streamlit as st
import sys
sys.path.append("backend")

from predict import predict

st.title("Manufacturing Prediction App")

st.write("Enter input values")

inputs = []
for i in range(13):   # change feature count
    val = st.number_input(f"Feature {i+1}")
    inputs.append(val)

if st.button("Predict"):
    result = predict(inputs)
    st.success(f"Prediction: {result:.2f}")
