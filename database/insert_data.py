import sqlite3

DATABASE_NAME = "data/gait_data.db"


def insert_sample_data():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    sample_data = (
        0.001,      # timestamp
        500.0,      # heel pressure
        800.0,      # toe pressure
        120.0,      # thigh pressure
        0.42,       # acceleration X
        0.13,       # acceleration Y
        9.81,       # acceleration Z
        2.4,        # gyroscope X
        0.8,        # gyroscope Y
        1.2,        # gyroscope Z
        "walking"   # activity
    )

    cursor.execute("""
        INSERT INTO gait_data (
            timestamp,
            heel_pressure,
            toe_pressure,
            thigh_pressure,
            acceleration_x,
            acceleration_y,
            acceleration_z,
            gyroscope_x,
            gyroscope_y,
            gyroscope_z,
            activity
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_data)

    connection.commit()
    connection.close()

    print("Sample gait data inserted successfully.")


if __name__ == "__main__":
    insert_sample_data()