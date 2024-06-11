import React, { useState } from 'react';
import styled from 'styled-components';

const RatingButton = styled.button`
  background-color: #1c1c3c;
  color: #fff;
  padding: 12px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.2rem;
  margin-top: 10px;

  &:hover {
    background-color: #3a3a80;
  }
`;

const RatingContainer = styled.div`
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 10px;
`;

const RatingTab = styled.button`
  background-color: ${props => (props.selected ? '#3a3a80' : '#f0f0f0')};
  color: ${props => (props.selected ? '#fff' : '#1c1c3c')};
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  font-size: 1.2rem;
  cursor: pointer;

  &:hover {
    background-color: #3a3a80;
    color: #fff;
  }
`;

const RatingComponent = ({ courseID, token }) => {
  const [showRatingOptions, setShowRatingOptions] = useState(false);
  const [selectedRating, setSelectedRating] = useState(null);
  const [ratingSubmitted, setRatingSubmitted] = useState(false);

  const handleRateCourse = async (rating) => {
    try {
      const response = await fetch(`http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/courses/rating/${courseID}`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rating }),
      });
      if (!response.ok) {
        throw new Error(`Failed to rate course: ${response.statusText}`);
      }
      setSelectedRating(rating);
      setRatingSubmitted(true);
    } catch (error) {
      console.error("Error submitting rating:", error);
    }
  };

  return (
    <div>
      <RatingButton onClick={() => setShowRatingOptions(!showRatingOptions)}>
        {showRatingOptions ? 'Hide Rating Options' : 'Rate This Course'}
      </RatingButton>
      {showRatingOptions && (
        <RatingContainer>
          {[...Array(10).keys()].map(number => (
            <RatingTab
              key={number + 1}
              selected={selectedRating === number + 1}
              onClick={() => handleRateCourse(number + 1)}
            >
              {number + 1}
            </RatingTab>
          ))}
        </RatingContainer>
      )}
      {ratingSubmitted && (
        <div style={{ marginTop: '10px', color: 'green' }}>
          Thank you for rating!
        </div>
      )}
    </div>
  );
};

export default RatingComponent;
