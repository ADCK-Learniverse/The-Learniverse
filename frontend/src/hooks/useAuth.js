import { useCallback, useContext, useEffect, useMemo, useState } from "react";
import AppContext from "../context/AppContext";

const server = "http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com";
const loginEndpoint = "login";
const loginUrl = `${server}/${loginEndpoint}/token`;

export const useAuth = (username, password) => {
  const [appState, setAppState] = useState({ userData: null });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetching = useCallback(async (formData) => {
    try {
      setIsLoading(true);
      const data = await fetch("http://the-learniverse-backend1.eu-north-1.elasticbeanstalk.com/login/token", {
        method: "POST",
        body: formData,
      });
      const json = await data.json();
      setAppState(json);


   if (json.detail === 'Your account has no access at this time!') {
        alert(json.detail);
        window.location.href = "/login";
      } else if (json.access_token === undefined) {
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
