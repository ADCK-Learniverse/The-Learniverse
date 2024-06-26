import { useContext, useEffect } from "react";
import { Link } from "react-router-dom";
import AppContext from "../../context/AppContext";
import Navbar from "../Navbar/Navbar";
import sendNewsletter from '../../newsletter';

const server = "http://127.0.0.1:8000";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`;


export default function HomePage() {
  const context = useContext(AppContext);
  const token = JSON.parse(localStorage.getItem("token"));

  return (
    <div id="page-top">
      <Navbar location = {"home"} />
      {/* Masthead */}
      <header className="masthead">
        <div className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center">
          <div className="d-flex justify-content-center">
            <div className="text-center">
              <h1 className="mx-auto my-0 text-uppercase">The Learniverse</h1>
              <h2 className="text-white-50 mx-auto mt-2 mb-5">Your new home</h2>
              <a className="btn btn-primary" href="#about">
                Get Started
              </a>
            </div>
          </div>
        </div>
      </header>

      {/* About Section */}
      <section className="about-section text-center" id="about">
        <div className="container px-4 px-lg-5">
          <div className="row gx-4 gx-lg-5 justify-content-center">
            <div className="col-lg-8">
              <h2 className="text-white mb-4">The Better Academy</h2>
              <p className="text-white-50">
                Where students and teachers connect to share knowledge and expertise.
                Teachers have the autonomy to design and offer courses tailored to their expertise,
                 while students have access to a diverse range of learning opportunities.
                 With options for both premium and public courses, learners can choose the level of engagement that suits them best.
                 Through this platform, a vibrant community of learners and educators collaborates to facilitate meaningful learning experiences.
              </p>
            </div>
          </div>
          <img className="img-fluid" src="ipad.png" alt="..." />
        </div>
      </section>

      {/* Projects Section */}
      <section className="projects-section bg-light" id="projects">
        <div className="container px-4 px-lg-5">
          {/* Featured Project Row */}
          <div className="row gx-0 mb-4 mb-lg-5 align-items-center">
            <div className="col-xl-8 col-lg-7">
              <img
                className="img-fluid mb-3 mb-lg-0"
                src="machine-learning.jpg"
                alt="..."
              />
            </div>
            <div className="col-xl-4 col-lg-5">
              <div className="featured-text text-center text-lg-left">
                <h4>Machine Learning</h4>
                <p className="text-black-50 mb-0">
                  Use your data to predict future events with the help of
                  machine learning. This course will walk you through creating a
                  machine learning prediction solution and will introduce
                  Python, the scikit-learn library, and the Jupyter Notebook
                  environment!
                </p>
              </div>
            </div>
          </div>
          {/* Project One Row */}
          <div className="row gx-0 mb-4 mb-lg-5 align-items-center">
            <div className="col-xl-8 col-lg-7">
              <img
                className="img-fluid mb-3 mb-lg-0"
                src="devops.jpg"
                alt="..."
              />
            </div>
            <div className="col-xl-4 col-lg-5">
              <div className="featured-text text-center text-lg-left">
                <h4>Devops</h4>
                <p className="text-black-50 mb-0">
                  Build your DevOps chops with our ever-expanding,
                  constantly-updated library of DevOps training and courses.
                  Whether you’re just finding your footing and figuring out the
                  ins and outs of CI/CD, looking for platform specific AWS
                  DevOps, Azure DevOps, or Google Cloud DevOps, or looking to go
                  deep into advanced DevOps topics, we’ve got you covered.
                </p>
              </div>
            </div>
          </div>
          {/* Project Two Row */}
          <div className="row gx-0 mb-4 mb-lg-5 align-items-center">
            <div className="col-xl-8 col-lg-7">
               <img
                className="img-fluid mb-3 mb-lg-0"
                src="drone.jpg"
                alt="..."
              />
            </div>
            <div className="col-xl-4 col-lg-5">
              <div className="featured-text text-center text-lg-left">
                <h4>Drone Programming</h4>
                <p className="text-black-50 mb-0">
                  Ability to read telemetry data and give commands to autopilot by communicating with ArduPilot using Python programming language.
                  Creating Python scripts with Dronekit library that communicates with ArduPilot.
                  Ability to develop custom Python scripts with PyMAVLink and understanding the MAVLink protocol
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Signup Section */}
      <section className="signup-section" id="signup">
        <div className="container px-4 px-lg-5">
          <div className="row gx-4 gx-lg-5">
            <div className="col-md-10 col-lg-8 mx-auto text-center">
              <i className="far fa-paper-plane fa-2x mb-2 text-white"></i>
              <h2 className="text-white mb-5">Subscribe to receive updates!</h2>
              <form
                className="form-signup"
                id="contactForm"
                data-sb-form-api-token="API_TOKEN"
              >
                <div className="row input-group-newsletter">
                  <div className="col">
                    <input
                      className="form-control"
                      id="emailAddress"
                      type="email"
                      placeholder="Enter email address..."
                      aria-label="Enter email address..."
                      data-sb-validations="required,email"
                    />
                  </div>
                  <div className="col-auto">
                    <button
                      className="btn btn-primary enabled"
                      id="submitButton"
                      type="button"
                      onClick={() => sendNewsletter(document.getElementById('emailAddress').value)}
                    >
                      Notify Me!
                    </button>
                  </div>
                </div>
                <div
                  className="invalid-feedback mt-2"
                  data-sb-feedback="emailAddress:required"
                >
                  An email is required.
                </div>
                <div
                  className="invalid-feedback mt-2"
                  data-sb-feedback="emailAddress:email"
                >
                  Email is not valid.
                </div>
                <div className="d-none" id="submitSuccessMessage">
                  <div className="text-center mb-3 mt-2 text-white">
                    <div className="fw-bolder">Form submission successful!</div>
                    To activate this form, sign up at
                    <br />
                    <a href="https://startbootstrap.com/solution/contact-forms">
                      https://startbootstrap.com/solution/contact-forms
                    </a>
                  </div>
                </div>
                <div className="d-none" id="submitErrorMessage">
                  <div className="text-center text-danger mb-3 mt-2">
                    Error sending message!
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="contact-section bg-black">
        <div className="container px-4 px-lg-5">
          <div className="row gx-4 gx-lg-5">
            <div className="col-md-4 mb-3 mb-md-0">
              <div className="card py-4 h-100">
                <div className="card-body text-center">
                  <i className="fas fa-map-marked-alt text-primary mb-2"></i>
                  <h4 className="bold text-black-50 m-0">Address</h4>
                  <hr className="my-4 mx-auto" />
                  <div className="small text-black-50">
                    Bulgaria
                  </div>
                </div>
              </div>
            </div>
            <div className="col-md-4 mb-3 mb-md-0">
              <div className="card py-4 h-100">
                <div className="card-body text-center">
                  <i className="fas fa-envelope text-primary mb-2"></i>
                  <h4 className="bold text-black-50 m-0">Email</h4>
                  <hr className="my-4 mx-auto" />
                  <div className="small text-black-50">
                    <a href="#!">thelearniverse@gmail.com</a>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-md-4 mb-3 mb-md-0">
              <div className="card py-4 h-100">
                <div className="card-body text-center">
                  <i className="fas fa-mobile-alt text-primary mb-2"></i>
                  <h4 className="bold text-black-50 m-0">Phone</h4>
                  <hr className="my-4 mx-auto" />
                  <div className="small text-black-50">+359 000000000</div>
                </div>
              </div>
            </div>
          </div>
          <div className="social d-flex justify-content-center">
            <a className="mx-2" href="https://x.com/home">
              <i className="fab fa-twitter"></i>
            </a>
            <a className="mx-2" href="https://www.youtube.com/">
              <i className="fab fa-youtube"></i>
            </a>
            <a className="mx-2" href="https://github.com/Alexandur11">
              <i className="fab fa-github"></i>
            </a>
            <a className="mx-2" href="https://github.com/ChavdarKostadinov98">
              <i className="fab fa-github"></i>
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer bg-black small text-center text-white-50">
        <div className="container px-4 px-lg-5">
          Copyright &copy; ADCK Learniverse
        </div>
      </footer>

      {/* Bootstrap core JS */}
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
      {/* Core theme JS */}
      <script src="js/scripts.js"></script>
      {/* SB Forms JS */}
      <script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>
    </div>
  );
}
