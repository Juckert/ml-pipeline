import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import mlflow

# Загрузка данных
df = pd.read_csv("data.csv")
X = df.drop(columns=["target"], errors="ignore")
y = df["target"] if "target" in df else df.iloc[:, -1]

# Разделение
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Сохранение модели
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Логирование в mlflow
mlflow.set_experiment("ml_pipeline")
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("train_score", model.score(X_train, y_train))
    mlflow.log_metric("test_score", model.score(X_test, y_test))
