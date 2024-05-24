import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import Loader from "../Loader/Loader";
import { useAuth } from "../hooks/useAuth"; // Ensure this hook is correctly imported

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [phonenumber, setPhonenumber] = useState("");
  const { appState, isLoading, error, register } = useAuth();
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

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email || !password || !firstname || !lastname || !phonenumber) {
      alert("All fields are required.");
      return;
    }

    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    formData.append("firstname", firstname);
    formData.append("lastname", lastname);
    formData.append("phonenumber", phonenumber);

    register(formData)
      .then(() => {
        alert("Successful registration");
        navigate("/");
      })
      .catch((error) => {
        alert("Registration failed: " + error.message);
      });
  };

  return (
    <div className="register-container">
      <h2>Register</h2>
      {isLoading ? (
        <Loader />
      ) : (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Email:</label>
            <input
              type="email"
              value={email}
              onChange={handleEmailChange}
              required
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={handlePasswordChange}
              required
            />
          </div>
          <div>
            <label>First Name:</label>
            <input
              type="text"
              value={firstname}
              onChange={handleFirstnameChange}
              required
            />
          </div>
          <div>
            <label>Last Name:</label>
            <input
              type="text"
              value={lastname}
              onChange={handleLastnameChange}
              required
            />
          </div>
          <div>
            <label>Phone Number:</label>
            <input
              type="tel"
              value={phonenumber}
              onChange={handlePhonenumberChange}
              required
            />
          </div>
          {error && <p className="error">{error.message}</p>}
          <button type="submit">Register</button>
        </form>
      )}
      <Link to="/login">Already have an account? Login here.</Link>
    </div>
  );
}
