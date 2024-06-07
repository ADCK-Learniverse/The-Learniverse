import styled from "styled-components";
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

export const CardComponent  =  ({ profileImage, email, firstName, lastName, phoneNumber, userId }) => {
  let token = localStorage.getItem('token');

    const handleApprove = async () => {
    try {
      const approveResponse = await fetch(`http://127.0.0.1:8000/teacher_panel/student/registration_request?student_id=${encodeURIComponent(userId)}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },

      });

      if (!approveResponse.ok) {
        throw new Error('Failed to approve');
      }

      // Handle success response
      console.log('Request approved successfully');
      window.location.href = "/student/requests";
    } catch (error) {
      console.error('Error approving request:', error);
    }
  };

  const handleDecline = async () => {
    try {
      const declineRequest = await fetch(`http://127.0.0.1:8000/teacher_panel/student/registration_request?student_id=${encodeURIComponent(userId)}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },

      });

      if (!declineRequest.ok) {
        throw new Error('Failed to approve');
      }

      console.log('Request declined successfully');
      window.location.href = "/student/requests";
    } catch (error) {
      console.error('Error approving request:', error);
    }
  };


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
        <Button onClick={handleApprove}>Approve</Button>
        <Button onClick={handleDecline}>Decline</Button>
      </ButtonContainer>
    </Card>
  );
};
