import { useState, useEffect } from "react";
import RouteMap from "../components/RouteMap";
import Layout from "../components/Layout";
import api from "../services/api";

import {
    FaMapMarkerAlt,
    FaFlagCheckered,
    FaRoad,
    FaClock,
    FaStar
} from "react-icons/fa";

function Route() {

    const [source, setSource] = useState("");
    const [destination, setDestination] = useState("");

    const [sourceStops, setSourceStops] = useState([]);
    const [destinationStops, setDestinationStops] = useState([]);

    const [route, setRoute] = useState(null);

    const [selectedRoute, setSelectedRoute] = useState(null);

    // ===========================================
    // Restore Previous Route
    // ===========================================

    useEffect(() => {

        const savedRoute = sessionStorage.getItem("routePage");

        if (savedRoute) {

            const data = JSON.parse(savedRoute);

            setSource(data.source || "");

            setDestination(data.destination || "");

            setRoute(data.route || null);

            setSelectedRoute(data.selectedRoute || null);

        }

    }, []);

    // ===========================================
    // Save Route Automatically
    // ===========================================

    useEffect(() => {

        if (!route) return;

        sessionStorage.setItem(

            "routePage",

            JSON.stringify({

                source,

                destination,

                route,

                selectedRoute

            })

        );

    }, [

        source,

        destination,

        route,

        selectedRoute

    ]);

    // ===========================================
    // Search Source
    // ===========================================

    const searchSource = async (value) => {

        setSource(value);

        if (value.length < 2) {

            setSourceStops([]);

            return;

        }

        const response = await api.get(

            `/stops?q=${value}`

        );

        setSourceStops(response.data.stops);

    };

    // ===========================================
    // Search Destination
    // ===========================================

    const searchDestination = async (value) => {

        setDestination(value);

        if (value.length < 2) {

            setDestinationStops([]);

            return;

        }

        const response = await api.get(

            `/stops?q=${value}`

        );

        setDestinationStops(response.data.stops);

    };

    // ===========================================
    // Find Route
    // ===========================================

    const findRoute = async () => {

        try {

            const response = await api.post(

                "/route",

                {

                    source,

                    destination

                }

            );

            setRoute(response.data);

            if (

                response.data.routes.length > 0

            ) {

                setSelectedRoute(

                    response.data.routes[0]

                );

            }

        }

        catch (error) {

            alert(

                error.response?.data?.message ||

                "Route not found."

            );

        }

    };

    return (
                <Layout>

            <h1 className="text-3xl font-bold mb-8">

                Route Optimization

            </h1>

            <div className="bg-white shadow rounded-xl p-6">

                {/* Source */}

                <div className="mb-5">

                    <label className="font-semibold">

                        Source

                    </label>

                    <input
                        type="text"
                        value={source}
                        onChange={(e) => searchSource(e.target.value)}
                        className="border w-full p-3 rounded mt-2"
                        placeholder="Search source stop..."
                    />

                    {sourceStops.length > 0 && (

                        <div className="border rounded mt-2 max-h-40 overflow-auto">

                            {sourceStops.map((stop, index) => (

                                <div
                                    key={index}
                                    className="p-3 hover:bg-blue-50 cursor-pointer transition"
                                    onClick={() => {

                                        setSource(stop.stop_name);

                                        setSourceStops([]);

                                    }}
                                >

                                    {stop.stop_name}

                                </div>

                            ))}

                        </div>

                    )}

                </div>

                {/* Destination */}

                <div className="mb-5">

                    <label className="font-semibold">

                        Destination

                    </label>

                    <input
                        type="text"
                        value={destination}
                        onChange={(e) => searchDestination(e.target.value)}
                        className="border w-full p-3 rounded mt-2"
                        placeholder="Search destination stop..."
                    />

                    {destinationStops.length > 0 && (

                        <div className="border rounded mt-2 max-h-40 overflow-auto">

                            {destinationStops.map((stop, index) => (

                                <div
                                    key={index}
                                    className="p-3 hover:bg-blue-50 cursor-pointer transition"
                                    onClick={() => {

                                        setDestination(stop.stop_name);

                                        setDestinationStops([]);

                                    }}
                                >

                                    {stop.stop_name}

                                </div>

                            ))}

                        </div>

                    )}

                </div>

                <div className="flex gap-4">

                    <button
                        onClick={findRoute}
                        className="bg-blue-600 hover:bg-blue-700 transition text-white px-6 py-3 rounded-lg font-semibold"
                    >

                        Find Route

                    </button>

                    <button
                        type="button"
                        onClick={() => {

                            sessionStorage.removeItem("routePage");

                            window.location.reload();

                        }}
                        className="bg-red-600 hover:bg-red-700 transition text-white px-6 py-3 rounded-lg font-semibold"
                    >

                        Clear

                    </button>

                </div>

            </div>

            {route && (

                <div className="bg-white shadow-xl rounded-2xl p-8 mt-8">

                    <h2 className="text-3xl font-bold text-blue-700 mb-8">

                        Route Information

                    </h2>

                    {/* Summary Cards */}

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                        <div className="bg-blue-50 rounded-xl p-5">

                            <div className="flex items-center gap-2 text-gray-500 text-sm">

                                <FaMapMarkerAlt className="text-blue-600" />

                                <span>SOURCE</span>

                            </div>

                            <h3 className="text-xl font-semibold mt-2">

                                {route.source.stop_name}

                            </h3>

                        </div>

                        <div className="bg-green-50 rounded-xl p-5">

                            <div className="flex items-center gap-2 text-gray-500 text-sm">

                                <FaFlagCheckered className="text-green-600" />

                                <span>DESTINATION</span>

                            </div>

                            <h3 className="text-xl font-semibold mt-2">

                                {route.destination.stop_name}

                            </h3>

                        </div>

                        <div className="bg-orange-50 rounded-xl p-5">

                            <div className="flex items-center gap-2 text-gray-500 text-sm">

                                <FaRoad className="text-orange-600" />

                                <span>DISTANCE</span>

                            </div>

                            <h3 className="text-xl font-semibold mt-2">

                                {selectedRoute?.distance_km} km

                            </h3>

                        </div>

                        <div className="bg-purple-50 rounded-xl p-5">

                            <div className="flex items-center gap-2 text-gray-500 text-sm">

                                <FaClock className="text-purple-600" />

                                <span>DURATION</span>

                            </div>

                            <h3 className="text-xl font-semibold mt-2">

                                {selectedRoute?.duration_min} min

                            </h3>

                        </div>

                    </div>
                                        {/* Available Routes */}

                    <div className="mt-10">

                        <h2 className="text-2xl font-bold mb-5">

                            Available Routes

                        </h2>

                        <div className="space-y-4">

                            {route.routes.map((singleRoute, index) => (

                                <div
                                    key={index}
                                    onClick={() => setSelectedRoute(singleRoute)}
                                    className={`cursor-pointer rounded-xl border p-5 transition-all duration-200
                                    ${
                                        selectedRoute === singleRoute
                                            ? "border-blue-600 bg-blue-50 shadow-lg"
                                            : "border-gray-200 hover:border-blue-400 hover:shadow-md"
                                    }`}
                                >

                                    <div className="flex justify-between items-center">

                                        <div className="flex items-center gap-3">

                                            <h3 className="text-xl font-semibold">

                                                Route {index + 1}

                                            </h3>

                                            {index + 1 === route.recommended_route && (

                                                <span className="bg-yellow-400 text-black text-sm px-3 py-1 rounded-full flex items-center gap-1">

                                                    <FaStar />

                                                    Recommended

                                                </span>

                                            )}

                                        </div>

                                    </div>

                                    <div className="grid grid-cols-2 gap-4 mt-4">

                                        <div>

                                            <p className="text-gray-500 text-sm">

                                                Distance

                                            </p>

                                            <p className="font-semibold">

                                                {singleRoute.distance_km} km

                                            </p>

                                        </div>

                                        <div>

                                            <p className="text-gray-500 text-sm">

                                                Duration

                                            </p>

                                            <p className="font-semibold">

                                                {singleRoute.duration_min} min

                                            </p>

                                        </div>

                                    </div>

                                </div>

                            ))}

                        </div>

                    </div>

                    {/* Interactive Map */}

                    <h2 className="text-2xl font-bold mt-10 mb-4">

                        🗺 Interactive Route Map

                    </h2>

                    {selectedRoute && (

                        <RouteMap
                            source={route.source}
                            destination={route.destination}
                            route={selectedRoute}
                        />

                    )}

                </div>

            )}

        </Layout>

    );

}

export default Route;