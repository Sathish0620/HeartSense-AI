"""
Visualization module for HeartSense AI.
"""

import matplotlib.pyplot as plt
import pandas as pd

from config import FIGURE_DIR


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