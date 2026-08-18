import sqlite3
import json
import serial
import time


DATABASE_NAME = "data/gait_data.db"

SERIAL_PORT = "/dev/cu.YOUR_ESP32_PORT"
BAUD_RATE = 115200


def connect_esp32():

    connection = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=1
    )

    time.sleep(2)

    print("ESP32 connected.")

    return connection


def save_sensor_data(cursor, sensor_data, activity, timestamp):

    cursor.execute("""
        INSERT INTO gait_data (
            timestamp,
            heel_pressure,
            acceleration_x,
            acceleration_y,
            acceleration_z,
            gyroscope_x,
            gyroscope_y,
            gyroscope_z,
            activity
        )
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        sensor_data["heel_pressure"],
        sensor_data["acceleration_x"],
        sensor_data["acceleration_y"],
        sensor_data["acceleration_z"],
        sensor_data["gyroscope_x"],
        sensor_data["gyroscope_y"],
        sensor_data["gyroscope_z"],
        activity
    ))


def record_data():

    print("\n===== REAL SENSOR DATA RECORDER =====")

    activity = input(
        "Enter activity (standing/walking/running): "
    ).strip().lower()

    if activity not in ["standing", "walking", "running"]:
        print("Invalid activity.")
        return

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    esp32 = connect_esp32()

    print(f"\nRecording: {activity}")
    print("Press Ctrl+C to stop.\n")

    start_time = time.time()

    try:

        while True:

            line = esp32.readline().decode(
                "utf-8"
            ).strip()

            if not line:
                continue

            try:

                sensor_data = json.loads(line)

                timestamp = time.time() - start_time

                save_sensor_data(
                    cursor,
                    sensor_data,
                    activity,
                    timestamp
                )

                connection.commit()

                print(
                    f"{timestamp:.3f} | {activity} | "
                    f"heel={sensor_data['heel_pressure']:.2f}  "
                    
                )

            except json.JSONDecodeError:

                print("Invalid JSON:", line)

    except KeyboardInterrupt:

        print("\nRecording stopped.")

    finally:

        esp32.close()
        connection.close()

        print("Data saved to database.")


if __name__ == "__main__":
    record_data()