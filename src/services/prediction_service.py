"""
Prediction service for HeartSense AI.
"""

import pandas as pd

from src.utils import load_artifacts
from src.services.recommendation_service import RecommendationService


class PredictionService:
    """
    Service responsible for making predictions.
    """

    def __init__(self):
        self.model, self.scaler, self.imputer = load_artifacts()
        self.recommendation_service = RecommendationService()

    def predict(self, patient_data: dict):

        df = pd.DataFrame([patient_data])

        # Apply preprocessing
        df = self.imputer.transform(df)
        df = self.scaler.transform(df)

        prediction = int(self.model.predict(df)[0])

        confidence = None

        if hasattr(self.model, "predict_proba"):
            confidence = round(
                max(self.model.predict_proba(df)[0]) * 100,
                2,
            )

        result = {
            "prediction": (
                "Heart Disease Detected"
                if prediction == 1
                else "No Heart Disease"
            ),
            "label": "Positive" if prediction else "Negative",
            "risk_level": (
                "High" if prediction else "Low"
            ),
            "confidence": confidence,
        }
        recommendation = self.recommendation_service.generate(
            patient_data, prediction
        )
        result["recommendations"] = recommendation

        return result