import { useState } from "react";
import Layout from "../components/Layout";
import RouteMap from "../components/RouteMap";
import api from "../services/api";

function Prediction() {

    const [formData, setFormData] = useState({

        source: "",

        destination: "",

        Speed_kmh: "",

        Passenger_Count: "",

        "Battery_State_%": "",

        Weather_Condition: "",

        Traffic_Condition: "",

        Road_Type: "",

        Road_Gradient: ""

    });

    const [prediction, setPrediction] = useState(null);

    const [routeInfo, setRouteInfo] = useState(null);

    // Autocomplete

    const [sourceStops, setSourceStops] = useState([]);

    const [destinationStops, setDestinationStops] = useState([]);

    // Selected route for RouteMap

    const [selectedRoute, setSelectedRoute] = useState(null);

    const searchSource = async (value) => {

        setFormData({

            ...formData,

            source: value

        });

        if (value.length < 2) {

            setSourceStops([]);

            return;

        }

        try {

            const response = await api.get(`/stops?q=${value}`);

            setSourceStops(response.data.stops);

        }

        catch (error) {

            console.error(error);

        }

    };

    const searchDestination = async (value) => {

        setFormData({

            ...formData,

            destination: value

        });

        if (value.length < 2) {

            setDestinationStops([]);

            return;

        }

        try {

            const response = await api.get(`/stops?q=${value}`);

            setDestinationStops(response.data.stops);

        }

        catch (error) {

            console.error(error);

        }

    };

    const handleChange = (e) => {

        const { name, value } = e.target;

        setFormData({

            ...formData,

            [name]: value

        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const response = await api.post(

                "/predict",

                {

                    source: formData.source,

                    destination: formData.destination,

                    Speed_kmh: Number(formData.Speed_kmh),

                    Passenger_Count: Number(formData.Passenger_Count),

                    "Battery_State_%": Number(
                        formData["Battery_State_%"]
                    ),

                    Weather_Condition:
                        formData.Weather_Condition,

                    Traffic_Condition:
                        formData.Traffic_Condition,

                    Road_Type:
                        formData.Road_Type,

                    Road_Gradient:
                        formData.Road_Gradient

                }

            );

            setPrediction(response.data.predictions);

            setRouteInfo({

                source: response.data.source,

                destination: response.data.destination,

                distance_km: response.data.distance_km,

                duration_min: response.data.duration_min,

                recommended_route:
                    response.data.recommended_route,

                route_count:
                    response.data.route_count,

                routes:
                    response.data.routes

            });

            // Show recommended route on map

            if (response.data.routes.length > 0) {

                setSelectedRoute(response.data.routes[0]);

            }

        }

        catch (error) {

            alert(

                error.response?.data?.message ||

                "Prediction Failed"

            );

        }

    };

    return (
                <Layout>

            <h1 className="text-3xl font-bold mb-8">
                Energy Prediction
            </h1>

            <form
                onSubmit={handleSubmit}
                className="bg-white rounded-xl shadow-lg p-8"
            >

                <h2 className="text-2xl font-bold mb-6">
                    Bus Journey Details
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    {/* Source */}

                    <div>

                        <label className="block font-semibold mb-2">
                            Source Stop
                        </label>

                        <input
                            type="text"
                            value={formData.source}
                            onChange={(e) =>
                                searchSource(e.target.value)
                            }
                            placeholder="Search source stop..."
                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            autoComplete="off"
                            required
                        />

                        {sourceStops.length > 0 && (

                            <div className="border rounded-lg mt-2 max-h-40 overflow-auto bg-white shadow">

                                {sourceStops.map((stop, index) => (

                                    <div
                                        key={index}
                                        className="p-3 hover:bg-blue-50 cursor-pointer transition"
                                        onClick={() => {

                                            setFormData({

                                                ...formData,

                                                source: stop.stop_name

                                            });

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

                    <div>

                        <label className="block font-semibold mb-2">
                            Destination Stop
                        </label>

                        <input
                            type="text"
                            value={formData.destination}
                            onChange={(e) =>
                                searchDestination(e.target.value)
                            }
                            placeholder="Search destination stop..."
                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            autoComplete="off"
                            required
                        />

                        {destinationStops.length > 0 && (

                            <div className="border rounded-lg mt-2 max-h-40 overflow-auto bg-white shadow">

                                {destinationStops.map((stop, index) => (

                                    <div
                                        key={index}
                                        className="p-3 hover:bg-blue-50 cursor-pointer transition"
                                        onClick={() => {

                                            setFormData({

                                                ...formData,

                                                destination: stop.stop_name

                                            });

                                            setDestinationStops([]);

                                        }}
                                    >

                                        {stop.stop_name}

                                    </div>

                                ))}

                            </div>

                        )}

                    </div>

                                        {/* Speed */}

                    <div>

                        <label className="block font-semibold mb-2">
                            Speed (km/h)
                        </label>

                        <input
                            type="number"
                            name="Speed_kmh"
                            value={formData.Speed_kmh}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            required
                        />

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Passenger Count
                        </label>

                        <input
                            type="number"
                            name="Passenger_Count"
                            value={formData.Passenger_Count}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            required
                        />

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Battery State (%)
                        </label>

                        <input
                            type="number"
                            name="Battery_State_%"
                            value={formData["Battery_State_%"]}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            required
                        />

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Weather
                        </label>

                        <select
                            name="Weather_Condition"
                            value={formData.Weather_Condition}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3"
                            required
                        >

                            <option value="">
                                Select Weather
                            </option>

                            <option value="Sunny">
                                Sunny
                            </option>

                            <option value="Cloudy">
                                Cloudy
                            </option>

                            <option value="Rainy">
                                Rainy
                            </option>

                        </select>

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Traffic
                        </label>

                        <select
                            name="Traffic_Condition"
                            value={formData.Traffic_Condition}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3"
                            required
                        >

                            <option value="">
                                Select Traffic
                            </option>

                            <option value="Low">
                                Low
                            </option>

                            <option value="Medium">
                                Medium
                            </option>

                            <option value="High">
                                High
                            </option>

                        </select>

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Road Type
                        </label>

                        <select
                            name="Road_Type"
                            value={formData.Road_Type}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3"
                            required
                        >

                            <option value="">
                                Select Road Type
                            </option>

                            <option value="City">
                                City
                            </option>

                            <option value="Highway">
                                Highway
                            </option>

                            <option value="Rural">
                                Rural
                            </option>

                        </select>

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">
                            Road Gradient
                        </label>

                        <select
                            name="Road_Gradient"
                            value={formData.Road_Gradient}
                            onChange={handleChange}
                            className="w-full border rounded-lg p-3"
                            required
                        >

                            <option value="">
                                Select Gradient
                            </option>

                            <option value="Flat">
                                Flat
                            </option>

                            <option value="Ascending">
                                Ascending
                            </option>

                            <option value="Descending">
                                Descending
                            </option>

                        </select>

                    </div>

                </div>

                <button
                    type="submit"
                    className="mt-8 w-full bg-blue-600 hover:bg-blue-700 transition text-white font-semibold py-3 rounded-lg"
                >
                    Predict Energy Consumption
                </button>

            </form>
                        {routeInfo && (

                <div className="mt-10">

                    <h2 className="text-3xl font-bold text-blue-700 mb-8">
                        Journey Summary
                    </h2>

                    <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

                        <div className="bg-blue-50 rounded-xl shadow p-5">

                            <p className="text-gray-500 text-sm">
                                Source
                            </p>

                            <h3 className="text-xl font-bold mt-2">
                                {routeInfo.source.stop_name || routeInfo.source}
                            </h3>

                        </div>

                        <div className="bg-green-50 rounded-xl shadow p-5">

                            <p className="text-gray-500 text-sm">
                                Destination
                            </p>

                            <h3 className="text-xl font-bold mt-2">
                                {routeInfo.destination.stop_name || routeInfo.destination}
                            </h3>

                        </div>

                        <div className="bg-orange-50 rounded-xl shadow p-5">

                            <p className="text-gray-500 text-sm">
                                Distance
                            </p>

                            <h3 className="text-xl font-bold mt-2">
                                {selectedRoute?.distance_km || routeInfo.distance_km} km
                            </h3>

                        </div>

                        <div className="bg-purple-50 rounded-xl shadow p-5">

                            <p className="text-gray-500 text-sm">
                                Duration
                            </p>

                            <h3 className="text-xl font-bold mt-2">
                                {selectedRoute?.duration_min || routeInfo.duration_min} min
                            </h3>

                        </div>

                    </div>

                </div>

            )}

            {prediction && (

                <>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">

                        <div className="bg-blue-600 text-white rounded-xl shadow-lg p-8">

                            <p className="text-lg">
                                Best Prediction
                            </p>

                            <h2 className="text-5xl font-bold mt-4">
                                {prediction["Best Prediction"]} kWh
                            </h2>

                        </div>

                        <div className="bg-green-600 text-white rounded-xl shadow-lg p-8">

                            <p className="text-lg">
                                Estimated Remaining Battery
                            </p>

                            <h2 className="text-5xl font-bold mt-4">
                                {prediction["Estimated Remaining Battery (%)"]} %
                            </h2>

                        </div>

                    </div>

                    <div className="mt-10 bg-white rounded-xl shadow-lg p-6">

                        <h2 className="text-2xl font-bold mb-6">
                            Machine Learning Model Comparison
                        </h2>

                        <table className="w-full">

                            <thead className="bg-gray-100">

                                <tr>

                                    <th className="text-left p-4">
                                        Model
                                    </th>

                                    <th className="text-left p-4">
                                        Predicted Energy
                                    </th>

                                </tr>

                            </thead>

                            <tbody>

                                {Object.entries(prediction)

                                    .filter(

                                        ([model]) =>

                                            ![
                                                "Battery_Voltage_V",
                                                "Vehicle_Weight_kg",
                                                "Driving_Mode",
                                                "Temperature_C",
                                                "Wind",
                                                "Best Prediction",
                                                "Estimated Remaining Battery (%)"
                                            ].includes(model)

                                    )

                                    .map(([model, value]) => (

                                        <tr
                                            key={model}
                                            className="border-b hover:bg-gray-50 transition"
                                        >

                                            <td className="p-4 font-medium">
                                                {model}
                                            </td>

                                            <td className="p-4 text-blue-600 font-semibold">
                                                {value} kWh
                                            </td>

                                        </tr>

                                    ))}

                            </tbody>

                        </table>

                    </div>

                </>

            )}
                        {routeInfo && routeInfo.routes && (

                <div className="mt-10">

                    <h2 className="text-2xl font-bold mb-5">
                        Available Routes
                    </h2>

                    <div className="space-y-4">

                        {routeInfo.routes.map((singleRoute, index) => (

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

                                        {index + 1 === routeInfo.recommended_route && (

                                            <span className="bg-yellow-400 text-black text-sm px-3 py-1 rounded-full">

                                                ⭐ Recommended

                                            </span>

                                        )}

                                    </div>

                                </div>

                                <div className="grid grid-cols-2 gap-6 mt-4">

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

            )}

            {routeInfo && selectedRoute && (

                <div className="mt-12">

                    <h2 className="text-3xl font-bold text-blue-700 mb-6">
                        🗺 Route Map
                    </h2>

                    <RouteMap
                        source={routeInfo.source}
                        destination={routeInfo.destination}
                        route={selectedRoute}
                    />

                </div>

            )}

        </Layout>

    );

}

export default Prediction;