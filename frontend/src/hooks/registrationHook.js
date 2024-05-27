import { useCallback, useState } from "react";

const server = "http://127.0.0.1:8000";
const registerEndpoint = "register/student";
const registerUrl = `${server}/${registerEndpoint}`;

export const userRegistration = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const register = useCallback(async (formData) => {
    try {
      setIsLoading(true);
      const response = await fetch(registerUrl, {
        method: "POST",
        body: formData,
      });

      const responseData = await response.json();

      if (!response.ok) {
        throw new Error(responseData.message || "Registration failed");
      }

      setIsLoading(false);
      return responseData; // Return response data on successful registration
    } catch (error) {
      setIsLoading(false);
      setError(error.message || "Registration failed");
      return null; // Return null on registration failure
    }
  }, []);

  return { isLoading, error, register };
};
