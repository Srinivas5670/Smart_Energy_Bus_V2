import {
    MapContainer,
    TileLayer,
    Marker,
    Polyline,
    Popup
} from "react-leaflet";

import L, { LatLngBounds } from "leaflet";

import "leaflet/dist/leaflet.css";

import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({

    iconRetinaUrl: markerIcon2x,

    iconUrl: markerIcon,

    shadowUrl: markerShadow

});

function RouteMap({ source, destination, route }) {

    if (!source || !destination || !route) {
        return null;
    }

    const routeCoordinates =
        route.geometry.coordinates.map(
            ([longitude, latitude]) => [latitude, longitude]
        );

    const sourcePosition = [
        source.latitude,
        source.longitude
    ];

    const destinationPosition = [
        destination.latitude,
        destination.longitude
    ];

    const bounds = new LatLngBounds([
        sourcePosition,
        destinationPosition,
        ...routeCoordinates
    ]).pad(0.2);

    return (

        <div className="mt-8 rounded-2xl overflow-hidden shadow-2xl border border-gray-200">
            <MapContainer
                bounds={bounds}
                style={{
                    height: "535px",
                    width: "100%"
                }}
                scrollWheelZoom={true}
            >

                <TileLayer
                    attribution='&copy; OpenStreetMap contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

                <Marker position={sourcePosition}>
                    <Popup>
                        <strong>📍 Source</strong>
                        <br />
                        {source.stop_name}
                    </Popup>
                </Marker>

                <Marker position={destinationPosition}>
                    <Popup>
                        <strong>🏁 Destination</strong>
                        <br />
                        {destination.stop_name}
                    </Popup>
                </Marker>

               <Polyline
    positions={routeCoordinates}
    pathOptions={{
        color: "#25deeb",
        weight: 7,
        opacity: 0.9
    }}
/>

            </MapContainer>

        </div>

    );

}

export default RouteMap;