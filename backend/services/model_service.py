import os
import sys
import joblib
import pandas as pd


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.config import Config

from ml.preprocess import (
    calculate_effective_vehicle_weight,
    estimate_battery_voltage,
    estimate_remaining_battery
)


class ModelService:

    def __init__(self):

        self.models = {}

        self.load_models()

    # =====================================================
    # Load Models
    # =====================================================

    def load_models(self):

        model_folder = Config.MODEL_FOLDER

        self.models = {

            "Linear Regression": joblib.load(
                os.path.join(
                    model_folder,
                    "linear.pkl"
                )
            ),

            "Random Forest": joblib.load(
                os.path.join(
                    model_folder,
                    "random_forest.pkl"
                )
            ),

            "Gradient Boosting": joblib.load(
                os.path.join(
                    model_folder,
                    "gradient_boost.pkl"
                )
            ),

            "XGBoost": joblib.load(
                os.path.join(
                    model_folder,
                    "xgboost.pkl"
                )
            ),

            "SVR": joblib.load(
                os.path.join(
                    model_folder,
                    "svr.pkl"
                )
            ),

            "KNN": joblib.load(
                os.path.join(
                    model_folder,
                    "knn.pkl"
                )
            ),

            "Voting Regressor": joblib.load(
                os.path.join(
                    model_folder,
                    "voting.pkl"
                )
            )

        }

        print("All ML models loaded successfully.")

    # =====================================================
    # Get Models
    # =====================================================

    def get_models(self):

        return self.models

    # =====================================================
    # Prediction
    # =====================================================

    def predict(self, input_data):

        # ---------------------------------------------
        # Default Values
        # ---------------------------------------------

        driving_mode = "Normal"

        temperature = 28

        wind = "Medium"

        # Empty vehicle weight (kg)

        base_vehicle_weight = 1800

        # ---------------------------------------------
        # Feature Engineering
        # ---------------------------------------------

        vehicle_weight = calculate_effective_vehicle_weight(

            base_vehicle_weight,

            int(
                input_data["Passenger_Count"]
            )

        )

        battery_voltage = estimate_battery_voltage(

            float(
                input_data["Battery_State_%"]
            )

        )

        # ---------------------------------------------
        # Model Input
        # ---------------------------------------------

        model_input = {

            "Speed_kmh": float(
                input_data["Speed_kmh"]
            ),

            "Battery_State_%": float(
                input_data["Battery_State_%"]
            ),

            "Battery_Voltage_V": battery_voltage,

            "Driving_Mode": driving_mode,

            "Road_Type": input_data["Road_Type"],

            "Traffic_Condition": input_data["Traffic_Condition"],

            "Road_Gradient": input_data["Road_Gradient"],

            "Weather_Condition": input_data["Weather_Condition"],

            "Temperature_C": temperature,

            "Wind": wind,

            "Vehicle_Weight_kg": vehicle_weight,

            "Passenger_Count": int(
                input_data["Passenger_Count"]
            ),

            "Distance_Travelled_km": float(
                input_data["Distance_Travelled_km"]
            )

        }

        input_df = pd.DataFrame(
            [model_input]
        )

        predictions = {}

         # ---------------------------------------------
        # Run Predictions
        # ---------------------------------------------

        for model_name, model in self.models.items():

            prediction = model.predict(input_df)[0]

            predictions[model_name] = round(
                float(prediction),
                4
            )

        # ---------------------------------------------
        # Best Prediction
        # ---------------------------------------------

        best_prediction = predictions[
            "Voting Regressor"
        ]

        predictions[
            "Best Prediction"
        ] = best_prediction

        # ---------------------------------------------
        # Remaining Battery
        # ---------------------------------------------

        remaining_battery = estimate_remaining_battery(

            float(
                input_data["Battery_State_%"]
            ),

            best_prediction

        )

        predictions[
            "Estimated Remaining Battery (%)"
        ] = remaining_battery

        # ---------------------------------------------
        # Generated Values
        # ---------------------------------------------

        predictions[
            "Battery_Voltage_V"
        ] = battery_voltage

        predictions[
            "Vehicle_Weight_kg"
        ] = vehicle_weight

        predictions[
            "Driving_Mode"
        ] = driving_mode

        predictions[
            "Temperature_C"
        ] = temperature

        predictions[
            "Wind"
        ] = wind

        return predictions


# =====================================================
# Singleton Instance
# =====================================================

model_service = ModelService()