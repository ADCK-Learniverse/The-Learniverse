import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

export default function DeleteSection() {
  const navigate = useNavigate();

  const [course, setCourse] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");


  const handleCourseChange = (e) => setCourse(e.target.value);

  // Form submission handler
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Form validation
    if (!course) {
      alert("All fields are required.");
      return;
    }

    setIsLoading(true);
    let token = localStorage.getItem('token');
    token = token.replace(/^"|"$/g, '');


    try {
      const formData = {
        course,
      };

      const response = await fetch(`http://127.0.0.1:8000/courses/?course_id=${encodeURIComponent(course)}`, {
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

        alert("Course deleted successfully");

        return;
      }


      alert("Course deleted successfully");
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
                <h2 className="fw-bold mb-2 text-uppercase">Delete Course</h2>
                <form id="delete-course-form" onSubmit={handleSubmit}>
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
                  <button type="submit" className="btn btn-outline-white btn-lg px-5">
                    {isLoading ? <Loader /> : "Delete Course"}
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
