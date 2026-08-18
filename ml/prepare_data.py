import sqlite3
import pandas as pd


DATABASE_NAME = "data/gait_data.db"


def prepare_data():

    connection = sqlite3.connect(DATABASE_NAME)

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

    # y = activity we want to predict
    y = dataframe["activity"]

    print("\n===== FEATURES (X) =====")
    print(X.head())

    print("\n===== LABELS (y) =====")
    print(y.head())

    print("\n===== X SHAPE =====")
    print(X.shape)

    print("\n===== y SHAPE =====")
    print(y.shape)

    print("\n===== ACTIVITY LABELS =====")
    print(y.value_counts())


if __name__ == "__main__":
    prepare_data()