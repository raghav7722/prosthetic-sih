# from fastapi import APIRouter, HTTPException

# from backend.database.insert import insert_sensor_data


# router = APIRouter()


# @router.post("/sensor-data")
# def receive_sensor_data(data: dict):
#     """
#     Receive one sensor reading from ESP32 and store it in the database.
#     """

#     try:
#         insert_sensor_data(data)

#         return {
#             "status": "success",
#             "message": "Sensor data stored successfully"
#         }

#     except KeyError as error:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Missing field in sensor data: {error}"
#         )

#     except Exception as error:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Failed to store sensor data: {error}"
#         )

from fastapi import APIRouter, HTTPException

from backend.database.insert import insert_sensor_data
from backend.ml.predict import predict_gait


router = APIRouter()


@router.post("/sensor-data")
def receive_sensor_data(data: dict):
    """
    Receive ESP32 sensor data and store it in the database.
    """

    try:
        insert_sensor_data(data)

        return {
            "status": "success",
            "message": "Sensor data stored successfully"
        }

    except KeyError as error:
        raise HTTPException(
            status_code=400,
            detail=f"Missing field in sensor data: {error}"
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to store sensor data: {error}"
        )


@router.post("/predict")
def predict_sensor_data(data: dict):
    """
    Receive ESP32 sensor data and return ML gait prediction.
    """

    try:
        prediction = predict_gait(data)

        return {
            "status": "success",
            "prediction": prediction["prediction"],
            "confidence": prediction.get("confidence")
        }

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )

    except KeyError as error:
        raise HTTPException(
            status_code=400,
            detail=f"Missing field in sensor data: {error}"
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {error}"
        )