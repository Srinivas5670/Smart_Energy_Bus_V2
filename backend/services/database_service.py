from database.db import get_connection


class DatabaseService:

    def save_prediction(self, prediction_data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO predictions (

                user_id,

                speed_kmh,

                battery_state,

                battery_voltage,

                driving_mode,

                road_type,

                traffic_condition,

                road_gradient,

                weather_condition,

                temperature,

                wind,

                vehicle_weight,

                passenger_count,

                distance_travelled,

                linear_prediction,

                random_forest_prediction,

                gradient_boost_prediction,

                xgboost_prediction,

                svr_prediction,

                knn_prediction,

                voting_prediction,

                remaining_battery

            )

            VALUES (

                ?,?,?,?,?,?,?,?,?,?,

                ?,?,?,?,?,?,?,?,?,?,

                ?,?

            )

        """, (

            prediction_data["user_id"],

            prediction_data["Speed_kmh"],

            prediction_data["Battery_State_%"],

            prediction_data["Battery_Voltage_V"],

            prediction_data["Driving_Mode"],

            prediction_data["Road_Type"],

            prediction_data["Traffic_Condition"],

            prediction_data["Road_Gradient"],

            prediction_data["Weather_Condition"],

            prediction_data["Temperature_C"],

            prediction_data["Wind"],

            prediction_data["Vehicle_Weight_kg"],

            prediction_data["Passenger_Count"],

            prediction_data["Distance_Travelled_km"],

            prediction_data["Linear Regression"],

            prediction_data["Random Forest"],

            prediction_data["Gradient Boosting"],

            prediction_data["XGBoost"],

            prediction_data["SVR"],

            prediction_data["KNN"],

            prediction_data["Voting Regressor"],

            prediction_data["Estimated Remaining Battery (%)"]

        ))

        conn.commit()
        conn.close()


database_service = DatabaseService()