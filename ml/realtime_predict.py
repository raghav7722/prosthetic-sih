import joblib
import pandas as pd
import time


MODEL_PATH = "models/gait_model.pkl"


def load_model():
    model_data = joblib.load(MODEL_PATH)

    model = model_data["model"]
    feature_columns = model_data["features"]

    return model, feature_columns


def predict_activity(model, feature_columns, sensor_data):

    input_data = pd.DataFrame(
        [sensor_data],
        columns=feature_columns
    )

    prediction = model.predict(input_data)

    return prediction[0]


def main():

    model, feature_columns = load_model()

    # Temporary simulated sensor readings
    sensor_readings = [

        {
            "heel_pressure": 500,
            "toe_pressure": 400,
            "thigh_pressure": 150,
            "acceleration_x": 0.02,
            "acceleration_y": -0.03,
            "acceleration_z": 9.8,
            "gyroscope_x": 0.1,
            "gyroscope_y": -0.2,
            "gyroscope_z": 0.1
        },

        {
            "heel_pressure": 550,
            "toe_pressure": 750,
            "thigh_pressure": 220,
            "acceleration_x": 0.8,
            "acceleration_y": -0.5,
            "acceleration_z": 10.2,
            "gyroscope_x": 10,
            "gyroscope_y": -5,
            "gyroscope_z": 8
        },

        {
            "heel_pressure": 850,
            "toe_pressure": 1050,
            "thigh_pressure": 350,
            "acceleration_x": 4.0,
            "acceleration_y": -3.0,
            "acceleration_z": 13.0,
            "gyroscope_x": 60,
            "gyroscope_y": -40,
            "gyroscope_z": 50
        }
    ]

    print("\n===== REAL-TIME PREDICTION SIMULATION =====")

    for sensor_data in sensor_readings:

        prediction = predict_activity(
            model,
            feature_columns,
            sensor_data
        )

        print("Predicted activity:", prediction)

        time.sleep(1)


if __name__ == "__main__":
    main()