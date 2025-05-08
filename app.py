from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Инициализация API
app = FastAPI()

# Загрузка модели
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Схема входных данных
class InputData(BaseModel):
    features: list

@app.post("/predict/")
def predict(data: InputData):
    prediction = model.predict(data.features)
    return {"prediction": prediction.tolist()}

