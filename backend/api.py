# backend/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from predict import make_prediction
import os

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI()

# -----------------------------
# CORS setup for frontend
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Input model
# -----------------------------
class InputData(BaseModel):
    features: list

# -----------------------------
# Home route
# -----------------------------
@app.get("/")
def home():
    return {"message": "ML Prediction API Running"}

# -----------------------------
# Predict endpoint
# -----------------------------
@app.post("/predict")
def predict(data: InputData):
    result = make_prediction(data.features)
    return {"prediction": result}

# -----------------------------
# Favicon route to prevent 404 logs
# -----------------------------
@app.get("/favicon.ico")
def favicon():
    # Path to favicon.ico (optional, can leave empty if you don't have one)
    favicon_path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    else:
        return {}  # return empty JSON if favicon is not present