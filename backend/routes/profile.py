from flask import Blueprint, jsonify
from database.db import get_connection
from utils.jwt_handler import token_required
from flask import request
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET"])
@token_required
def profile(current_user):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                full_name,
                email,
                created_at
            FROM users
            WHERE id = ?
        """, (current_user["user_id"],))

        user = cursor.fetchone()

        conn.close()

        if user is None:
            return jsonify({
                "success": False,
                "message": "User not found."
            }), 404

        return jsonify({
            "success": True,
            "profile": dict(user)
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
@profile_bp.route("/profile", methods=["PUT"])
@token_required
def update_profile(current_user):

    try:
        data = request.get_json()

        full_name = data["full_name"]
        email = data["email"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET full_name = ?, email = ?
            WHERE id = ?
        """, (
            full_name,
            email,
            current_user["user_id"]
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Profile updated successfully."
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
@profile_bp.route("/change-password", methods=["PUT"])
@token_required
def change_password(current_user):

    try:
        data = request.get_json()

        current_password = data["current_password"]
        new_password = data["new_password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT password
            FROM users
            WHERE id = ?
        """, (current_user["user_id"],))

        user = cursor.fetchone()

        if user is None:
            conn.close()
            return jsonify({
                "success": False,
                "message": "User not found."
            }), 404

        if not check_password_hash(
            user["password"],
            current_password
        ):
            conn.close()
            return jsonify({
                "success": False,
                "message": "Current password is incorrect."
            }), 401

        hashed_password = generate_password_hash(new_password)

        cursor.execute("""
            UPDATE users
            SET password = ?
            WHERE id = ?
        """, (
            hashed_password,
            current_user["user_id"]
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Password changed successfully."
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
@profile_bp.route("/profile", methods=["DELETE"])
@token_required
def delete_profile(current_user):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Delete user's prediction history first
        cursor.execute("""
            DELETE FROM predictions
            WHERE user_id = ?
        """, (current_user["user_id"],))

        # Delete user account
        cursor.execute("""
            DELETE FROM users
            WHERE id = ?
        """, (current_user["user_id"],))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Account deleted successfully."
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500