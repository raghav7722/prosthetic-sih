import json
import serial
import requests


# Change this when your teammate gives you the actual ESP32 port.
SERIAL_PORT = "/dev/cu.YOUR_ESP32_PORT"

BAUD_RATE = 115200

BACKEND_URL = "http://127.0.0.1:8000/api/sensor-data"


def connect_esp32():
    """Connect to ESP32 through USB serial."""

    connection = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=1
    )

    print("Connected to ESP32.")

    return connection


def read_sensor_data(connection):
    """Read and decode one JSON line from ESP32."""

    line = connection.readline().decode("utf-8").strip()

    if not line:
        return None

    try:
        return json.loads(line)

    except json.JSONDecodeError:
        print("Invalid JSON received:")
        print(line)

        return None


def send_to_backend(sensor_data):
    """Send one ESP32 reading to the FastAPI backend."""

    response = requests.post(
        BACKEND_URL,
        json=sensor_data,
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def main():

    connection = connect_esp32()

    print("Waiting for ESP32 sensor data...\n")

    try:

        while True:

            sensor_data = read_sensor_data(connection)

            if sensor_data is None:
                continue

            print("ESP32:", sensor_data)

            try:

                result = send_to_backend(sensor_data)

                print("Backend:", result)

            except requests.RequestException as error:

                print("Could not send data to backend:")
                print(error)

    except KeyboardInterrupt:

        print("\nSensor reader stopped.")

    finally:

        connection.close()


if __name__ == "__main__":
    main()