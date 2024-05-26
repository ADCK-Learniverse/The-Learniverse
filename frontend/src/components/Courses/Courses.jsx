import { useContext, useEffect, useState } from "react";
import AppContext from "../../context/AppContext";
const token = JSON.parse(localStorage.getItem("token"));
const server = "http://127.0.0.1:8000";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`

// Individual Course Component
const Course = ({ name, description }) => {
  return (
    <div>
      <h2>{name}</h2>
      <p>{description}</p>
    </div>
  );
};

// Component to Render All Courses
const AllCourses = () => {
  // State to store the list of courses
  const [courses, setCourses] = useState([]);

  // Simulated data fetch (replace with actual API call)
  useEffect(() => {
    fetch(`${server}/courses`, {
      headers: {
        Authorization: `bearer ${token}`,
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data.Courses);
//         setCategories(data.Courses);
      })
      .catch((error) => console.error("Error:", error));
  }, []);ount

  return (
    <div>
      <h1>All Courses</h1>
      {courses.map(course => (
        <Course key={course.id} name={course.name} description={course.description} />
      ))}
    </div>
  );
};

export default AllCourses;
