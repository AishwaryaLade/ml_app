import joblib

MODEL_PATH = "machine_output.pkl"

def load_model():
    model = joblib.load(MODEL_PATH)
    return model
