from flask import Blueprint, request, jsonify

from services.model_service import model_service
from services.database_service import database_service
from services.route_service import route_service
from services.osrm_service import osrm_service
from utils.jwt_handler import token_required


prediction_bp = Blueprint(
    "prediction",
    __name__
)


@prediction_bp.route(
    "/predict",
    methods=["POST"]
)
@token_required
def predict(current_user):

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "message": "No input data received."
            }), 400

        # =====================================================
        # Required Fields
        # =====================================================

        required_fields = [
            "source",
            "destination",
            "Speed_kmh",
            "Battery_State_%",
            "Passenger_Count",
            "Weather_Condition",
            "Traffic_Condition",
            "Road_Type",
            "Road_Gradient"
        ]

        missing = [
            field for field in required_fields
            if field not in data or data[field] == ""
        ]

        if missing:

            return jsonify({
                "success": False,
                "message": f"Missing fields: {', '.join(missing)}"
            }), 400

        # =====================================================
        # Find Stops
        # =====================================================

        source = route_service.get_stop(data["source"])
        destination = route_service.get_stop(data["destination"])

        if source is None:

            return jsonify({
                "success": False,
                "message": "Source stop not found."
            }), 404

        if destination is None:

            return jsonify({
                "success": False,
                "message": "Destination stop not found."
            }), 404

        # =====================================================
        # Get Route
        # =====================================================

        route_result = osrm_service.get_route(
            source["latitude"],
            source["longitude"],
            destination["latitude"],
            destination["longitude"]
        )

        if not route_result["success"]:

            return jsonify(route_result), 400

        best_route = route_result["routes"][0]

        # =====================================================
        # Add Distance For ML Model
        # =====================================================

        prediction_input = data.copy()

        prediction_input["Distance_Travelled_km"] = best_route["distance_km"]

        # =====================================================
        # Run ML Prediction
        # =====================================================

        predictions = model_service.predict(prediction_input)

        # =====================================================
        # Save Prediction History
        # =====================================================

        prediction_data = prediction_input.copy()

        prediction_data.update(predictions)

        prediction_data["user_id"] = current_user["user_id"]

        database_service.save_prediction(
            prediction_data
        )

        # =====================================================
        # Response
        # =====================================================

        return jsonify({

            "success": True,

            "source": source,

            "destination": destination,

            "distance_km": best_route["distance_km"],

            "duration_min": best_route["duration_min"],

            "recommended_route": route_result["recommended_route"],

            "route_count": route_result["route_count"],

            "routes": route_result["routes"],

            "predictions": predictions

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500