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
  cursor: pointer;
`;

const SearchContainer = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 20px;
`;

const SearchInput = styled.input`
  padding: 10px;
  border: none;
  border-radius: 5px 0 0 5px;
  width: 300px;
`;

const SearchButton = styled.button`
  padding: 10px;
  border: none;
  border-radius: 0 5px 5px 0;
  background-color: #3a3a80;
  color: #fff;
  cursor: pointer;

  &:hover {
    background-color: #2a2a60;
  }
`;

const AllCourses = () => {
  const [courses, setCourses] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();

  const fetchCourses = async (search = "") => {
    try {
      console.log("Fetching courses with search query:", search); // Debug log
      const response = await fetch(`http://127.0.0.1:8000/courses/all?search=${search}`);
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      const data = await response.json();
      console.log("Received data:", data); // Debug log
      setCourses(data.Courses);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const handleSearch = () => {
    fetchCourses(searchQuery);
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <CoursesWrapper>
      <Navbar location="courses" />
      <h1 style={{ marginTop: "100px" }}>Courses</h1>
      <SearchContainer>
        <SearchInput
          type="text"
          placeholder="Search courses..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <SearchButton onClick={handleSearch}>Search</SearchButton>
      </SearchContainer>
      <CourseContainer>
        {courses && courses.length > 0 ? (
          courses.map((course) => (
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
          ))
        ) : (
          <p>No courses found</p>
        )}
      </CourseContainer>
    </CoursesWrapper>
  );
};

export default AllCourses;
