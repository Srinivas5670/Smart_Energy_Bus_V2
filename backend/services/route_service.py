import os
import pandas as pd
from math import radians, sin, cos, sqrt, atan2


class RouteService:

    REQUIRED_COLUMNS = [
        "stop_name",
        "stop_lat",
        "stop_lon"
    ]

    def __init__(self):

        project_root = os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )

        dataset_path = os.path.join(
            project_root,
            "dataset",
            "bus stops.csv"
        )

        if not os.path.exists(dataset_path):
            raise FileNotFoundError(
                f"Bus stop dataset not found:\n{dataset_path}"
            )

        self.stops = pd.read_csv(dataset_path)

        self._validate_dataset()
        self._prepare_dataset()

    def _validate_dataset(self):

        missing = [
            col for col in self.REQUIRED_COLUMNS
            if col not in self.stops.columns
        ]

        if missing:
            raise Exception(
                f"Dataset missing required columns: {missing}"
            )

    def _prepare_dataset(self):

        self.stops["stop_name"] = (
            self.stops["stop_name"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        self.stops = self.stops.dropna(
            subset=["stop_lat", "stop_lon"]
        )

        self.stops = self.stops.drop_duplicates(
            subset=["stop_name", "stop_lat", "stop_lon"]
        )

        self.stops["search_name"] = (
            self.stops["stop_name"]
            .str.lower()
        )

    def get_stop(self, stop_name):

        stop_name = stop_name.strip().lower()

        stop = self.stops[
            self.stops["search_name"] == stop_name
        ]

        if stop.empty:
            return None

        stop = stop.iloc[0]

        return {
            "stop_name": stop["stop_name"],
            "latitude": float(stop["stop_lat"]),
            "longitude": float(stop["stop_lon"]),
            "description": str(stop.get("stop_desc", "")),
            "zone": str(stop.get("zone_id", ""))
        }

    def search_stops(self, keyword):

        keyword = keyword.strip().lower()

        if keyword == "":
            return []

        matches = self.stops[
            self.stops["search_name"].str.contains(
                keyword,
                na=False
            )
        ]

        results = []

        for _, stop in matches.head(20).iterrows():

            results.append({
                "stop_name": stop["stop_name"],
                "latitude": float(stop["stop_lat"]),
                "longitude": float(stop["stop_lon"]),
                "description": str(stop.get("stop_desc", "")),
                "zone": str(stop.get("zone_id", ""))
            })

        return results

    def calculate_distance(self, source, destination):

        R = 6371

        lat1 = radians(source["latitude"])
        lon1 = radians(source["longitude"])

        lat2 = radians(destination["latitude"])
        lon2 = radians(destination["longitude"])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            sin(dlat / 2) ** 2
            + cos(lat1)
            * cos(lat2)
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a)
        )

        return round(R * c, 2)


route_service = RouteService()