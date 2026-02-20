from fastapi import FastAPI
from pydantic import BaseModel
from backend.predict import make_prediction

app = FastAPI()

class InputData(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "ML Prediction API Running"}

@app.post("/predict")
def predict(data: InputData):
    result = make_prediction(data.features)
    return {"prediction": result}
