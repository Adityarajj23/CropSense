import os
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv()


class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    JWT_EXP_DELTA = timedelta(hours=int(os.getenv("JWT_EXP_HOURS", "24")))

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "smart_farming")

    DEVICE_MASTER_API_KEY = os.getenv("DEVICE_MASTER_API_KEY", "dev-device-key")

    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
    MODEL_PATH = os.getenv("MODEL_PATH", "trained_models/crop_health_model.pkl")
