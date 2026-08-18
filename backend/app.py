from fastapi import FastAPI

from backend.api.routes import router


app = FastAPI(
    title="Prosthetic Gait Backend",
    description="Backend API for ESP32 sensor data and ML-based gait analysis",
    version="1.0.0"
)


app.include_router(router, prefix="/api")