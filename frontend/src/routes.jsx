import { createBrowserRouter } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import NotFoundPage from "./components/NotFoundPage/NotFoundPage";
import Login from "./components/Login/Login";
import RegistrationStudents from "./components/Register/RegistrationStudents";
import RegistrationTeachers from "./components/Register/RegistrationTeachers";
import Courses from "./components/Courses/Courses";
import Course from "./components/Courses/Course";
import CourseSections from "./components/Courses/CourseSections";


export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "login", // Corrected path definition
    element: <Login />,
  },
  {
    path: "courses",
    element: <Courses />,
  },
   {
    path: "course/sections/:courseID",
    element: <CourseSections />,
  },
  {
    path: "register/students",
    element: <RegistrationStudents />,
  },
  {
    path: "register/teachers",
    element: <RegistrationTeachers />,
  },
  {
    path: "*", // Wildcard route should come last
    element: <NotFoundPage />,
  },
]);
