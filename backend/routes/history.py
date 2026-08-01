from flask import Blueprint, jsonify

from database.db import get_connection
from utils.jwt_handler import token_required


history_bp = Blueprint(
    "history",
    __name__
)


# =====================================================
# Get Prediction History
# =====================================================

@history_bp.route(
    "/history",
    methods=["GET"]
)
@token_required
def get_history(current_user):

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM predictions

            WHERE user_id = ?

            ORDER BY created_at DESC

        """, (

            current_user["user_id"],

        ))

        rows = cursor.fetchall()

        history = [

            dict(row)

            for row in rows

        ]

        conn.close()

        return jsonify({

            "success": True,

            "count": len(history),

            "history": history

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


# =====================================================
# Delete Prediction
# =====================================================

@history_bp.route(
    "/history/<int:prediction_id>",
    methods=["DELETE"]
)
@token_required
def delete_prediction(
    current_user,
    prediction_id
):

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM predictions

            WHERE id = ?

            AND user_id = ?

        """, (

            prediction_id,

            current_user["user_id"]

        ))

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            return jsonify({

                "success": False,

                "message": "Prediction not found."

            }), 404

        conn.close()

        return jsonify({

            "success": True,

            "message": "Prediction deleted successfully."

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500