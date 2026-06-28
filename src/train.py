"""
Model training module.

Trains multiple machine learning models
and compares their performance.
"""

import logging

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


logging.basicConfig(level=logging.INFO)


def train_models(X_train, X_test, y_train, y_test):
    """
    Train multiple models and compare accuracy.
    """

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),

        "KNN": KNeighborsClassifier(n_neighbors=7),

        "Decision Tree": DecisionTreeClassifier(random_state=42),

        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
        ),

        "Naive Bayes": GaussianNB(),

        "Support Vector Machine": SVC(probability=True, random_state=42,),

        "MLP Neural Network": MLPClassifier(
            hidden_layer_sizes=(32, 16),
            max_iter=500,
            random_state=42,
        ),
    }

    scores = {}

    best_model = None
    best_score = 0

    logging.info("Training models...\n")

    for name, model in models.items():

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(y_test, prediction)

        scores[name] = accuracy

        print(f"{name:<25} : {accuracy:.4f}")

        if accuracy > best_score:
            best_score = accuracy
            best_model = model

    print("\nBest Model:", type(best_model).__name__)
    print("Best Accuracy:", round(best_score * 100, 2), "%")
    best_predictions = best_model.predict(X_test)

    return best_model, best_predictions, scores
    