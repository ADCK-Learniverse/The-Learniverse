import React, { useEffect, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import Navbar from "../Navbar/Navbar";
import defaultCoursePic from "../../assets/default.jpg";
import Loader from "../Loader/Loader"; // Adjust the import path

export default function CourseSections() {
  const { courseID } = useParams();
  const navigate = useNavigate();
  const token = JSON.parse(localStorage.getItem("token"));

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showSections, setShowSections] = useState(false);
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [showRatingOptions, setShowRatingOptions] = useState(false);
  const [userRating, setUserRating] = useState(null);

  useEffect(() => {
    if (!token) {
      navigate('/login');
      return;
    }

    const fetchCourseData = async () => {
      try {
        const courseResponse = await fetch(`http://127.0.0.1:8000/courses/${courseID}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!courseResponse.ok) {
          throw new Error(`Failed to fetch course data: ${courseResponse.statusText}`);
        }
        const courseData = await courseResponse.json();
        console.log('Fetched Course Data:', courseData);
        setCourse(courseData[0]);

        const subscriptionResponse = await fetch(`http://127.0.0.1:8000/courses/subscription/${courseID}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (subscriptionResponse.ok) {
          const subscriptionData = await subscriptionResponse.json();
          setIsSubscribed(subscriptionData.subscribed);
        }

        const ratingResponse = await fetch(`http://127.0.0.1:8000/courses/rating/${courseID}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (ratingResponse.ok) {
          const ratingData = await ratingResponse.json();
          setUserRating(ratingData.rating !== null ? ratingData.rating : 'No rating');
        }
      } catch (err) {
        console.error("Error fetching data:", err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchCourseData();
  }, [courseID, token, navigate]);

  useEffect(() => {
    // Check if the user is subscribed and has rated the course
    if (isSubscribed && userRating) {
      // Hide the rating and subscription options if the user is subscribed and has rated the course
      setShowRatingOptions(false);
    }
  }, [isSubscribed, userRating]);

  const handleSubscribe = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/courses/subscription/${courseID}`, {
        method: isSubscribed ? 'DELETE' : 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error(`Failed to ${isSubscribed ? 'unsubscribe' : 'subscribe'}: ${response.statusText}`);
      }
      setIsSubscribed(!isSubscribed);
    } catch (error) {
      console.error("Error subscribing/unsubscribing:", error);
    }
  };

const handleRating = async (rating) => {
  try {
    // Parse the rating value as an integer
    const ratingValue = parseInt(rating);

    // Check if the parsed rating is within the acceptable range
    if (isNaN(ratingValue) || ratingValue < 1 || ratingValue > 10) {
      throw new Error("Rating must be an integer between 1 and 10");
    }

    const response = await fetch(`http://127.0.0.1:8000/courses/rating/${courseID}?rating=${ratingValue}`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to rate course: ${response.statusText}`);
    }

    // Update the user's rating locally
    setUserRating(ratingValue);
    // Hide the rating options after the user has rated the course
    setShowRatingOptions(false);
  } catch (error) {
    console.error("Error rating course:", error);
  }
};



  const getProgressColor = (progress) => {
    if (0 <= progress <= 35) return 'red';
    if (35 <= progress <= 75) return 'orange';
    return 'green';
  };

  if (loading) return <Loader />;
  if (error) return <div>Error: {error.message}</div>;
  if (!course) return <div>No course data available.</div>;

  return (
    <section style={{ background: 'linear-gradient(135deg, #1c1c3c, #3a3a80)', color: '#fff', padding: '100px 0' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '35px' }}>
        <Navbar location="course/sections/" />
        <div style={{ marginBottom: '50px', textAlign: 'center' }}>
          <h1 style={{ color: '#fff', fontSize: '3rem' }}>{course["Course Title"]}</h1>
          <h2 style={{ color: '#ccc', marginTop: '10px' }}>{course.Description}</h2>
        </div>

        <div style={{ display: 'flex', gap: '20px' }}>
          <div style={{ flex: '2', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding: '20px' }}>
            <img
              className="img-fluid"
              src={course.picture || defaultCoursePic}
              alt={course["Course Title"]}
              style={{ borderRadius: '8px', width: '100%', objectFit: 'cover', height: 'auto' }}
            />
          </div>
          <div style={{ flex: '3', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding: '20px', position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <p className="mb-0" style={{ fontSize: '2rem', color: '#1c1c3c' }}>Owner: {course.By}</p>
              <p className="mb-0" style={{ fontSize: '2rem', marginTop: '10px', color: course.Status === 'premium' ? '#ffcc00' : (course.Status === 'public' ? 'green' : 'inherit'), fontWeight: course.Status === 'premium' ? 'bold' : 'normal' }}>
                Status: {course.Status}
              </p>
              <p className="text-black-50 mb-0" style={{ fontSize: '1.5rem', marginTop: '10px' }}>Tags: {course.Tags}</p>
            </div>
            <div style={{ marginTop: '50px' }}>
              <h4 style={{ fontSize: '1.5rem', color: '#1c1c3c' }}>Rating: {course.Rating}</h4>
              {course.Progress && (
                <p style={{ fontSize: '1.2rem', color: getProgressColor(course.Progress), marginTop: '10px' }}>
                  Progress: {course.Progress}
                </p>
              )}
            </div>
            <div>
              {showRatingOptions ? (
                <div>
                  {[...Array(10)].map((_, i) => (
                    <button
                      key={i + 1}
                      onClick={() => handleRating(i + 1)}
                      style={{
                        backgroundColor: userRating === i + 1 ? '#ffd700' : '#fff',
                        color: '#000',
                        padding: '10px',
                        margin: '5px',
                        border: '1px solid #ccc',
                        borderRadius: '5px',
                        cursor: 'pointer',
                        pointerEvents: userRating ? 'none' : 'auto', // Disable button after rating
                      }}>
                      {i + 1}
                    </button>
                  ))}
                </div>
              ) : (
                <button
                  onClick={() => setShowRatingOptions(true)}
                  style={{
                    backgroundColor: '#ffd700',
                    color: '#000',
                    padding: '12px 20px',
                    border: 'none',
                    borderRadius: '8px',
                    cursor: 'pointer',
                    fontSize: '1.2rem',
                    pointerEvents: userRating ? 'none' : 'auto', // Disable button after rating
                  }}>
                  {userRating ? `Rated: ${userRating}` : 'Rate this Course'}
                </button>
              )}
            </div>
            <button
              onClick={handleSubscribe}
              style={{
                backgroundColor: isSubscribed ? '#ffcccb' : '#ff0000',
                color: '#fff',
                padding: '12px 10px',
                border: 'none',
                borderRadius: '8px',
                cursor: 'pointer',
                fontSize: '1.2rem',
                marginTop: '10px',
              }}>
              {isSubscribed ? 'UNSUBSCRIBE' : 'SUBSCRIBE'}
            </button>
          </div>
        </div>

        {!isSubscribed && course.Status === 'premium' ? null : (
          <button
            onClick={() => setShowSections(!showSections)}
            style={{
              marginTop: '20px',
              width: '100%',
              backgroundColor: '#1c1c3c',
              color: '#fff',
              padding: '10px 20px',
              border: 'none',
              borderRadius: '8px',
              cursor: 'pointer'
            }}>
            {showSections ? 'Hide Sections' : 'Show Sections'}
          </button>
        )}

        {showSections && (
          <div style={{ marginTop: '20px' }}>
            {course.Sections && course.Sections.length > 0 ? (
              course.Sections.map((section, index) => (
                <div key={index} style={{
                  background: 'linear-gradient(135deg, #fff, #f0f0f0)',
                  borderRadius: '8px',
                  padding: '10px 20px',
                  marginBottom: '10px',
                  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
                  textAlign: 'left'
                }}>
                  <Link to={`/course/sections/${courseID}/${section["Section ID"]}`} style={{ textDecoration: 'none', color: '#1c1c3c' }}>
                    {section.Title}
                  </Link>
                </div>
              ))
            ) : (
              <p>No sections available.</p>
            )}
          </div>
        )}
      </div>
    </section>
  );
}
