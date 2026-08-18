import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from backend.ml.feature_extraction import (
    extract_features,
    FEATURE_COLUMNS
)


MODEL_PATH = "models/gait_model.pkl"


def train_model():

    # Get ML-ready data from the central feature extraction layer
    X, y = extract_features()

    print("Training data shape:", X.shape)
    print("Labels:")
    print(y.value_counts())

    # Make sure there are enough classes for stratified splitting
    if y.nunique() < 2:
        raise ValueError(
            "At least 2 different activity classes are required for training."
        )

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Create model directory
    os.makedirs("models", exist_ok=True)

    # Save model + feature order
    model_data = {
        "model": model,
        "features": FEATURE_COLUMNS
    }

    joblib.dump(model_data, MODEL_PATH)

    print(f"\nModel saved to {MODEL_PATH}")

    # Test predictions
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("\n===== MODEL ACCURACY =====")
    print(f"{accuracy * 100:.2f}%")

    print("\n===== CLASSIFICATION REPORT =====")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    train_model()