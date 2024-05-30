import { Link } from "react-router-dom";
export default function CoursesNavbar() {
  return (
    <nav
      className="navbar navbar-expand-lg navbar-light fixed-top"
      id="mainNav"
    >
      <div className="container px-4 px-lg-5">
        <Link to="/">Learniverse</Link>
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
          <li className="nav-item">
              <Link to="/newCourse" className="nav-link">
                Create Course
              </Link>
            </li>
          <li className="nav-item">
              <Link to="/viewMembers" className="nav-link">
                Subscribed members
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/courses" className="nav-link">
                All courses
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/profile" className="nav-link">
                Profile
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}