import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import AppContext from "../../context/AppContext";
import "./Navbar.css";

export default function Navbar({ location }) {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const locationLowerCase = location.toLowerCase();
  const context = useContext(AppContext);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 50) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    alert("Logging out");
    window.location.href = "/";
  };

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  return (
    <nav className={`navbar navbar-expand-lg navbar-light fixed-top ${scrolled ? "navbar-scrolled" : ""}`} id="mainNav">
      <div className="container px-4 px-lg-5">
        <li className="nav-item">
          <Link to="/" className="navbar-brand">
            The Learniverse
          </Link>
        </li>
        <button
          className="navbar-toggler navbar-toggler-right"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive"
          aria-controls="navbarResponsive"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          Menu
          <i className="fas fa-bars"></i>
        </button>
        <div className="collapse navbar-collapse" id="navbarResponsive">
          <ul className="navbar-nav ms-auto">
            {locationLowerCase === "home" && (
              <>
                <li className="nav-item">
                  <a className="nav-link" href="#about">
                    About
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#projects">
                    Best Courses
                  </a>
                </li>
                <li className="nav-item">
                  <Link to="/courses" className="nav-link">
                    All courses
                  </Link>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#signup">
                    Newsletter
                  </a>
                </li>
                {!context.token && (
                  <li className="nav-item">
                    <Link to="/login" className="nav-link">
                      Step into the Universe
                    </Link>
                  </li>
                )}
                {context.token && (
                  <li className={`nav-item dropdown ${dropdownOpen ? "open" : ""}`}>
                    <button className="profile-btn nav-link" onClick={toggleDropdown}>
                      Menu
                    </button>
                    <div className="dropdown-content">
                      <Link to="/profile" className="nav-link">Profile</Link>
                      <Link to="/student/requests" className="nav-link">Student Requests</Link>
                      <Link to="/teacher/requests" className="nav-link">Teacher Requests</Link>
                      <Link to="/control-panel" className="nav-link">O/A Dashboard</Link>
                      <Link to="/" className="nav-link" onClick={logout}>Logout</Link>
                    </div>
                  </li>
                )}
              </>
            )}
            {locationLowerCase === "courses" && (
              <>
                {context.token && (
                  <li className="nav-item">
                    <Link to="/courses/create-course" className="nav-link">
                      Create Course
                    </Link>
                  </li>
                )}
                {context.token && (
                  <li className="nav-item">
                    <Link to="/courses/delete-course" className="nav-link">
                      Delete Course
                    </Link>
                  </li>
                )}
                {context.token && (
                  <li className={`nav-item dropdown ${dropdownOpen ? "open" : ""}`}>
                    <button className="profile-btn nav-link" onClick={toggleDropdown}>
                      Menu
                    </button>
                    <div className="dropdown-content">
                      <Link to="/profile" className="nav-link">Profile</Link>
                      <Link to="/student/requests" className="nav-link">Student Requests</Link>
                      <Link to="/teacher/requests" className="nav-link">Teacher Requests</Link>
                      <Link to="/" className="nav-link" onClick={logout}>Logout</Link>
                    </div>
                  </li>
                )}
              </>
            )}
            {locationLowerCase === "admin" && (
              <>
                {context.token && (
                  <li className="nav-item">
                    <Link to="" className="nav-link">
                      Analytics
                    </Link>
                  </li>
                )}
                {context.token && (
                  <li className={`nav-item dropdown ${dropdownOpen ? "open" : ""}`}>
                    <button className="profile-btn nav-link" onClick={toggleDropdown}>
                      Menu
                    </button>
                    <div className="dropdown-content">
                      <Link to="/profile" className="nav-link">Profile</Link>
                      <Link to="/student/requests" className="nav-link">Student Requests</Link>
                      <Link to="/teacher/requests" className="nav-link">Teacher Requests</Link>
                      <Link to="/" className="nav-link" onClick={logout}>Logout</Link>
                    </div>
                  </li>
                )}
              </>
            )}
            {locationLowerCase === "course/sections/" && (
              <>
                <li className="nav-item">
                  <Link to="/sections/create-section/" className="nav-link">
                    Create Section
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="/sections/delete-section/" className="nav-link">
                    Delete Section
                  </Link>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/course/subscribedMembers">
                    Subscribed Members
                  </a>
                </li>
                {context.token && (
                  <li className={`nav-item dropdown ${dropdownOpen ? "open" : ""}`}>
                    <button className="profile-btn nav-link" onClick={toggleDropdown}>
                      Menu
                    </button>
                    <div className="dropdown-content">
                      <Link to="/profile" className="nav-link">Profile</Link>
                      <Link to="/" className="nav-link" onClick={logout}>Logout</Link>
                    </div>
                  </li>
                )}
              </>
            )}
            {locationLowerCase === "profile" && (
              <>
                <li className="nav-item">
                  <Link to="/courses" className="nav-link">
                    All courses
                  </Link>
                </li>
                {context.token && (
                  <li className="nav-item">
                    <Link to="/profile/password" className="nav-link">
                      Change Password
                    </Link>
                  </li>
                )}
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}
