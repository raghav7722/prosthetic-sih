# import random


# def read_sensors():
#     """
#     Temporary sensor interface.

#     Later this function will read actual:
#     - Pressure sensors
#     - IMU
#     """

#     sensor_data = {
#         "heel_pressure": random.uniform(400, 900),
#         "toe_pressure": random.uniform(300, 1000),
#         "thigh_pressure": random.uniform(100, 400),

#         "acceleration_x": random.uniform(-5, 5),
#         "acceleration_y": random.uniform(-5, 5),
#         "acceleration_z": random.uniform(5, 15),

#         "gyroscope_x": random.uniform(-80, 80),
#         "gyroscope_y": random.uniform(-80, 80),
#         "gyroscope_z": random.uniform(-80, 80)
#     }

#     return sensor_data


# if __name__ == "__main__":

#     sensor_data = read_sensors()

#     print("\n===== SENSOR DATA =====")

#     for sensor, value in sensor_data.items():
#         print(f"{sensor}: {value:.2f}")

import serial
import json

SERIAL_PORT = "/dev/cu.usbserial-0001"

BAUD_RATE = 115200

def connect_sensor():

    connection = serial.Serial(

        SERIAL_PORT,

        BAUD_RATE,

        timeout=1

    )

    return connection

def read_sensors(connection):

    line = connection.readline().decode("utf-8").strip()

    if not line:

        return None

    sensor_data = json.loads(line)

    return sensor_data

if __name__ == "__main__":

    connection = connect_sensor()

    print("Connected to sensor system.")

    print("Waiting for sensor data...\n")

    while True:

        sensor_data = read_sensors(connection)

        if sensor_data is not None:

            print(sensor_data)