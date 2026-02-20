import streamlit as st
import requests

st.title("Manufacturing Output Prediction")

st.write("Enter machine parameters below:")

features = []

# -----------------------------
# Numerical Inputs
# -----------------------------

injection_temperature = st.number_input("Injection_Temperature", value=0.0)
injection_pressure = st.number_input("Injection_Pressure", value=0.0)
cycle_time = st.number_input("Cycle_Time", value=0.0)
cooling_time = st.number_input("Cooling_Time", value=0.0)
material_viscosity = st.number_input("Material_Viscosity", value=0.0)
ambient_temperature = st.number_input("Ambient_Temperature", value=0.0)
machine_age = st.number_input("Machine_Age", value=0.0)
operator_experience = st.number_input("Operator_Experience", value=0.0)
maintenance_hours = st.number_input("Maintenance_Hours", value=0.0)

# -----------------------------
# Categorical Inputs
# -----------------------------

shift = st.selectbox("Shift", ["Morning", "Evening", "Night"])

machine_type = st.selectbox(
    "Machine_Type",
    ["Type_A", "Type_B", "Type_C"]
)

material_grade = st.selectbox(
    "Material_Grade",
    ["Grade_1", "Grade_2", "Grade_3"]
)

day_of_week = st.selectbox(
    "Day_of_Week",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

# -----------------------------
# Engineered Numerical Inputs
# -----------------------------

temperature_pressure_ratio = st.number_input("Temperature_Pressure_Ratio", value=0.0)
total_cycle_time = st.number_input("Total_Cycle_Time", value=0.0)
efficiency_score = st.number_input("Efficiency_Score", value=0.0)
machine_utilization = st.number_input("Machine_Utilization", value=0.0)

# -----------------------------
# Arrange Features in EXACT Training Order
# -----------------------------

features = [
    injection_temperature,
    injection_pressure,
    cycle_time,
    cooling_time,
    material_viscosity,
    ambient_temperature,
    machine_age,
    operator_experience,
    maintenance_hours,
    shift,
    machine_type,
    material_grade,
    day_of_week,
    temperature_pressure_ratio,
    total_cycle_time,
    efficiency_score,
    machine_utilization
]

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("Predict"):
    url = "http://127.0.0.1:8000/predict"
    data = {"features": features}

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()["prediction"]
            st.success(f"Predicted Output: {result}")
        else:
            st.error(f"Backend Error: {response.text}")

    except Exception as e:
        st.error(f"Cannot connect to backend server: {e}")