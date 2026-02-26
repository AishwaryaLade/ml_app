import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "machine_output.pkl")

print("Loading model from:", MODEL_PATH)
model = joblib.load(MODEL_PATH)


def make_prediction(features):

    columns = [
        'Injection_Temperature',
        'Injection_Pressure',
        'Cycle_Time',
        'Cooling_Time',
        'Material_Viscosity',
        'Ambient_Temperature',
        'Machine_Age',
        'Operator_Experience',
        'Maintenance_Hours',
        'Shift',
        'Machine_Type',
        'Material_Grade',
        'Day_of_Week',
        'Temperature_Pressure_Ratio',
        'Total_Cycle_Time',
        'Efficiency_Score',
        'Machine_Utilization'
    ]

    df = pd.DataFrame([features], columns=columns)

    prediction = model.predict(df)

    return prediction[0]