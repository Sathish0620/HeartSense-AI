"""
Utility functions for saving and loading project artifacts.
"""

import joblib

from config import MODEL_DIR


def save_artifacts(model, scaler, imputer):
    """
    Save trained model and preprocessing objects.
    """

    joblib.dump(model, MODEL_DIR / "best_model.pkl")

    joblib.dump(scaler, MODEL_DIR / "scaler.pkl")

    joblib.dump(imputer, MODEL_DIR / "imputer.pkl")

    print("\n✅ Saved model artifacts")

    print("   • best_model.pkl")

    print("   • scaler.pkl")

    print("   • imputer.pkl")


def load_artifacts():
    """
    Load saved artifacts.
    """

    model = joblib.load(MODEL_DIR / "best_model.pkl")

    scaler = joblib.load(MODEL_DIR / "scaler.pkl")

    imputer = joblib.load(MODEL_DIR / "imputer.pkl")

    return model, scaler, imputer