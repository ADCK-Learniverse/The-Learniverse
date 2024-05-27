import { createBrowserRouter } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import NotFoundPage from "./components/NotFoundPage/NotFoundPage";
import Login from "./components/Login/Login";
import Categories from "./components/Categories/Categories";
import Category from "./components/Categories/Category";
import CategoryInfo from "./components/Categories/CategoryInfo";
import TopicInfo from "./components/Categories/TopicInfo";
import RegistrationStudents from "./components/Register/RegistrationStudents";
import RegistrationTeachers from "./components/Register/RegistrationTeachers";
import Courses from "./components/Courses/Courses";
import Course from "./components/Courses/Course";


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
    path: "course",
    element: <Course />,
  },
  {
    path: "categories/:categoryID",
    element: <CategoryInfo />,
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
    path: "categories/:categoryID/:topicID",
    element: <TopicInfo />,
  },
  {
    path: "*", // Wildcard route should come last
    element: <NotFoundPage />,
  },
]);
