import { useCallback, useContext, useEffect, useMemo, useState } from "react";
import AppContext from "../context/AppContext";

const server = "http://127.0.0.1:8000";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`;

export const useAuth = (username, password) => {
  const [appState, setAppState] = useState({ userData: null });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetching = useCallback(async (formData) => {
    try {
      setIsLoading(true);
      const data = await fetch("http://127.0.0.1:8000/login/token", {
        method: "POST",
        body: formData,
      });
      const json = await data.json();
      setAppState(json);

      if (json.access_token === undefined) {
        setError("Login failed: token is undefined");
        alert("Wrong Username or Password");
        window.location.href = "/login";
      } else {
        setAppState({ userData: json });
        window.location.href = "/";
        localStorage.setItem(
        "token",
        JSON.stringify(json.access_token));
      }


    } catch (error) {
      console.log(error.message);
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (!username) {
      return;
    }
    if (!password) {
      return;
    }
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    fetching(formData);
  }, [fetching]);

  return { appState, isLoading, error, login: fetching };
};
