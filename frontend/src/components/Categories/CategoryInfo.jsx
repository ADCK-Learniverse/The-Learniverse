import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

const token = JSON.parse(localStorage.getItem("token"));

export default function CategoryInfo() {
  const url = useParams();
  const categoryID = url.categoryID;

  const [topics, setTopics] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/categories/${categoryID}`, {
      headers: {
        Authorization: `bearer ${token}`,
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data[0].Topics);
        setTopics(data[0].Topics);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <>
      <h1
        style={{
          color: "black",
        }}
      >
        Category Topics
      </h1>
      {topics.map((topic) => (
        <ul key={topic["Topic ID"]}>
          <Link to={`/categories/${categoryID}/${topic["Topic ID"]}`}>
            <li>{topic["Topic name"]}</li>
          </Link>
        </ul>
      ))}
    </>
  );
}
