import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../Navbar/Navbar";

let token = localStorage.getItem('token');

const SubscribedMembers = () => {
  const [members, setMembers] = useState([]);
  const [courseMembers, setCourseMembers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMembers = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/teacher_panel/7/subscribers", {
          headers: {
            Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
          },
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        setMembers(data.Members);
        setCourseMembers(data['Course Subscribers']);
        console.log(data)
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchMembers();
  }, []);

  return (
    <>
      <h1
        style={{
          color: "black",
        }}
      >
        Course Members
      </h1>
      <pre>{JSON.stringify(courseMembers, null, 2)}</pre>
    </>
  );
};

export default SubscribedMembers;