import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import Loader from "../Loader/Loader";
import { userRegistration } from "../../hooks/registrationHook";
import "./Register.style.css";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [phonenumber, setPhonenumber] = useState("");
  const { appState, isLoading, error, register } = userRegistration();
  const navigate = useNavigate();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleFirstnameChange = (e) => {
    setFirstname(e.target.value);
  };

  const handleLastnameChange = (e) => {
    setLastname(e.target.value);
  };

  const handlePhonenumberChange = (e) => {
    setPhonenumber(e.target.value);
  };

      const handleSubmit = async (e) => {
      e.preventDefault();

      if (!email || !password || !firstname || !lastname || !phonenumber) {
        alert("All fields are required.");
        return;
      }

      const formData = {
        email,
        password,
        firstname,
        lastname,
        phone_number: phonenumber
      };

      try {
        const response = await fetch('http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/register/teacher', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(formData)
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

        alert("Successful registration");
        navigate("/");
      } catch (error) {
        alert("Registration failed: " + error.message);
      }
    };

  return (
    <>
      <section className="register-wrapper vh-100">
        <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div className="card bg-dark text-white" style={{ borderRadius: "1rem" }}>
                <div className="card-body text-center">
                  <div className="">
                    <h2 className="fw-bold mb-2 text-uppercase">Register</h2>
                    <form id="teacher-registration-form" onSubmit={handleSubmit}>
                      <div className="form-outline mb-4">
                        <input
                          type="email"
                          className="form-control-lg"
                          placeholder="Email"
                          value={email}
                          onChange={handleEmailChange}
                          id="teacher-email"
                        />
                      </div>
                      <div className="form-outline mb-4">
                        <input
                          type="password"
                          className="form-control-lg"
                          placeholder="Password"
                          value={password}
                          onChange={handlePasswordChange}
                          id="teacher-password"
                        />
                      </div>
                      <div className="form-outline mb-4">
                        <input
                          type="text"
                          className="form-control-lg"
                          placeholder="First Name"
                          value={firstname}
                          onChange={handleFirstnameChange}
                          id="teacher-firstname"
                        />
                      </div>
                      <div className="form-outline mb-4">
                        <input
                          type="text"
                          className="form-control-lg"
                          placeholder="Last Name"
                          value={lastname}
                          onChange={handleLastnameChange}
                          id="teacher-lastname"
                        />
                      </div>
                      <div className="form-outline mb-4">
                        <input
                          type="tel"
                          className="form-control-lg"
                          placeholder="Phone Number"
                          value={phonenumber}
                          onChange={handlePhonenumberChange}
                          id="teacher-phone"
                        />
                      </div>
                      <button type="submit" className="btn btn-outline-white btn-lg px-5">
                        {isLoading ? <Loader /> : "Register"}
                      </button>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};
