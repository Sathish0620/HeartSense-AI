"""
Data preprocessing module for HeartSense AI.

This module:
- Loads the dataset
- Cleans invalid values
- Handles missing values
- Splits the data
- Scales the features
"""

import logging

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.config import DATASET_PATH


logging.basicConfig(level=logging.INFO)


def load_dataset() -> pd.DataFrame:
    """
    Load dataset from CSV.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """

    logging.info("Loading dataset...")

    df = pd.read_csv(DATASET_PATH)

    logging.info(f"Dataset loaded successfully: {df.shape}")

    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset.

    - Removes duplicate rows
    - Converts invalid placeholder values to NaN
    """

    logging.info("Cleaning dataset...")

    df = df.copy()

    # Count duplicates
    duplicates = df.duplicated().sum()
    logging.info(f"Duplicate rows found: {duplicates}")
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    logging.info(f"Dataset shape after cleaning: {df.shape}")
    
    # Replace invalid values
    df.replace(999, np.nan, inplace=True)

    return df


def preprocess_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Prepare data for machine learning.

    Returns
    -------
    X_train
    X_test
    y_train
    y_test
    scaler
    """

    logging.info("Starting preprocessing...")

    X = df.drop("target", axis=1)

    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    # Handle missing values
    imputer = SimpleImputer(strategy="median")

    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    logging.info("Preprocessing completed.")

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler,
        imputer,
    )