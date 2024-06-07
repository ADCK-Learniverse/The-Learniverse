import { createBrowserRouter } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import NotFoundPage from "./components/NotFoundPage/NotFoundPage";
import Login from "./components/Login/Login";
import RegistrationStudents from "./components/Register/RegistrationStudents";
import RegistrationTeachers from "./components/Register/RegistrationTeachers";
import TeacherRequests from "./components/Register/TeacherRequests";
import StudentRequests from "./components/Register/StudentRequests";
import Courses from "./components/Courses/Courses";
import Course from "./components/Courses/Course";
import CourseSections from "./components/Courses/CourseSections";
import CreateCourse from "./components/Courses/CreateCourse";
import CreateSection from "./components/Courses/CreateSection";
import DeleteSection from "./components/Courses/DeleteSection";
import DeleteCourse from "./components/Courses/DeleteCourse";
import Profile from "./components/Profile/Profile";
import UpdateFirstName from "./components/Profile/UpdateFirstName";
import UpdateLastName from "./components/Profile/UpdateLastName";
import UpdatePassword from "./components/Profile/UpdatePassword";
import UpdateEmail from "./components/Profile/UpdateEmail";
import UpdatePhone from "./components/Profile/UpdatePhone";
import SubscribedMembers from "./components/Courses/SubscribedMembers";
import AdminPage from "./components/Admin/AdminPage";



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
    path: "/sections/delete-section",
    element: <DeleteSection />,
  },
       {
    path: "/courses/delete-course",
    element: <DeleteCourse />,
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
    path: "teacher/requests",
    element: <TeacherRequests />,
  },
  {
    path: "student/requests",
    element: <StudentRequests />,
  },
    {
    path: "/profile",
    element: <Profile />,
  },
    {
    path: "/profile/firstName",
    element: <UpdateFirstName />,
  },
    {
    path: "/profile/lastName",
    element: <UpdateLastName />,
  },
    {
    path: "/profile/password",
    element: <UpdatePassword />,
  },
    {
    path: "/profile/email",
    element: <UpdateEmail />,
  },
      {
    path: "/profile/phone",
    element: <UpdatePhone />,
  },
     {
    path: "course/subscribedMembers",
    element: <SubscribedMembers />,
  },
      {
    path: "/control-panel",
    element: <AdminPage />,
  },
  {
    path: "*",
    element: <NotFoundPage />,
  },
]);
