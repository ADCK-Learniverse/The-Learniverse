import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

export default function CreateSection() {
  const navigate = useNavigate();

  // State variables for form inputs and loading/error handling
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [description, setDescription] = useState("");
  const [information, setInformation] = useState("");
  const [courseID, setCourseID] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  // Event handlers for input changes
  const handleTitleChange = (e) => setTitle(e.target.value);
  const handleContentChange = (e) => setContent(e.target.value);
  const handleDescriptionChange = (e) => setDescription(e.target.value);
  const handleInformationChange = (e) => setInformation(e.target.value);
  const handleCourseChange = (e) => setCourseID(e.target.value);

  // Form submission handler
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Form validation
    if (!title || !content || !description || !information || !courseID) {
      alert("All fields are required.");
      return;
    }

    setIsLoading(true);
    let token = localStorage.getItem('token');
    token = token.replace(/^"|"$/g, '');


    try {
      const formData = {
        title,
        content,
        description,
        information,
        course_id: courseID // Fixed variable name
      };

      const response = await fetch('http://127.0.0.1:8000/sections/new', {
        method: "POST",
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

      // Section created successfully
      alert("Section created successfully");
      navigate('/'); // Redirect to home page or wherever appropriate
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
                <h2 className="fw-bold mb-2 text-uppercase">Create Section</h2>
                <form id="create-section-form" onSubmit={handleSubmit}>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Title"
                      value={title}
                      onChange={handleTitleChange}
                      aria-label="Section Title"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Content"
                      value={content}
                      onChange={handleContentChange}
                      aria-label="Section Content"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Description"
                      value={description}
                      onChange={handleDescriptionChange}
                      aria-label="Section Description"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Information"
                      value={information}
                      onChange={handleInformationChange}
                      aria-label="Section Information"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Course ID"
                      value={courseID}
                      onChange={handleCourseChange}
                      aria-label="Course ID"
                    />
                  </div>
                  <button type="submit" className="btn btn-outline-white btn-lg px-5">
                    {isLoading ? <Loader /> : "Create Section"}
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
