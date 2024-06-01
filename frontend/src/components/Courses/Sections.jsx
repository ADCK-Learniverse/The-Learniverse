import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import styled from "styled-components";

const CoursesWrapper = styled.div`
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #1c1c3c, #3a3a80);
  background-size: cover;
  background-attachment: fixed;
  color: #fff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const CourseContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  width: 80%;
  margin-top: 20px;
`;

const Card = styled.div`
  background-color: #282848;
  color: #fff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  cursor: pointer; /* Add cursor pointer to indicate clickability */
`;

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
    <CoursesWrapper>
      <Navbar location={"course/sections/"} />
      <h1 style={{ marginTop: "100px" }}>Course Sections</h1>
      <CourseContainer>
        {course.map((sections) => (
          <Card key={sections["Section ID"]}>
            <ul>
              <li>User with ID: {sections["Section ID"]}</li>
            </ul>
          </Card>
        ))}
      </CourseContainer>
    </CoursesWrapper>
  );
}
