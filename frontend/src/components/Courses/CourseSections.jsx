import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import SectionsNavbar from "../Navbar/SectionsNavbar";

const token = JSON.parse(localStorage.getItem("token"));

export default function CourseSections() {
  const { courseID } = useParams(); // Destructure useParams for cleaner code

  const [sections, setSections] = useState([]);

  useEffect(() => {
    console.log(`Fetching sections for course ID: ${courseID}`); // Check courseID
    fetch(`http://127.0.0.1:8000/sections/?course_id=${courseID}`, {
      headers: {
        Authorization: `Bearer ${token}`, // Ensure the correct capitalization of 'Bearer'
      },
    })
      .then((response) => {
        console.log("checkpoint1"); // Ensure we reach this point
        if (!response.ok) {
          console.error(`Response not ok: ${response.statusText}`);
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        console.log("checkpoint2", data); // Check the data received
        if (data && data.length > 0) {
          setSections(data);
        } else {
          setSections([]); // Set to an empty array if no sections are found
        }
      })
      .catch((error) => console.error("Error:", error));
  }, [courseID]); // Add courseID as a dependency

  return (
    <>
    <SectionsNavbar />
      <h1 style={{ color: "black" }}>Course Sections</h1>
      {sections.length > 0 ? (
        sections.map((section, index) => (
          <ul key={index}>
            <Link to={`course/sections/${courseID}/${index}`}>
              <li>{section["Section Title"]}</li> {/* Use appropriate field names */}
            </Link>
          </ul>
        ))
      ) : (
        <p>No sections available.</p>
      )}
    </>
  );
}
