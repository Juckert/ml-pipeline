from fastapi import FastAPI
import pickle
import pandas as pd

# Загружаем обученную модель
model = pickle.load(open("model.pkl", "rb"))

# Инициализация FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Model API is running"}

@app.post("/predict/")
def predict(input_data: dict):
    # Преобразуем входные данные в формат DataFrame
    df = pd.DataFrame(input_data)
    
    # Предсказание
    prediction = model.predict(df)
    
    # Возвращаем результат предсказания
    return {"prediction": prediction.tolist()}
