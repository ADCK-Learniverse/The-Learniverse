import React from 'react';
import { useParams } from 'react-router-dom';
import CourseDetails from "./CourseDetails";

const CoursePage = () => {
  const { courseId } = useParams();

  return (
    <div>
      <CourseDetails courseId={courseId} />
    </div>
  );
};

export default CoursePage;
