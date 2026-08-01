import jwt
from functools import wraps
from flask import request, jsonify
from config import Config


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if "Authorization" in request.headers:
            bearer = request.headers["Authorization"]

            if bearer.startswith("Bearer "):
                token = bearer.split(" ")[1]

        if not token:
            return jsonify({
                "success": False,
                "message": "Token is missing."
            }), 401

        try:
            data = jwt.decode(
                token,
                Config.SECRET_KEY,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            return jsonify({
                "success": False,
                "message": "Token has expired."
            }), 401

        except jwt.InvalidTokenError:
            return jsonify({
                "success": False,
                "message": "Invalid token."
            }), 401

        return f(data, *args, **kwargs)

    return decorated