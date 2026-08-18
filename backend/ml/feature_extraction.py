import pandas as pd

from backend.database.db import get_connection


FEATURE_COLUMNS = [
    "heel_pressure",
    "acceleration_x",
    "acceleration_y",
    "acceleration_z",
    "gyroscope_x",
    "gyroscope_y",
    "gyroscope_z"
]


def load_gait_data():
    """
    Load gait data from the central project database.
    """

    connection = get_connection()

    query = """
        SELECT
            id,
            timestamp,
            heel_pressure,
            acceleration_x,
            acceleration_y,
            acceleration_z,
            gyroscope_x,
            gyroscope_y,
            gyroscope_z,
            activity
        FROM gait_data
    """

    dataframe = pd.read_sql_query(query, connection)

    connection.close()

    return dataframe


def extract_features():
    """
    Prepare ML features and labels from gait data.

    Only rows with an activity label are used for training.
    """

    dataframe = load_gait_data()

    if dataframe.empty:
        raise ValueError("No gait data found in the database.")

    # Training requires known activity labels.
    dataframe = dataframe.dropna(subset=["activity"])

    if dataframe.empty:
        raise ValueError(
            "No labeled gait data found. "
            "Add activity labels before training the model."
        )

    X = dataframe[FEATURE_COLUMNS].copy()
    y = dataframe["activity"].copy()

    return X, y


if __name__ == "__main__":

    X, y = extract_features()

    print("\n===== ML FEATURES =====")
    print(X.head())

    print("\n===== LABELS =====")
    print(y.head())

    print("\n===== FEATURE SHAPE =====")
    print(X.shape)

    print("\n===== LABEL DISTRIBUTION =====")
    print(y.value_counts())