import { Link, useNavigate } from "react-router-dom";

export default function Category({ categoryTitle, categoryID }) {
  const navigate = useNavigate();

  return (
    <Link
      to={`/categories/${categoryID}`}
      onClick={() => {
        navigate(`/categories/${categoryID}`);
      }}
    >
      <li>{categoryTitle}</li>
    </Link>
  );
}