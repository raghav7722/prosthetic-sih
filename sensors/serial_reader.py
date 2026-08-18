import serial
import json


# We will change this later to your actual ESP32 port.
SERIAL_PORT = "/dev/cu.YOUR_ESP32_PORT"

BAUD_RATE = 115200


def connect_esp32():

    connection = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=1
    )

    print("Connected to ESP32.")

    return connection


def read_sensor_data(connection):

    line = connection.readline().decode("utf-8").strip()

    if not line:
        return None

    try:
        sensor_data = json.loads(line)

        return sensor_data

    except json.JSONDecodeError:

        print("Invalid sensor data received:")
        print(line)

        return None


def main():

    connection = connect_esp32()

    print("Waiting for sensor data...\n")

    while True:

        sensor_data = read_sensor_data(connection)

        if sensor_data is not None:

            print(sensor_data)


if __name__ == "__main__":
    main()