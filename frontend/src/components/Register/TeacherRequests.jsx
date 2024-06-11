import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import "./Register.style.css";
import { CardComponent } from './CardTeachers';



const TeacherRequests = () => {
  const [requests, setRequests] = useState([]);
  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchTeachers = async () => {
      try {
        const response = await fetch("http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/admin_panel/teacher/pending_requests", {
          headers: {
            Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
          },
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        setRequests(data);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchTeachers();
  }, []);
  const validRequests = Array.isArray(requests) ? requests : [];

  return (
    <>
      <Navbar location="courses" />
      <section className="register-wrapper vh-100">
        <h2 className="fw-bold mb-2 text-uppercase text-center" style={{ marginTop: "0px" }}>View Teacher Requests</h2>
        {validRequests.length > 0 ? (
          <div className="row">
            {validRequests.map((request, index) => (
              <CardComponent
                key={index}
                email={request['Email']}
                firstName={request['First Name']}
                lastName={request['Last Name']}
                phoneNumber={request['Phone Number']}
                userId={request['User ID']}
              />
            ))}
          </div>
        ) : (
          <p className="text-center">No student requests awaiting approval!</p>
        )}
      </section>
    </>
  );
};

export default TeacherRequests;