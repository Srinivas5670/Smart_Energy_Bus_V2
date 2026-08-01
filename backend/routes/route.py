from flask import Blueprint, request, jsonify

from services.route_service import route_service
from services.osrm_service import osrm_service

route_bp = Blueprint("route", __name__)


@route_bp.route("/route", methods=["POST"])
def get_route():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is required."
            }), 400

        source = data.get("source")
        destination = data.get("destination")

        if not source or not destination:
            return jsonify({
                "success": False,
                "message": "Source and destination are required."
            }), 400

        source_stop = route_service.get_stop(source)
        destination_stop = route_service.get_stop(destination)

        if source_stop is None:
            return jsonify({
                "success": False,
                "message": "Source stop not found."
            }), 404

        if destination_stop is None:
            return jsonify({
                "success": False,
                "message": "Destination stop not found."
            }), 404

        route_result = osrm_service.get_route(
            source_lat=source_stop["latitude"],
            source_lon=source_stop["longitude"],
            destination_lat=destination_stop["latitude"],
            destination_lon=destination_stop["longitude"]
        )

        if not route_result["success"]:
            return jsonify(route_result), 500

        return jsonify({

            "success": True,

            "source": source_stop,

            "destination": destination_stop,

            "recommended_route": route_result["recommended_route"],

            "route_count": route_result["route_count"],

            "routes": route_result["routes"]

        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@route_bp.route("/stops", methods=["GET"])
def search_stops():

    keyword = (
        request.args.get("keyword")
        or request.args.get("q")
    )

    if not keyword:

        return jsonify({
            "success": False,
            "message": "Search keyword is required."
        }), 400

    stops = route_service.search_stops(keyword)

    return jsonify({

        "success": True,

        "count": len(stops),

        "stops": stops

    }), 200