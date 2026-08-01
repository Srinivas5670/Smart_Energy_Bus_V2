from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_connection
import jwt
import datetime
from config import Config

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    try:
        data = request.get_json()

        full_name = data["full_name"]
        email = data["email"]
        password = data["password"]

        hashed_password = generate_password_hash(password)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users(full_name, email, password)
            VALUES (?, ?, ?)
        """, (full_name, email, hashed_password))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "User registered successfully."
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@auth_bp.route("/login", methods=["POST"])
def login():

    try:
        data = request.get_json()

        email = data["email"]
        password = data["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()
        conn.close()

        if user is None:
            return jsonify({
                "success": False,
                "message": "Invalid email or password."
            }), 401

        if not check_password_hash(user["password"], password):
            return jsonify({
                "success": False,
                "message": "Invalid email or password."
            }), 401

        token = jwt.encode(
            {
                "user_id": user["id"],
                "email": user["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=Config.JWT_EXPIRATION_HOURS)
            },
            Config.SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({
            "success": True,
            "token": token
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500