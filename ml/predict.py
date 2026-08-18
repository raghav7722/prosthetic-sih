import joblib
import pandas as pd


MODEL_PATH = "models/gait_model.pkl"


def predict_activity():

    # Load the trained model
    model_data = joblib.load(MODEL_PATH)

    model = model_data["model"]
    feature_columns = model_data["features"]

    # Example new sensor readings
    sensor_data = {
        "heel_pressure": 550,
        "toe_pressure": 750,
        "thigh_pressure": 220,

        "acceleration_x": 0.8,
        "acceleration_y": -0.5,
        "acceleration_z": 10.2,

        "gyroscope_x": 10,
        "gyroscope_y": -5,
        "gyroscope_z": 8
    }

    # Convert sensor data into DataFrame
    input_data = pd.DataFrame(
        [sensor_data],
        columns=feature_columns
    )

    # Predict activity
    prediction = model.predict(input_data)

    print("\n===== PREDICTION =====")
    print("Predicted activity:", prediction[0])


if __name__ == "__main__":
    predict_activity()