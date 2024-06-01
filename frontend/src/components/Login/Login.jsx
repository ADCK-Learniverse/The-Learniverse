import { Link, useNavigate } from "react-router-dom";
import "./Login.style.css";
import { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import Loader from "../Loader/Loader";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { appState, isLoading, error, login } = useAuth(username, password);
  const navigate = useNavigate();

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!username) {
      return;
    }

    if (!password) {
      return;
    }
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    login(formData);

    if (appState !== null) {
      alert("successful login");
      window.location.href = "/";
      localStorage.setItem('token', token);
    }
  };

  if (isLoading) {
    return <Loader />;
  }

  return (
    <>
      <section className="login-wrapper vh-100">
        <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div
                className="card bg-dark text-white"
                style={{
                  borderRadius: "1rem",
                }}
              >
                <div className="card-body text-center">
                  <div className="">
                    <h2 className="fw-bold mb-2 text-uppercase">Login</h2>
                    <p className="text-white-50 mb-5">
                      Please enter your email and password!
                    </p>

                    <form onSubmit={handleSubmit}>
                      <div
                        data-mdb-input-init
                        className="form-outline form-white mb-4"
                      >
                        <input
                          type="email"
                          id="typeEmailX"
                          className="form-control form-control-lg"
                          onChange={handleUsernameChange}
                        />
                        <label className="form-label" htmlFor="typeEmailX">
                          Email
                        </label>
                      </div>

                      <div
                        data-mdb-input-init
                        className="form-outline form-white mb-4"
                      >
                        <input
                          type="password"
                          id="typePasswordX"
                          className="form-control form-control-lg"
                          onChange={handlePasswordChange}
                        />
                        <label className="form-label" htmlFor="typePasswordX">
                          Password
                        </label>
                      </div>

                      <p className="small mb-5 pb-lg-2">
                        <a className="text-white-50" href="#!">
                          Forgot password?
                        </a>
                      </p>

                      <button
                        data-mdb-button-init
                        data-mdb-ripple-init
                        className="btn btn-outline-white btn-lg px-5"
                        type="submit"
                      >
                        Login
                      </button>
                    </form>

                    <div className="d-flex justify-content-center text-center mt-4 pt-1">
                      <a href="#!" className="text-black">
                        <i className="fab fa-facebook-f fa-lg"></i>
                      </a>
                      <a href="#!" className="text-black">
                        <i className="fab fa-twitter fa-lg mx-4 px-2"></i>
                      </a>
                      <a href="#!" className="text-black">
                        <i className="fab fa-google fa-lg"></i>
                      </a>
                    </div>
                  </div>

                  <div>
                    <p className="mb-0">
                      Don't have an account?{" "}
                      <Link to="/register/teachers" className="text-white-50 fw-bold">
                        Sign Up as Teacher
                      </Link>
                    </p>
                    <p className="mb-0">
                      Don't have an account?{" "}
                      <Link to="/register/students" className="text-white-50 fw-bold">
                        Sign Up as Student
                      </Link>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
