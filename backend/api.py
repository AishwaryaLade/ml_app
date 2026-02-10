from fastapi import FastAPI
from pydantic import BaseModel
from backend.predict import predict

app = FastAPI()

class InputData(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def get_prediction(data: InputData):
    result = predict(data.features)
    return {"prediction": result}
