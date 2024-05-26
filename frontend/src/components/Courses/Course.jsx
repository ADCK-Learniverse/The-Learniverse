import { Link, useNavigate } from "react-router-dom";

export default function Course({ courseTitle, courseID }) {
  const navigate = useNavigate();

  return (
    <Link
      to={`/courses/${courseID}`}
      onClick={() => {
        navigate(`/courses/${courseID}`);
      }}
    >
      <li>{courseTitle}</li>
    </Link>
  );
}