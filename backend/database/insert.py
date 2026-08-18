# from backend.database.db import get_connection


# def insert_sensor_data(data):
#     """
#     Insert one ESP32 sensor reading into the gait_data table.

#     Expected JSON format:
#     {
#         "server_timestamp": "...",
#         "device": "ESP32-CAM",
#         "sensors": {
#             "ax": ...,
#             "ay": ...,
#             "az": ...,
#             "gx": ...,
#             "gy": ...,
#             "gz": ...,
#             "temperature_c": ...,
#             "fsr1": ...
#         }
#     }
#     """

#     sensors = data["sensors"]

#     connection = get_connection()
#     cursor = connection.cursor()

#     cursor.execute(
#         """
#         INSERT INTO gait_data (
#             server_timestamp,
#             device,
#             ax,
#             ay,
#             az,
#             gx,
#             gy,
#             gz,
#             temperature_c,
#             fsr1
#         )
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """,
#         (
#             data["server_timestamp"],
#             data["device"],
#             sensors["ax"],
#             sensors["ay"],
#             sensors["az"],
#             sensors["gx"],
#             sensors["gy"],
#             sensors["gz"],
#             sensors["temperature_c"],
#             sensors["fsr1"],
#         ),
#     )

#     connection.commit()
#     connection.close()

from backend.database.db import get_connection


def insert_sensor_data(data):
    """
    Insert one ESP32 sensor reading into the existing gait_data table.

    Expected JSON format:

    {
        "server_timestamp": "...",
        "device": "ESP32-CAM",
        "sensors": {
            "ax": ...,
            "ay": ...,
            "az": ...,
            "gx": ...,
            "gy": ...,
            "gz": ...,
            "temperature_c": ...,
            "fsr1": ...
        }
    }
    """

    sensors = data["sensors"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["server_timestamp"],
            sensors["fsr1"],
            sensors["ax"],
            sensors["ay"],
            sensors["az"],
            sensors["gx"],
            sensors["gy"],
            sensors["gz"],
            None
        )
    )

    connection.commit()
    connection.close()