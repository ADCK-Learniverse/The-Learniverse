import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

export default function ChangePassword() {
    const [password, setPassword] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!password) {
            alert("All fields are required");
            return;
        }

        setIsLoading(true);
        let token = localStorage.getItem('token');

        try {
            const response = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/teacher_panel/password?password=${encodeURIComponent(password)}`, {
                method: "PUT",
                headers: {
                    Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
                },
            });

            if (!response.ok) {
                const errorMessage = await response.text();
                if (response.status === 422) {
                    alert("Validation error: " + errorMessage);
                } else if (response.status === 409) {
                    alert("Conflict error: " + errorMessage);
                } else {
                    throw new Error("Server error: " + errorMessage);
                }
                return;
            }

            alert("Password changed successfully");
            navigate('/profile');
        } catch (error) {
            setError(error.message);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <section style={{ background: 'linear-gradient(135deg, #1c1c3c, #3a3a80)', color: '#fff', padding: '235px' }}>
            <div className="container py-5 h-100">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                        <div className="card bg-dark text-white" style={{ borderRadius: "1rem" }}>
                            <div className="card-body text-center">
                                <h2 className="f2-bold mb-2 text-uppercase">Change Password</h2>
                                <form id="change-password-form" onSubmit={handleSubmit}>
                                    <div className="form-outline mb-4">
                                        <input
                                            type="text"
                                            className="form-control-lg"
                                            placeholder="Password"
                                            value={password}
                                            onChange={handlePasswordChange}
                                            id="password-change"
                                            aria-label="Password"
                                        />
                                    </div>
                                    <button type="submit" className="btn btn-outline-white btn-lg px-5">
                                        {isLoading ? <Loader /> : "Change Password"}
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
