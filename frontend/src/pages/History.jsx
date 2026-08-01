import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function History() {

    const [history, setHistory] = useState([]);

    useEffect(() => {
        loadHistory();
    }, []);

    const loadHistory = async () => {

        try {

            const response = await api.get("/history");

            setHistory(response.data.history);

        } catch (error) {

            console.log(error);

        }

    };

    const deletePrediction = async (id) => {

        if (!window.confirm("Delete this prediction?"))
            return;

        try {

            await api.delete(`/history/${id}`);

            loadHistory();

        } catch (error) {

            alert(
                error.response?.data?.message ||
                "Delete Failed"
            );

        }

    };

const exportCSV = async () => {

    try {

        const token = localStorage.getItem("token");

        const response = await fetch(
            "http://127.0.0.1:5000/export/csv",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        if (!response.ok) {

            throw new Error("Export failed");

        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "prediction_history.csv";

        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);

    }

    catch (error) {

        alert("Failed to export CSV.");

        console.error(error);

    }

};

    return (

        <Layout>

            <div className="flex justify-between items-center mb-6">

                <h2 className="text-3xl font-bold">
                    Prediction History
                </h2>

                <button
                    onClick={exportCSV}
                    className="bg-green-600 text-white px-5 py-2 rounded"
                >
                    Export CSV
                </button>

            </div>

            <div className="bg-white rounded-xl shadow overflow-auto">

                <table className="w-full">

                    <thead className="bg-gray-100">

                        <tr>

                            <th className="p-3">Date</th>
                            <th className="p-3">Speed</th>
                            <th className="p-3">Battery</th>
                            <th className="p-3">Energy</th>
                            <th className="p-3">Action</th>

                        </tr>

                    </thead>

                    <tbody>

                        {history.map((item) => (

                            <tr
                                key={item.id}
                                className="border-b text-center"
                            >

                                <td className="p-3">
                                    {item.created_at}
                                </td>

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

                                    <button
                                        onClick={() => deletePrediction(item.id)}
                                        className="bg-red-600 text-white px-3 py-1 rounded"
                                    >
                                        Delete
                                    </button>

                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </Layout>

    );

}

export default History;