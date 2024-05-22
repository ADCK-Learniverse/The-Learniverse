import { createContext } from "react";

const AppContext = createContext({
  token: null,
  setContext: () => {},
});

export default AppContext;
