import sqlite3

DATABASE_NAME = "data/gait_data.db"


def read_gait_data():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM gait_data")

    rows = cursor.fetchall()

    connection.close()

    print("\nGait Data:")
    print("-" * 120)

    for row in rows:
        print(row)


if __name__ == "__main__":
    read_gait_data()