from flask import Blueprint, jsonify
from database.db import get_connection
from utils.jwt_handler import token_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
@token_required
def dashboard(current_user):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Analytics
        cursor.execute("""
            SELECT
                COUNT(*) AS total_predictions,
                AVG(voting_prediction) AS average_energy,
                MAX(voting_prediction) AS highest_energy,
                MIN(voting_prediction) AS lowest_energy
            FROM predictions
            WHERE user_id = ?
        """, (current_user["user_id"],))

        analytics = dict(cursor.fetchone())

        # Latest 5 Predictions
        cursor.execute("""
            SELECT
                id,
                speed_kmh,
                battery_state,
                voting_prediction,
                created_at
            FROM predictions
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT 5
        """, (current_user["user_id"],))

        recent_predictions = [
            dict(row) for row in cursor.fetchall()
        ]

        conn.close()

        return jsonify({
            "success": True,
            "analytics": analytics,
            "recent_predictions": recent_predictions
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500