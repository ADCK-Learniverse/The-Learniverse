import React, { useEffect, useState } from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import Navbar from "../Navbar/Navbar";

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

const AllCourses = () => {
  const [courses, setCourses] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/courses/all", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        setCourses(data.Courses);
        console.log(data)
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchCourses();
  }, []);

  return (
    <CoursesWrapper>
      <Navbar location = {"courses"} />
      <h1 style={{ marginTop: "100px" }}>Courses</h1>
      <CourseContainer>
        {courses.map((course) => (
          <Card
            key={course['Course ID']}
            onClick={() => navigate(`/course/sections/${course['Course ID']}`)}
          >
            <h2>{course["Course Title"]}</h2>
            <p>{course.Description}</p>
            <p>Rating: {course.Rating}</p>
            <p>Status: {course.Status}</p>
            <p>By: {course.By}</p>
          </Card>
        ))}
      </CourseContainer>
    </CoursesWrapper>
  );
};

export default AllCourses;
