import { Link, useNavigate } from "react-router-dom";
import "./Login.style.css";
import { useState, useEffect } from "react";
import { useAuth } from "../../hooks/useAuth";
import Loader from "../Loader/Loader";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { appState, isLoading, error, login } = useAuth();
  const navigate = useNavigate();

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!username || !password) {
      return;
    }

    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    await login(formData);
  };

  useEffect(() => {
    if (appState && appState.token) {
      console.log("App state after login:", appState); // Log statement
      alert("Successful login");
      navigate("/");
    }
  }, [appState, navigate]);

  if (isLoading) {
    return <Loader />;
  }

  return (
    <div className="container-background-image">
      <div className="go-back-container">
        <Link to="/" className="go-back-btn">
          ← Go back
        </Link>
      </div>

      <div className="container-wrapper">
        <div className="forms">
          <h1>Login</h1>
          <form id="login-form" onSubmit={handleSubmit}>
            <label htmlFor="username">
              <span className="input-label">Username</span>
              <input
                type="text"
                id="username"
                name="username"
                value={username}
                placeholder="Enter username"
                onChange={handleUsernameChange}
                required
              />
            </label>
            <label htmlFor="password">
              <span className="input-label">Password</span>
              <input
                type="password"
                id="password"
                name="password"
                value={password}
                placeholder="************"
                onChange={handlePasswordChange}
                required
              />
            </label>
            <button type="submit" className="button" id="loginBtn">
              Login
            </button>
          </form>
          <form id="register-form" method="post">
            <button
              href="http://localhost:63342/Forum-System-API/frontend/register_page.html?_ijt=9oj1a5ec2q6l52obc4ccf2acs1&_ij_reload=RELOAD_ON_SAVE"
              className="register-btn"
            >
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}