import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

export default function DeleteSection() {
  const navigate = useNavigate();


  const [course, setCourse] = useState("");
  const [section, setSection] = useState("");

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");


  const handleCourseChange = (e) => setCourse(e.target.value);
  const handleSectionChange = (e) => setSection(e.target.value);

  // Form submission handler
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Form validation
    if (!course || !section) {
      alert("All fields are required.");
      return;
    }

    setIsLoading(true);
    let token = localStorage.getItem('token');
    token = token.replace(/^"|"$/g, '');


    try {
      const formData = {
        course,
        section,
      };

      const response = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/sections/${encodeURIComponent(section)}?course_id=${encodeURIComponent(course)}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
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


      alert("Section deleted successfully");
      navigate('/');
    } catch (error) {
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="register-wrapper vh-100">
      <div className="container py-5 h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-12 col-md-8 col-lg-6 col-xl-5">
            <div className="card bg-dark text-white" style={{ borderRadius: "1rem" }}>
              <div className="card-body text-center">
                <h2 className="fw-bold mb-2 text-uppercase">Delete Section</h2>
                <form id="delete-section-form" onSubmit={handleSubmit}>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="course ID"
                      value={course}
                      onChange={handleCourseChange}
                      aria-label="Course ID"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Section ID"
                      value={section}
                      onChange={handleSectionChange}
                      aria-label="Section ID"
                    />
                  </div>
                  <button type="submit" className="btn btn-outline-white btn-lg px-5">
                    {isLoading ? <Loader /> : "Delete Section"}
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
