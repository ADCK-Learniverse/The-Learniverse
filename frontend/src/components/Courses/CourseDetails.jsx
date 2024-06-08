import React from 'react';

const CourseDetails = ({ course }) => {
  const { title, description, rating, status, owner, tags, sections, progress } = course;

  return (
    <div>
      <h1>{title}</h1>
      <p>{description}</p>
      <p>Rating: {rating}</p>
      <p>Status: {status}</p>
      <p>Owner: {owner}</p>
      <p>Tags: {tags}</p>
      <p>Progress: {progress}</p>

      <div>
        <h2>Sections</h2>
        {sections.map(section => (
          <div key={section['Section ID']}>
            <h3>{section.Title}</h3>
            <p>{section.Content}</p>
            <p>Description: {section.Description}</p>
            <p>Information: {section.Information}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CourseDetails;
