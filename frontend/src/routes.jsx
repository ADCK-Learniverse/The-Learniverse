import { createBrowserRouter } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import NotFoundPage from "./components/NotFoundPage/NotFoundPage";
import Login from "./components/Login/Login";
import RegistrationStudents from "./components/Register/RegistrationStudents";
import RegistrationTeachers from "./components/Register/RegistrationTeachers";
import Courses from "./components/Courses/Courses";
import Course from "./components/Courses/Course";
import CourseSections from "./components/Courses/CourseSections";
import CreateCourse from "./components/Courses/CreateCourse";
import CreateSection from "./components/Courses/CreateSection";
import Profile from "./components/Profile/Profile";
import SubscribedMembers from "./components/Courses/SubscribedMembers";


export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "login",
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
    path: "courses/create-course",
    element: <CreateCourse />,
  },
      {
    path: "/sections/create-section",
    element: <CreateSection />,
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
    path: "/profile",
    element: <Profile />,
  },
     {
    path: "course/subscribedMembers",
    element: <SubscribedMembers />,
  },
  {
    path: "*",
    element: <NotFoundPage />,
  },
]);
