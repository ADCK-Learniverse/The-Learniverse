import React from "react";
import { Link } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import SwitchAccountRole from "./SwitchAccountRole";
import DeactivateAccount from "./DeactivateAccount";
import "./Admin.css";
import CircularProgressBar from './Analytics';


const AdminPage = () => {
    const registeredUsers = 100;
  const existingCourses = 50;
  const newsletterSubscribed = 30;
  return (
    <div className="admin-wrapper">
      <Navbar location="admin" />
      <div className="control-panel">
        <div className="main-panel">
            <DeactivateAccount />
        </div>
        <div className="side-panel">
          <div className="top-box">
            <SwitchAccountRole />
          </div>
          <div className="bottom-box"></div>
        </div>
      </div>
    </div>
  );
};

export default AdminPage;
