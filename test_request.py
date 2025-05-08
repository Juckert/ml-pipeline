import requests
import json

# Пример одного вектора признаков
data = {
    "features": [
        [0.03807591, 0.05068014, 0.06169621, 0.02187237, -0.0442235,
         -0.03482076, 0.01764627, -0.01861207, -0.00101283, -0.00074299]
    ]
}

try:
    print("Sending test request...")
    response = requests.post("http://127.0.0.1:8000/predict/", json=data)
    response.raise_for_status()
    
    print("Status code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))
    
    prediction = response.json().get("prediction")
    if prediction is not None:
        print("Prediction received successfully!")
    else:
        print("Error: No prediction in response")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {str(e)}")