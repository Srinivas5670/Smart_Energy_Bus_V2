import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import api from "../services/api";

function Register() {

    const navigate = useNavigate();

    // ==========================
    // Form State
    // ==========================

    const [fullName, setFullName] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [confirmPassword, setConfirmPassword] = useState("");

    const [loading, setLoading] = useState(false);

    // ==========================
    // Register
    // ==========================

    const register = async (e) => {

        e.preventDefault();

        if (
            !fullName ||
            !email ||
            !password ||
            !confirmPassword
        ) {

            alert("Please fill all fields.");

            return;

        }

        if (password !== confirmPassword) {

            alert("Passwords do not match.");

            return;

        }

        if (password.length < 6) {

            alert("Password must be at least 6 characters.");

            return;

        }

        setLoading(true);

        try {

            await api.post("/register", {

                full_name: fullName,

                email,

                password

            });

            alert("Registration successful.");

            navigate("/");

        }

        catch (error) {

            console.error(error);

            alert(

                error.response?.data?.message ||

                "Registration failed."

            );

        }

        finally {

            setLoading(false);

        }

    };
    return (

    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-white to-blue-100 flex items-center justify-center p-6">

        <div className="w-full max-w-6xl bg-white rounded-3xl shadow-2xl overflow-hidden grid lg:grid-cols-2">

            {/* ================= Left Panel ================= */}

            <div className="flex items-center justify-center p-8 lg:p-14">

                <form
                    onSubmit={register}
                    className="w-full max-w-md"
                >

                    <h2 className="text-4xl font-bold text-gray-800 mb-2">

                        Create Account

                    </h2>

                    <p className="text-gray-500 mb-10">

                        Join Smart Energy Bus V2

                    </p>

                    {/* Full Name */}

                    <div className="mb-5">

                        <label className="block text-sm font-medium text-gray-700 mb-2">

                            Full Name

                        </label>

                        <input
                            type="text"
                            placeholder="Enter your full name"
                            value={fullName}
                            onChange={(e) => setFullName(e.target.value)}
                            className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 transition"
                        />

                    </div>

                    {/* Email */}

                    <div className="mb-5">

                        <label className="block text-sm font-medium text-gray-700 mb-2">

                            Email

                        </label>

                        <input
                            type="email"
                            placeholder="Enter your email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 transition"
                        />

                    </div>

                    {/* Password */}

                    <div className="mb-5">

                        <label className="block text-sm font-medium text-gray-700 mb-2">

                            Password

                        </label>

                        <input
                            type="password"
                            placeholder="Enter your password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 transition"
                        />

                    </div>

                    {/* Confirm Password */}

                    <div className="mb-6">

                        <label className="block text-sm font-medium text-gray-700 mb-2">

                            Confirm Password

                        </label>

                        <input
                            type="password"
                            placeholder="Confirm your password"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 transition"
                        />

                    </div>
                                        {/* Register Button */}

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-gradient-to-r from-red-600 to-orange-500 text-white py-3 rounded-xl font-semibold text-lg shadow-lg hover:shadow-xl hover:scale-[1.02] transition-all duration-300 disabled:opacity-60 disabled:cursor-not-allowed"
                    >

                        {loading ? (

                            <div className="flex items-center justify-center gap-3">

                                <svg
                                    className="animate-spin h-5 w-5"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <circle
                                        className="opacity-25"
                                        cx="12"
                                        cy="12"
                                        r="10"
                                        stroke="currentColor"
                                        strokeWidth="4"
                                    />

                                    <path
                                        className="opacity-75"
                                        fill="currentColor"
                                        d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                                    />

                                </svg>

                                Creating Account...

                            </div>

                        ) : (

                            "Create Account"

                        )}

                    </button>

                    {/* Divider */}

                    <div className="flex items-center my-8">

                        <div className="flex-1 h-px bg-gray-300"></div>

                        <span className="mx-4 text-sm text-gray-500">

                            OR

                        </span>

                        <div className="flex-1 h-px bg-gray-300"></div>

                    </div>

                    <p className="text-center text-gray-600">

                        Already have an account?

                        <Link
                            to="/"
                            className="ml-2 text-red-600 font-semibold hover:underline"
                        >
                            Sign In
                        </Link>

                    </p>

                </form>

            </div>

            {/* ================= Right Panel ================= */}

            <div className="hidden lg:flex flex-col justify-center items-center bg-gradient-to-br from-red-600 via-red-500 to-orange-500 text-white p-14">

                <div className="text-7xl mb-6">

                    👋

                </div>

                <h1 className="text-5xl font-bold mb-6 text-center">

                    Join Us!

                </h1>

                <p className="text-center text-lg opacity-90 leading-8">

                    Create your Smart Energy Bus account

                    <br />

                    to predict energy consumption,

                    optimize intelligent routes,

                    and manage your journey

                    from one modern dashboard.

                </p>

                <div className="mt-12">

                    <Link
                        to="/"
                        className="border-2 border-white rounded-full px-10 py-3 hover:bg-white hover:text-red-600 transition-all duration-300 font-semibold"
                    >
                        Sign In
                    </Link>

                </div>

            </div>

        </div>

    </div>

);

}

export default Register;