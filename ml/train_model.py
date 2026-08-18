# 

import sqlite3
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


DATABASE_NAME = "data/gait_data.db"


def train_model():

    # Connect to database
    connection = sqlite3.connect(DATABASE_NAME)

    # Load data
    query = "SELECT * FROM gait_data"
    dataframe = pd.read_sql_query(query, connection)

    connection.close()

    # Features used by the ML model
    feature_columns = [
        "heel_pressure",
        "toe_pressure",
        "thigh_pressure",
        "acceleration_x",
        "acceleration_y",
        "acceleration_z",
        "gyroscope_x",
        "gyroscope_y",
        "gyroscope_z"
    ]

    # X = sensor data
    X = dataframe[feature_columns]

    # y = activity label
    y = dataframe["activity"]

    # Split dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Create Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)

    # Create models folder if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Save model + feature order
    model_data = {
        "model": model,
        "features": feature_columns
    }

    joblib.dump(
        model_data,
        "models/gait_model.pkl"
    )

    print("\nTrained model saved to models/gait_model.pkl")

    # Make predictions on test data
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("\n===== MODEL ACCURACY =====")
    print(f"{accuracy * 100:.2f}%")

    # Detailed performance
    print("\n===== CLASSIFICATION REPORT =====")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    train_model()