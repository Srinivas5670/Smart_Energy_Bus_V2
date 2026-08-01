import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Dashboard() {
    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {
        loadDashboard();
    }, []);

    const loadDashboard = async () => {
        try {
            const response = await api.get("/dashboard");
            setDashboard(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    if (!dashboard) {
        return (
            <Layout>
                <div className="text-center text-2xl mt-10">
                    Loading Dashboard...
                </div>
            </Layout>
        );
    }

    return (
        <Layout>

            <h2 className="text-3xl font-bold mb-8">
                Dashboard
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                <div className="bg-white rounded-xl shadow p-6">
                    <p className="text-gray-500">Total Predictions</p>
                    <h2 className="text-3xl font-bold">
                        {dashboard.analytics.total_predictions}
                    </h2>
                </div>

                <div className="bg-white rounded-xl shadow p-6">
                    <p className="text-gray-500">Average Energy</p>
                    <h2 className="text-3xl font-bold">
                        {dashboard.analytics.average_energy
                            ? dashboard.analytics.average_energy.toFixed(2)
                            : "0.00"}{" "}
                        kWh
                    </h2>
                </div>

                <div className="bg-white rounded-xl shadow p-6">
                    <p className="text-gray-500">Highest Energy</p>
                    <h2 className="text-3xl font-bold">
                        {dashboard.analytics.highest_energy
                            ? dashboard.analytics.highest_energy.toFixed(2)
                            : "0.00"}{" "}
                        kWh
                    </h2>
                </div>

                <div className="bg-white rounded-xl shadow p-6">
                    <p className="text-gray-500">Lowest Energy</p>
                    <h2 className="text-3xl font-bold">
                        {dashboard.analytics.lowest_energy
                            ? dashboard.analytics.lowest_energy.toFixed(2)
                            : "0.00"}{" "}
                        kWh
                    </h2>
                </div>

            </div>

            <div className="bg-white rounded-xl shadow mt-10 p-6">

                <h3 className="text-2xl font-bold mb-4">
                    Recent Predictions
                </h3>

                <table className="w-full">

                    <thead>

                        <tr className="border-b">

                            <th className="text-left p-3">Speed</th>
                            <th className="text-left p-3">Battery</th>
                            <th className="text-left p-3">Energy</th>
                            <th className="text-left p-3">Date</th>

                        </tr>

                    </thead>

                    <tbody>

                        {dashboard.recent_predictions.length === 0 ? (
                            <tr>
                                <td
                                    colSpan="4"
                                    className="text-center p-6"
                                >
                                    No predictions available.
                                </td>
                            </tr>
                        ) : (
                            dashboard.recent_predictions.map((item) => (
                                <tr key={item.id} className="border-b">

                                    <td className="p-3">
                                        {item.speed_kmh}
                                    </td>

                                    <td className="p-3">
                                        {item.battery_state}%
                                    </td>

                                    <td className="p-3">
                                        {item.voting_prediction} kWh
                                    </td>

                                    <td className="p-3">
                                        {item.created_at}
                                    </td>

                                </tr>
                            ))
                        )}

                    </tbody>

                </table>

            </div>

        </Layout>
    );
}

export default Dashboard;