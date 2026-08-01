import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Analytics() {

    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {
        loadAnalytics();
    }, []);

    const loadAnalytics = async () => {

        try {

            const response = await api.get("/analytics");

            setAnalytics(response.data.analytics);

        } catch (error) {

            console.log(error);

        }

    };

    if (!analytics) {
        return (
            <Layout>
                <h2 className="text-2xl font-bold">
                    Loading Analytics...
                </h2>
            </Layout>
        );
    }

    return (

        <Layout>

            <h2 className="text-3xl font-bold mb-8">
                Analytics
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                <div className="bg-white shadow rounded-xl p-6">

                    <p className="text-gray-500">
                        Total Predictions
                    </p>

                    <h2 className="text-4xl font-bold">
                        {analytics.total_predictions}
                    </h2>

                </div>

                <div className="bg-white shadow rounded-xl p-6">

                    <p className="text-gray-500">
                        Average Energy
                    </p>

                    <h2 className="text-4xl font-bold">
                        {analytics.average_energy?.toFixed(2)} kWh
                    </h2>

                </div>

                <div className="bg-white shadow rounded-xl p-6">

                    <p className="text-gray-500">
                        Maximum Energy
                    </p>

                    <h2 className="text-4xl font-bold">
                        {analytics.max_energy?.toFixed(2)} kWh
                    </h2>

                </div>

                <div className="bg-white shadow rounded-xl p-6">

                    <p className="text-gray-500">
                        Minimum Energy
                    </p>

                    <h2 className="text-4xl font-bold">
                        {analytics.min_energy?.toFixed(2)} kWh
                    </h2>

                </div>

            </div>

        </Layout>

    );

}

export default Analytics;