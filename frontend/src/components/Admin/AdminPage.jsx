import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import AppContext from "../../context/AppContext";
import Navbar from "../Navbar/Navbar";
import "./Admin.css";

const AdminPage = () => {
  return (
    <div className="admin-wrapper">
      <Navbar location="admin" />
      <div className="control-panel">
        <div className="main-panel">Information related to the platform</div>
        <div className="side-panel">
          <div className="top-box">Buttons for stuff</div>
          <div className="bottom-box">Not sure yet</div>
        </div>

      </div>
    </div>
  );
};

export default AdminPage;