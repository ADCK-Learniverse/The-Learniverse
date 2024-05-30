import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import SectionsNavbar from "../Navbar/SectionsNavbar";
import styled from "styled-components";

const token = JSON.parse(localStorage.getItem("token"));

export default function CourseSections() {
  const url = useParams();
  const courseID = url.courseID;
  const sectionID = url.sectionID;
  console.log(url);
  const [sections, setSections] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/sections/${courseID}`, {
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
        console.log(data[0].Sections);
        setSections(data[0].Sections);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <>
      <h1
        style={{
          color: "black",
        }}
      >
        Course Sections
      </h1>
      {course.map((sections) => (
        <ul key={topic["Section ID"]}>
          <li>
            User with ID: 'hello'
          </li>
        </ul>
      ))}
    </>
  );
}
