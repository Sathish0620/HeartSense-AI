from preprocessing import (
    load_dataset,
    clean_dataset,
    preprocess_data,
)

from train import train_models
from visualization import (
    plot_target_distribution,
    plot_correlation_heatmap,
)
from evaluate import evaluate_model
from utils import save_artifacts

def main():

    dataset = load_dataset()
    dataset = clean_dataset(dataset)
    plot_target_distribution(dataset)
    plot_correlation_heatmap(dataset)

    X_train, X_test, y_train, y_test, scaler, imputer = preprocess_data(dataset)

    # Train all models
    best_model, predictions, scores = train_models(
        X_train,
        X_test,
        y_train,
        y_test,
    )
    evaluate_model(
        best_model,
        X_test,
        y_test,
    )
    save_artifacts(best_model, scaler, imputer)
    print("=" * 50)
    print("HeartSense AI")
    print("=" * 50)

    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    print("\nDataset Ready for Model Training.")


if __name__ == "__main__":
    main()