import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <div className="d-flex flex-column justify-content-center align-items-center vw-100 vh-100">
      <h1 className="display-1">
        <strong>404</strong>
      </h1>
      <h2>Page Not Found</h2>
      <p>Sorry, the page you are looking for does not exist.</p>
      <Link to="/" className="btn btn-primary">
        Go Back Home
      </Link>
    </div>
  );
}
