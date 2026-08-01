import { useState } from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

function Layout({ children }) {

    const [sidebarOpen, setSidebarOpen] = useState(false);

    return (

        <div className="flex min-h-screen bg-gray-100">

            {/* Mobile Overlay */}

            {sidebarOpen && (

                <div
                    className="fixed inset-0 bg-black bg-opacity-40 z-30 md:hidden"
                    onClick={() => setSidebarOpen(false)}
                />

            )}

            {/* Sidebar */}

            <div
                className={`
                    fixed md:static z-40 h-full
                    transform transition-transform duration-300
                    ${sidebarOpen ? "translate-x-0" : "-translate-x-full"}
                    md:translate-x-0
                `}
            >

                <Sidebar />

            </div>

            {/* Main Content */}

            <div className="flex-1 flex flex-col">

                <Navbar
                    toggleSidebar={() => setSidebarOpen(!sidebarOpen)}
                />

                <main className="flex-1 w-full p-4 md:p-8">

                    {children}

                </main>

            </div>

        </div>

    );

}

export default Layout;