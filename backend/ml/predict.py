import os
import joblib
import pandas as pd


MODEL_PATH = "models/gait_model.pkl"


def load_model():
    """Load the trained gait classification model."""

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Trained model not found. Train the model first."
        )

    model_data = joblib.load(MODEL_PATH)

    return model_data["model"], model_data["features"]


def prepare_sensor_data(data, feature_columns):
    """
    Convert incoming ESP32 JSON into the feature format
    expected by the ML model.
    """

    sensors = data["sensors"]

    feature_data = {
        "heel_pressure": sensors["fsr1"],
        "acceleration_x": sensors["ax"],
        "acceleration_y": sensors["ay"],
        "acceleration_z": sensors["az"],
        "gyroscope_x": sensors["gx"],
        "gyroscope_y": sensors["gy"],
        "gyroscope_z": sensors["gz"]
    }

    dataframe = pd.DataFrame(
        [[feature_data[column] for column in feature_columns]],
        columns=feature_columns
    )

    return dataframe


def predict_gait(data):
    """
    Predict the gait/activity from one sensor reading.
    """

    model, feature_columns = load_model()

    sensor_features = prepare_sensor_data(
        data,
        feature_columns
    )

    prediction = model.predict(sensor_features)[0]

    result = {
        "prediction": prediction
    }

    # Return probability/confidence when supported
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(sensor_features)[0]
        confidence = max(probabilities)

        result["confidence"] = float(confidence)

    return result