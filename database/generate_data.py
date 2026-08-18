import sqlite3
import random

DATABASE_NAME = "data/gait_data.db"


ACTIVITIES = [
    "standing",
    "walking",
    "running",
    # "uneven_surface",
    # "inclined_surface"
]


def generate_sensor_data(activity):
    if activity == "standing":
        heel_pressure = random.uniform(400, 600)
        toe_pressure = random.uniform(300, 500)
        thigh_pressure = random.uniform(100, 200)

        acceleration_x = random.uniform(-0.1, 0.1)
        acceleration_y = random.uniform(-0.1, 0.1)
        acceleration_z = random.uniform(9.6, 10.0)

        gyroscope_x = random.uniform(-0.5, 0.5)
        gyroscope_y = random.uniform(-0.5, 0.5)
        gyroscope_z = random.uniform(-0.5, 0.5)

    elif activity == "walking":
        heel_pressure = random.uniform(450, 700)
        toe_pressure = random.uniform(600, 900)
        thigh_pressure = random.uniform(150, 300)

        acceleration_x = random.uniform(-2, 2)
        acceleration_y = random.uniform(-2, 2)
        acceleration_z = random.uniform(8, 12)

        gyroscope_x = random.uniform(-30, 30)
        gyroscope_y = random.uniform(-30, 30)
        gyroscope_z = random.uniform(-30, 30)

    elif activity == "running":
        heel_pressure = random.uniform(700, 1000)
        toe_pressure = random.uniform(900, 1200)
        thigh_pressure = random.uniform(250, 450)

        acceleration_x = random.uniform(-5, 5)
        acceleration_y = random.uniform(-5, 5)
        acceleration_z = random.uniform(5, 15)

        gyroscope_x = random.uniform(-80, 80)
        gyroscope_y = random.uniform(-80, 80)
        gyroscope_z = random.uniform(-80, 80)

    # elif activity == "uneven_surface":
    #     heel_pressure = random.uniform(350, 850)
    #     toe_pressure = random.uniform(400, 1000)
    #     thigh_pressure = random.uniform(120, 350)

    #     acceleration_x = random.uniform(-4, 4)
    #     acceleration_y = random.uniform(-4, 4)
    #     acceleration_z = random.uniform(6, 14)

    #     gyroscope_x = random.uniform(-60, 60)
    #     gyroscope_y = random.uniform(-60, 60)
    #     gyroscope_z = random.uniform(-60, 60)

    # else:  # inclined_surface
    #     heel_pressure = random.uniform(300, 700)
    #     toe_pressure = random.uniform(700, 1100)
    #     thigh_pressure = random.uniform(200, 400)

    #     acceleration_x = random.uniform(-3, 3)
    #     acceleration_y = random.uniform(-3, 3)
    #     acceleration_z = random.uniform(7, 13)

    #     gyroscope_x = random.uniform(-50, 50)
    #     gyroscope_y = random.uniform(-50, 50)
    #     gyroscope_z = random.uniform(-50, 50)

    return (
        heel_pressure,
        toe_pressure,
        thigh_pressure,
        acceleration_x,
        acceleration_y,
        acceleration_z,
        gyroscope_x,
        gyroscope_y,
        gyroscope_z
    )


def generate_dataset(samples_per_activity=100):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM gait_data")
    timestamp = 0.0

    for activity in ACTIVITIES:

        for _ in range(samples_per_activity):

            sensor_data = generate_sensor_data(activity)

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
            """, (
                timestamp,
                *sensor_data,
                activity
            ))

            timestamp += 0.001

    connection.commit()
    connection.close()

    total_samples = samples_per_activity * len(ACTIVITIES)

    print(f"{total_samples} samples generated successfully.")


if __name__ == "__main__":
    generate_dataset(100)