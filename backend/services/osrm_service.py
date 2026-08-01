import requests


class OSRMService:

    def __init__(self):
        # Public OSRM server (Development)
        self.base_url = "https://router.project-osrm.org"

    def get_route(
        self,
        source_lat,
        source_lon,
        destination_lat,
        destination_lon
    ):

        url = (
            f"{self.base_url}/route/v1/driving/"
            f"{source_lon},{source_lat};"
            f"{destination_lon},{destination_lat}"
            "?alternatives=true"
            "&overview=full"
            "&steps=false"
            "&geometries=geojson"
        )

        try:

            response = requests.get(url, timeout=20)

            response.raise_for_status()

            data = response.json()

            if data.get("code") != "Ok":
                return {
                    "success": False,
                    "message": data.get(
                        "message",
                        "Unable to calculate route."
                    )
                }

            routes = []

            for index, route in enumerate(data["routes"], start=1):

                routes.append({

                    "route_id": index,

                    "distance_km": round(
                        route["distance"] / 1000,
                        2
                    ),

                    "duration_min": round(
                        route["duration"] / 60,
                        2
                    ),

                    "geometry": route["geometry"]
                })

            routes.sort(
                key=lambda r: (
                    r["distance_km"],
                    r["duration_min"]
                )
            )

            for i, route in enumerate(routes, start=1):
                route["route_id"] = i

            return {

                "success": True,

                "recommended_route": 1,

                "route_count": len(routes),

                "routes": routes
            }

        except requests.exceptions.Timeout:

            return {
                "success": False,
                "message": "OSRM server timed out."
            }

        except requests.exceptions.ConnectionError:

            return {
                "success": False,
                "message": "Unable to connect to OSRM server."
            }

        except requests.exceptions.HTTPError as e:

            return {
                "success": False,
                "message": f"HTTP Error: {e}"
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }


osrm_service = OSRMService()