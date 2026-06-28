from src.services.prediction_service import PredictionService

service = PredictionService()

patient = {
    "age": 52,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 230,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.2,
    "slope": 2,
    "ca": 0,
    "thal": 2,
}

result = service.predict(patient)

print("\n========== HeartSense AI ==========\n")

for key, value in result.items():
    print(f"{key:<15}: {value}")