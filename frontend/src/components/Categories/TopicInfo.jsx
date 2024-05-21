import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const token = JSON.parse(localStorage.getItem("token"));

export default function TopicInfo() {
  const url = useParams();
  const categoryID = url.categoryID;
  const topicID = url.topicID;
  console.log(url);
  const [topics, setTopics] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/topics/${topicID}`, {
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
        console.log(data[0].Replies);
        setTopics(data[0].Replies);
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
        Topic Replies
      </h1>
      {topics.map((topic) => (
        <ul key={topic["Reply ID"]}>
          <li>
            User with ID: {topic["User ID"]} replied with:{" "}
            {`"${topic["Reply content"]}"`}. Date:{" "}
            {topic["Date posted"].toLocaleString()}. Likes: {topic["Likes"]}.
            Dislikes: {topic["Dislikes"]}.
          </li>
        </ul>
      ))}
    </>
  );
}
