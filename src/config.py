"""
Project configuration file.

Contains all directory paths used throughout the project.
"""

from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset directory
DATA_DIR = BASE_DIR / "dataset"

# Models directory
MODEL_DIR = BASE_DIR / "models"

# Reports directory
REPORT_DIR = BASE_DIR / "reports"

# Figures directory
FIGURE_DIR = REPORT_DIR / "figures"

# Dataset file
DATASET_PATH = DATA_DIR / "Heart_dataset.csv"

# Saved model path
MODEL_PATH = MODEL_DIR / "best_model.pkl"

# Create directories if they don't exist
MODEL_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
FIGURE_DIR.mkdir(exist_ok=True)