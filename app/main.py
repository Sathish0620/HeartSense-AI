from fastapi import FastAPI
from app.schemas import Patient
from src.services.prediction_service import PredictionService

service = PredictionService()
app = FastAPI(
    title="HeartSense AI API",
    description="Heart Disease Prediction using Machine Learning",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to HeartSense AI",
        "status": "Running"
    }

@app.post("/predict")
def predict(patient: Patient):

    result = service.predict(patient.model_dump())

    return result