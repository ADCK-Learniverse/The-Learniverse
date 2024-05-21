import { useContext, useEffect, useState } from "react";
import AppContext from "../../context/AppContext";
import Category from "./Category";

const token = JSON.parse(localStorage.getItem("token"));
const server = "http://127.0.0.1:8000";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`;

export default function Categories() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch(`${server}/categories`, {
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
        console.log(data.Categories);
        setCategories(data.Categories);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <>
      {categories.map((category) => (
        <ul key={category["Category ID"]}>
          {" "}
          {/* Using 'key' prop for unique identification */}
          <Category
            categoryTitle={category["Category Name"]}
            categoryID={category["Category ID"]}
          ></Category>
        </ul>
      ))}
    </>
  );
}
