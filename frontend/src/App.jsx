import { RouterProvider } from "react-router-dom";
import { router } from "./routes";
import "./App.css";
import { useEffect, useState } from "react";
import AppContext from "./context/AppContext";

function App() {
  const [accessToken, setToken] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setToken(token);
    }
  }, []);

  return (
    <>
      <AppContext.Provider value={{ token: accessToken, setContext: setToken }}>
        <RouterProvider router={router}></RouterProvider>
      </AppContext.Provider>
    </>
  );
}

export default App;