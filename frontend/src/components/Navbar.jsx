import { FaBars } from "react-icons/fa";

function Navbar({ toggleSidebar }) {

    return (

        <div className="bg-white shadow flex items-center px-4 md:px-8 py-4">

            {/* Mobile Menu */}

            <button
                onClick={toggleSidebar}
                className="md:hidden mr-4 text-slate-900"
            >
                <FaBars size={22} />
            </button>

            <div>

                <h1 className="text-2xl font-bold">
                    Smart Energy Bus V2
                </h1>

                <p className="text-gray-500">
                    AI Powered Energy Prediction System
                </p>

            </div>

        </div>

    );

}

export default Navbar;