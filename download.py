import pandas as pd
from sklearn.datasets import load_diabetes

# Загрузка данных и сохранение в CSV
data = load_diabetes(as_frame=True)
df = data.frame
df.to_csv("data.csv", index=False)
print("Data downloaded and saved to data.csv")
