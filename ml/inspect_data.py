import sqlite3
import pandas as pd


DATABASE_NAME = "data/gait_data.db"


def inspect_dataset():

    connection = sqlite3.connect(DATABASE_NAME)

    query = "SELECT * FROM gait_data"

    dataframe = pd.read_sql_query(query, connection)

    connection.close()

    print("\n===== DATASET =====")
    print(dataframe)

    print("\n===== DATASET SHAPE =====")
    print(dataframe.shape)

    print("\n===== ACTIVITY COUNTS =====")
    print(dataframe["activity"].value_counts())

    print("\n===== MISSING VALUES =====")
    print(dataframe.isnull().sum())

    print("\n===== STATISTICS =====")
    print(dataframe.describe())


if __name__ == "__main__":
    inspect_dataset()