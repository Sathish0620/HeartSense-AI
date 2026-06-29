from fastapi import FastAPI
from app.schemas import Patient
from src.services.prediction_service import PredictionService
from fastapi.middleware.cors import CORSMiddleware
from app.config import ALLOWED_ORIGINS
service = PredictionService()
app = FastAPI(
    title="HeartSense AI API",
    description="""Heart disease prediction API powered by Machine Learning.

        Features

        • Heart disease prediction

        • Confidence score

        • Personalized recommendations

        • REST API

        Built using FastAPI + Scikit-Learn.
        """,
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {
        "message": "Welcome to HeartSense AI",
        "status": "Running"
    }
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": "HeartSense AI API",
        "version": "1.0.0"
    }


@app.post("/predict")
def predict(patient: Patient):

    result = service.predict(patient.model_dump())

    return result