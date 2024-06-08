import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

export default function CreateCourse() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [objectives, setObjectives] = useState("");
  const [status, setStatus] = useState("");
  const [tags, setTags] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleObjectivesChange = (e) => {
    setObjectives(e.target.value);
  };

  const handleStatusChange = (e) => {
    setStatus(e.target.value);
  };

  const handleTagsChange = (e) => {
    setTags(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title || !description || !objectives || !status || !tags) {
      alert("All fields are required.");
      return;
    }

    setIsLoading(true);
    let token = localStorage.getItem('token');
    token = token.replace(/^"|"$/g, '');
    console.log(token);

    try {
      const formData = {
        title,
        description,
        objectives,
        status,
        tags: tags.split(',').map(tag => tag.trim())
      };

      const payload = {
        token,
        courseData: formData
      };

      const response = await fetch('http://127.0.0.1:8000/courses/new', {
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

      // Course created successfully
      alert("Course created successfully");
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
                <h2 className="fw-bold mb-2 text-uppercase">Create Course</h2>
                <form id="create-course-form" onSubmit={handleSubmit}>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Title"
                      value={title}
                      onChange={handleTitleChange}
                      id="course-title"
                      aria-label="Course Title"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Description"
                      value={description}
                      onChange={handleDescriptionChange}
                      id="course-description"
                      aria-label="Course Description"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Objectives"
                      value={objectives}
                      onChange={handleObjectivesChange}
                      id="course-objectives"
                      aria-label="Course Objectives"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="text"
                      className="form-control-lg"
                      placeholder="Tags separated by ,"
                      value={tags}
                      onChange={handleTagsChange}
                      id="course-tags"
                      aria-label="Course Tags"
                    />
                  </div>
                  <div className="form-outline mb-4">
                      <select
                        className="form-control-lg"
                        id="course-status"
                        aria-label="Course Status"
                        onChange={handleStatusChange}
                      >
                        <option value="">Select Type</option>
                        <option value="premium">premium</option>
                        <option value="public">public</option>
                      </select>
                  </div>
                  <button type="submit" className="btn btn-outline-white btn-lg px-5">
                    {isLoading ? <Loader /> : "Create Course"}
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
