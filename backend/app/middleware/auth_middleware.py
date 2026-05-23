from functools import wraps
import jwt
from flask import request, g, current_app

from app.utils.helpers import decode_jwt
from app.utils.helpers import utc_now_iso
from app.utils.response import error_response
from app.db.mongo import get_db
from app.db.collections import DEVICES


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return error_response("Missing Bearer token", 401)

        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_jwt(token)
            g.user = payload
        except jwt.ExpiredSignatureError:
            return error_response("Token expired", 401)
        except jwt.InvalidTokenError:
            return error_response("Invalid token", 401)

        return fn(*args, **kwargs)

    return wrapper
