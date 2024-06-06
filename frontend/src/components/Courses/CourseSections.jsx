import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import Navbar from "../Navbar/Navbar";



export default function CourseSections() {
  const { courseID } = useParams();
  const token = JSON.parse(localStorage.getItem("token"));

  const [sections, setSections] = useState([]);

  useEffect(() => {
    console.log(`Fetching sections for course ID: ${courseID}`);
    fetch(`http://127.0.0.1:8000/sections/?course_id=${courseID}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => {
        if (!response.ok) {
          console.error(`Response not ok: ${response.statusText}`);
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        console.log("checkpoint2", data);
        if (data && data.length > 0) {
          setSections(data);
        } else {
          setSections([]);
        }
      })
      .catch((error) => console.error("Error:", error));
  }, [courseID]);

  return (
    <>
    <Navbar location = {"course/sections/"} />
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
