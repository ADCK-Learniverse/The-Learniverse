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

export const SwitchRole = () => {
  let token = localStorage.getItem('token');
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleRoleChange = (e) => {
    setRole(e.target.value);
  };

  const handleSwitch = async (e) => {
    e.preventDefault(); // Prevent form submission default behavior
    try {
      const approveSwitch = await fetch(`http://127.0.0.1:8000/owner_panel/account_role?person_email=${encodeURIComponent(email)}&role=${encodeURIComponent(role)}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },
      });

      if (!approveSwitch.ok) {
        throw new Error('Failed to switch');
      }

      console.log('Account role switched successfully');
      alert('Role Switched Successfully')
      window.location.href = "/control-panel";
    } catch (error) {
      console.error('Error executing request:', error);
    }
  };

  return (
    <Card>
       <h1>Change Role</h1>
      <ProfileImage src={'https://t4.ftcdn.net/jpg/01/97/15/87/360_F_197158744_1NBB1dEAHV2j9xETSUClYqZo7SEadToU.jpg'} alt="Profile" />
      <form id="switch-role-form" onSubmit={handleSwitch}>
        <Info>
          <Input
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={handleEmailChange}
          />
          <Select value={role} onChange={handleRoleChange}>
            <option value="">Select role</option>
            <option value="admin">Admin</option>
            <option value="teacher">Teacher</option>
            <option value="student">Student</option>
          </Select>
        </Info>
        <ButtonContainer>
          <Button type="submit">Switch Role</Button>
        </ButtonContainer>
      </form>
    </Card>
  );
};

export default SwitchRole;