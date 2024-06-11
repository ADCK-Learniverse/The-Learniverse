import styled from "styled-components";
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Loader from "../Loader/Loader";

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

const Input = styled.input`
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Select = styled.select`
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
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

export const DeactivateAccount = () => {
  let token = localStorage.getItem('token');
  const [email, setEmail] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };


  const handleDeactivation = async (e) => {
    e.preventDefault();
    try {
      const deactivate = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/owner_panel/restrict_access?person_email=${encodeURIComponent(email)}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },
      });

      if (!deactivate.ok) {
        throw new Error('Failed to deactivate');
      }

      alert('Account Deactivated Successfully')
      window.location.href = "/control-panel";
    } catch (error) {
      console.error('Error executing request:', error);
    }
  };

  return (
    <Card>
       <h1>Deactivate Account</h1>
      <ProfileImage src={'https://t4.ftcdn.net/jpg/01/97/15/87/360_F_197158744_1NBB1dEAHV2j9xETSUClYqZo7SEadToU.jpg'} alt="Profile" />
      <form id="Deactivate-account-form" onSubmit={handleDeactivation}>
        <Info>
          <Input
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={handleEmailChange}
          />
        </Info>
        <ButtonContainer>
          <Button type="submit">Deactivate Account</Button>
        </ButtonContainer>
      </form>
    </Card>
  );
};

export default DeactivateAccount;