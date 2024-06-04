/* eslint-disable react/prop-types */
import { Link } from "react-router-dom";

export default function Navbar({ location }) {
  const locationLowerCase = location.toLowerCase();

  return (
    <nav className="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div className="container px-4 px-lg-5">
        <li className="nav-item">
          <Link to="/" className="nav-link">
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
                <li className="nav-item">
                  <Link to="/login" className="nav-link">
                    Step into the Universe
                  </Link>
                </li>
              </>
            )}
            {locationLowerCase === "courses" && (
              <>
                <li className="nav-item">
                  <Link to="/courses/create-course" className="nav-link">
                    Create Course
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="/profile" className="nav-link">
                    Profile
                  </Link>
                </li>
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
                  <a className="nav-link" href="/course/subscribedMembers">
                    Subscribed Members
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#profile">
                    Profile
                  </a>
                </li>
              </>
            )}
            {locationLowerCase === "profile" && (
              <>
                <li className="nav-item">
                  <Link to="/courses" className="nav-link">
                    All courses
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}
