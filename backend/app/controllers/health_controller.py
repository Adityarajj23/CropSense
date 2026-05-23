from flask import current_app

from app.db.mongo import get_db
from app.utils.response import success_response, error_response


def health():
    return success_response({"status": "ok", "service": "smart-farming-backend"}, "Healthy")


def health_db():
    try:
        db = get_db()
        db.command("ping")
        return success_response({"status": "ok", "db": current_app.config["MONGO_DB_NAME"]}, "DB healthy")
    except Exception as exc:
        return error_response(f"DB unhealthy: {exc}", 500)


def health_storage():
    return success_response(
        {
            "status": "ok",
            "mode": "local-filesystem",
            "upload_dir": current_app.config["UPLOAD_DIR"],
        },
        "Storage health",
    )
