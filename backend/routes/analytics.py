from flask import Blueprint, jsonify
from database.db import get_connection
from utils.jwt_handler import token_required

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics", methods=["GET"])
@token_required
def analytics(current_user):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_predictions,
                AVG(voting_prediction) AS average_energy,
                MAX(voting_prediction) AS max_energy,
                MIN(voting_prediction) AS min_energy
            FROM predictions
            WHERE user_id = ?
        """, (current_user["user_id"],))

        result = dict(cursor.fetchone())

        conn.close()

        return jsonify({
            "success": True,
            "analytics": result
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500