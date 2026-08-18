import sqlite3


DATABASE_NAME = "data/gait_data.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gait_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,

            heel_pressure REAL,
            toe_pressure REAL,
            thigh_pressure REAL,

            acceleration_x REAL,
            acceleration_y REAL,
            acceleration_z REAL,

            gyroscope_x REAL,
            gyroscope_y REAL,
            gyroscope_z REAL,

            activity TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Gait database created successfully.")


if __name__ == "__main__":
    create_database()