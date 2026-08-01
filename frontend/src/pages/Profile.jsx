import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";

function Profile() {

    const navigate = useNavigate();

    const [profile, setProfile] = useState({
        full_name: "",
        email: ""
    });

    const [password, setPassword] = useState({
        current_password: "",
        new_password: ""
    });

    useEffect(() => {
        loadProfile();
    }, []);

    const loadProfile = async () => {

        try {

            const response = await api.get("/profile");

            setProfile(response.data.profile);

        } catch (error) {

            console.log(error);

        }

    };

    const updateProfile = async (e) => {

        e.preventDefault();

        try {

            await api.put("/profile", {
                full_name: profile.full_name,
                email: profile.email
            });

            alert("Profile updated successfully.");

        } catch (error) {

            alert(
                error.response?.data?.message ||
                "Update failed."
            );

        }

    };

    const changePassword = async (e) => {

        e.preventDefault();

        try {

            await api.put("/change-password", password);

            alert("Password changed successfully.");

            setPassword({
                current_password: "",
                new_password: ""
            });

        } catch (error) {

            alert(
                error.response?.data?.message ||
                "Password change failed."
            );

        }

    };

    const logout = () => {

        localStorage.removeItem("token");

        navigate("/");

    };

    return (
                <Layout>

            <h1 className="text-3xl font-bold mb-8">
                Profile
            </h1>

            <div className="grid md:grid-cols-2 gap-8">

                {/* Personal Information */}

                <div className="bg-white shadow rounded-xl p-6">

                    <h2 className="text-2xl font-bold mb-5">
                        Personal Information
                    </h2>

                    <form onSubmit={updateProfile}>

                        <input
                            type="text"
                            value={profile.full_name}
                            onChange={(e) =>
                                setProfile({
                                    ...profile,
                                    full_name: e.target.value
                                })
                            }
                            className="w-full border rounded p-3 mb-4"
                            placeholder="Full Name"
                        />

                        <input
                            type="email"
                            value={profile.email}
                            onChange={(e) =>
                                setProfile({
                                    ...profile,
                                    email: e.target.value
                                })
                            }
                            className="w-full border rounded p-3 mb-4"
                            placeholder="Email"
                        />

                        <button
                            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded"
                        >
                            Update Profile
                        </button>

                    </form>

                </div>

                {/* Change Password */}

                <div className="bg-white shadow rounded-xl p-6">

                    <h2 className="text-2xl font-bold mb-5">
                        Change Password
                    </h2>

                    <form onSubmit={changePassword}>

                        <input
                            type="password"
                            placeholder="Current Password"
                            value={password.current_password}
                            onChange={(e) =>
                                setPassword({
                                    ...password,
                                    current_password: e.target.value
                                })
                            }
                            className="w-full border rounded p-3 mb-4"
                        />

                        <input
                            type="password"
                            placeholder="New Password"
                            value={password.new_password}
                            onChange={(e) =>
                                setPassword({
                                    ...password,
                                    new_password: e.target.value
                                })
                            }
                            className="w-full border rounded p-3 mb-4"
                        />

                        <button
                            className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded"
                        >
                            Change Password
                        </button>

                    </form>

                </div>

            </div>

            {/* Logout Section */}

            <div className="mt-10 bg-white shadow rounded-xl p-6">

                <h2 className="text-2xl font-bold text-red-600 mb-4">
                    Account
                </h2>

                <p className="text-gray-600 mb-6">
                    Click the button below to securely log out of your account.
                </p>

                <button
                    onClick={logout}
                    className="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-lg font-semibold"
                >
                    Logout
                </button>

            </div>

        </Layout>

    );

}

export default Profile;