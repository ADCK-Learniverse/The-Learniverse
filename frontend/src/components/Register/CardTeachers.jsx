import styled from "styled-components";
import "./Register.style.css";
import defaultProfilePic from "../../assets/defaultProfile.png";

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
       const approveResponse = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/admin_panel/teacher/registration_request?teacher_id=${encodeURIComponent(userId)}`, {
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
      window.location.href = "/teacher/requests";
    } catch (error) {
      console.error('Error approving request:', error);
    }
  };

  const handleDecline = async () => {
    try {
      const declineResponse = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/admin_panel/teacher/registration_request?teacher_id=${encodeURIComponent(userId)}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },

      });

      if (!declineResponse.ok) {
        throw new Error('Failed to approve');
      }
      console.log('Request declined successfully');
      window.location.href = "/teacher/requests";
    } catch (error) {
      console.error('Error approving request:', error);
    }
  };


  return (
    <Card>
      <ProfileImage src={defaultProfilePic} alt="Profile" />
      <Info>
          <InfoText>
            <span style={{ fontWeight: 'bold' }}>Email:</span> {email}
          </InfoText>
          <InfoText>
            <span style={{ fontWeight: 'bold' }}>Name:</span> {firstName} {lastName}
          </InfoText>
          <InfoText>
            <span style={{ fontWeight: 'bold' }}>Phone :</span> {phoneNumber}
          </InfoText>
        </Info>
      <ButtonContainer>
        <Button onClick={handleApprove}>Approve</Button>
        <Button onClick={handleDecline}>Decline</Button>
      </ButtonContainer>
    </Card>
  );
};
