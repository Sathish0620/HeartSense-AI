"""
Visualization module for HeartSense AI.
"""

import matplotlib.pyplot as plt
import pandas as pd

from src.config import FIGURE_DIR


def plot_target_distribution(df: pd.DataFrame):
    """Plot class distribution."""

    plt.figure(figsize=(6, 4))

    df["target"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.title("Target Distribution")

    plt.xlabel("Heart Disease")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR / "target_distribution.png"
    )

    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame):
    """Plot correlation heatmap."""

    plt.figure(figsize=(12, 10))

    correlation = df.corr()

    plt.imshow(
        correlation,
        interpolation="nearest",
        aspect="auto",
    )

    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=90,
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns,
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR / "correlation_heatmap.png"
    )

    plt.close()

def plot_model_comparison(scores):
    """
    Plot model comparison chart.
    """

    import matplotlib.pyplot as plt

    names = list(scores.keys())
    values = [score * 100 for score in scores.values()]

    plt.figure(figsize=(10, 5))

    plt.bar(names, values)

    plt.xticks(rotation=20, ha="right")

    plt.ylabel("Accuracy (%)")

    plt.title("Model Comparison")

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR / "model_comparison.png"
    )

    plt.close()