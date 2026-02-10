import torch
import numpy as np
from model import load_model

MODEL_PATH = "backend/multilinear_model.pth"
INPUT_DIM = 13   # change to your feature count

model = load_model(INPUT_DIM, MODEL_PATH)

def predict(data):
    x = torch.FloatTensor([data])
    with torch.no_grad():
        pred = model(x)
    return pred.item()
