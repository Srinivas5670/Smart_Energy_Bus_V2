import { NavLink, useNavigate } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");
        navigate("/");

    };

    return (

        <div className="w-64 h-screen bg-slate-900 text-white">

            <div className="text-2xl font-bold p-6 border-b border-slate-700">
                Smart Energy Bus
            </div>

            <nav className="mt-6 flex flex-col">

                <NavLink
                    to="/dashboard"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    Dashboard
                </NavLink>

                <NavLink
                    to="/prediction"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    Prediction
                </NavLink>

                <NavLink
                    to="/history"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    History
                </NavLink>

                <NavLink
                    to="/analytics"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    Analytics
                </NavLink>

                <NavLink
                    to="/route"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    Route Optimization
                </NavLink>

                <NavLink
                    to="/profile"
                    className="px-6 py-3 hover:bg-slate-700"
                >
                    Profile
                </NavLink>

            </nav>

        </div>

    );

}

export default Sidebar;