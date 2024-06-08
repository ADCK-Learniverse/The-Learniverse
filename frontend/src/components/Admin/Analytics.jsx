import styled, { keyframes } from "styled-components";
import React, { useState, useEffect } from 'react';

const rotate = keyframes`
  0% {
    stroke-dasharray: 0, 100;
  }
`;

const CircleWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
`;

const Svg = styled.svg`
  transform: rotate(-90deg);
`;

const CircleBackground = styled.circle`
  fill: none;
  stroke: #eee;
  stroke-width: 10;
`;

const CircleProgress = styled.circle`
  fill: none;
  stroke: #3498db;
  stroke-width: 10;
  stroke-linecap: round;
  animation: ${rotate} 2s ease-out forwards;
`;

const PercentageText = styled.text`
  font-size: 20px;
  fill: #3498db;
  text-anchor: middle;
  dominant-baseline: middle;
`;

const calculatePercentage = (registeredUsers, existingCourses, newsletterSubscribed) => {
  // Customize this formula based on your requirements
  const total = registeredUsers + existingCourses + newsletterSubscribed;
  const percentage = (total / 300) * 100; // Assuming 300 is the max value for 100%
  return Math.min(percentage, 100); // Ensure percentage doesn't exceed 100
};

const CircularProgressBar = ({ registeredUsers, existingCourses, newsletterSubscribed }) => {
  const percentage = calculatePercentage(registeredUsers, existingCourses, newsletterSubscribed);
  const radius = 50;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (percentage / 100) * circumference;

  return (

    <CircleWrapper>
      <Svg width="120" height="120">
        <CircleBackground cx="60" cy="60" r={radius} />
        <CircleProgress
          cx="60"
          cy="60"
          r={radius}
          strokeDasharray={`${circumference} ${circumference}`}
          strokeDashoffset={offset}
        />
        <PercentageText x="60" y="60">{`${Math.round(25)}%`}</PercentageText>
      </Svg>
    </CircleWrapper>
  );
};

export default CircularProgressBar;
