import { useContext, useEffect } from "react";
import { Link } from "react-router-dom";
import AppContext from "../../context/AppContext";
import './Home_page.css';



const server = "http://127.0.0.1:8000";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`;
const token = JSON.parse(localStorage.getItem('token'));

export default function HomePage() {
  const context = useContext(AppContext);

  return (
    <div id="page-top">
      {/* Navigation */}
      <nav className="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
        <div className="container px-4 px-lg-5">
          <a className="navbar-brand" href="#page-top">Learniverse</a>
          <button className="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i className="fas fa-bars"></i>
          </button>
          <div className="collapse navbar-collapse" id="navbarResponsive">
{/*             <ul className="navbar-nav ms-auto"> */}
{/*               <li className="nav-item"><a className="nav-link" href="#about">About</a></li> */}
{/*               <li className="nav-item"><a className="nav-link" href="#projects">Best Courses</a></li> */}
{/*               <li className="nav-item"><a className="nav-link" href="/src/components/Courses/Courses.html">All Courses</a></li> */}
{/*               <li className="nav-item"><a className="nav-link" href="#signup">Newsletter</a></li> */}
{/*               <li className="nav-item"><a className="nav-link" href="/src/components/Login/Login_page.html">Step into the Universe</a></li> */}
{/*             </ul> */}
          </div>
        </div>
      </nav>

      {/* Masthead */}
      <header className="masthead">
        <div className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center">
          <div className="d-flex justify-content-center">
            <div className="text-center">
              <h1 className="mx-auto my-0 text-uppercase">The Learniverse</h1>
              <h2 className="text-white-50 mx-auto mt-2 mb-5">Your new home</h2>
              <a className="btn btn-primary" href="#about">Get Started</a>
            </div>
          </div>
        </div>
      </header>
  );
};