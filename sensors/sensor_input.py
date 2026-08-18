import random


def read_sensors():
    """
    Temporary sensor interface.

    Later this function will read actual:
    - Pressure sensors
    - IMU
    """

    sensor_data = {
        "heel_pressure": random.uniform(400, 900),
        "toe_pressure": random.uniform(300, 1000),
        "thigh_pressure": random.uniform(100, 400),

        "acceleration_x": random.uniform(-5, 5),
        "acceleration_y": random.uniform(-5, 5),
        "acceleration_z": random.uniform(5, 15),

        "gyroscope_x": random.uniform(-80, 80),
        "gyroscope_y": random.uniform(-80, 80),
        "gyroscope_z": random.uniform(-80, 80)
    }

    return sensor_data


if __name__ == "__main__":

    sensor_data = read_sensors()

    print("\n===== SENSOR DATA =====")

    for sensor, value in sensor_data.items():
        print(f"{sensor}: {value:.2f}")