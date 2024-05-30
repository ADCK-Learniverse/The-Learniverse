import React from "react";


const Course = ({ name, description, rating, status, by }) => {
  return (
   <Link
      to={`/course/sections/${courseID}`}
      onClick={() => {
        navigate(`course/sections/${courseID}`);
      }}
    >
      <li>{courseTitle}</li>
    </Link>
  );
};

export default Course;
