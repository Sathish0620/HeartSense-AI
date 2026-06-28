"""
Prediction module for HeartSense AI.
"""

import pandas as pd

from src.utils import load_artifacts


def predict_patient(patient_data: dict):
    """
    Predict heart disease risk for a single patient.

    Parameters
    ----------
    patient_data : dict
        Dictionary containing patient information.

    Returns
    -------
    tuple
        prediction, confidence
    """

    model, scaler, imputer = load_artifacts()

    df = pd.DataFrame([patient_data])

    # Apply the same preprocessing used during training
    df = imputer.transform(df)
    df = scaler.transform(df)

    prediction = model.predict(df)[0]

    confidence = None

    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(df).max()

    return prediction, confidence