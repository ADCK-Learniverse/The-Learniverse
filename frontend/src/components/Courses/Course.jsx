import React from "react";


const Course = ({ name, description, rating, status, by }) => {
  return (
    <div className="course">
      <h2>{name}</h2>
      <p>{description}</p>
      <p>Rating: {rating}</p>
      <p>Status: {status}</p>
      <p>By: {by}</p>
    </div>
  );
};

export default Course;
