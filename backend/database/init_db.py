import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import get_connection


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # =====================================================
    # USERS TABLE
    # =====================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # =====================================================
    # PREDICTIONS TABLE
    # =====================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            speed_kmh REAL,

            battery_state REAL,

            battery_voltage REAL,

            driving_mode TEXT,

            road_type TEXT,

            traffic_condition TEXT,

            road_gradient REAL,

            weather_condition TEXT,

            temperature REAL,

            wind REAL,

            vehicle_weight REAL,

            passenger_count INTEGER,

            distance_travelled REAL,

            linear_prediction REAL,

            random_forest_prediction REAL,

            gradient_boost_prediction REAL,

            xgboost_prediction REAL,

            svr_prediction REAL,

            knn_prediction REAL,

            voting_prediction REAL,

            remaining_battery REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(id)

        )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()