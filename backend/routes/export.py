from flask import Blueprint, Response
from database.db import get_connection
from utils.jwt_handler import token_required
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.csv_export import generate_csv

export_bp = Blueprint("export", __name__)


@export_bp.route("/export/csv", methods=["GET"])
@token_required
def export_csv(current_user):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (current_user["user_id"],))

    rows = cursor.fetchall()
    conn.close()

    history = [dict(row) for row in rows]

    csv_data = generate_csv(history)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=prediction_history.csv"
        }
    )