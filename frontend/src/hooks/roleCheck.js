import { useCallback, useEffect, useState } from "react";

const server = "http://127.0.0.1:8000";
const loginEndpoint = "owner_panel/info";
const loginUrl = `${server}/${loginEndpoint}`;
let token = localStorage.getItem('token');

const useRoleCheck = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [role, setRole] = useState(null);

  const fetchRoleInfo = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await fetch(loginUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
        },
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      setRole(data.role); 
    } catch (error) {
      console.error(error.message);
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchRoleInfo();
  }, [fetchRoleInfo]);

  return { role, isLoading, error };
};

export default useRoleCheck;
