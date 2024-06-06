import React, { useEffect, useState } from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import "./Register.style.css";

const Card = styled.div`
  background-color: #2c3e50;
  color: white;
  border-radius: 1rem;
  padding: 20px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 300px;
  margin: auto;
`;

const ProfileImage = styled.img`
  border-radius: 50%;
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-bottom: 20px;
`;

const Info = styled.div`
  margin-bottom: 15px;
`;

const InfoText = styled.p`
  margin: 5px 0;
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: space-around;
`;

const Button = styled.button`
  background-color: #2980b9;
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #3498db;
  }
`;

const CardComponent = ({ profileImage, email, firstName, lastName, phoneNumber }) => {
  return (
    <Card>
      <ProfileImage src={'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp'} alt="Profile" />
      <Info>
        <InfoText>{email}</InfoText>
        <InfoText>{firstName}</InfoText>
        <InfoText>{lastName}</InfoText>
        <InfoText>{phoneNumber}</InfoText>
      </Info>
      <ButtonContainer>
        <Button>Accept</Button>
        <Button>Reject</Button>
      </ButtonContainer>
    </Card>
  );
};

const TeacherRequests = () => {
  const [requests, setRequests] = useState([]);
  const navigate = useNavigate();
  let token = localStorage.getItem('token');

  useEffect(() => {
    const fetchTeachers = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/teacher_panel/student/pending_requests", {
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
  }, [token]);

  return (
    <>
    <Navbar location = {"courses"} />
    <section className="register-wrapper vh-100">
                    <h2 className="fw-bold mb-2 text-uppercase center"style={{ marginTop: "0px" }}>View Teacher Requests</h2>
                    <div className="row">
                    {requests.map((request, index) => (
                      <CardComponent
                        key={index}
                        email={request['Email']} // Using bracket notation
                        firstName={request['First Name']} // Using bracket notation
                        lastName={request['Last Name']} // Using bracket notation
                        phoneNumber={request['Phone Number']} // Using bracket notation
                      />

                    ))}
                         </div>
         </section>
    </>
  );
};

export default TeacherRequests;
