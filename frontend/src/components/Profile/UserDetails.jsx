import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function UserDetails({ user }) {
  return (
    <div
      style={{
        marginBottom: "20px",
        padding: "20px",
        backgroundColor: "#fff",
        borderRadius: "5px",
      }}
    >
      <div
        style={{ marginBottom: "20px", display: "flex", alignItems: "center" }}
      >
        <strong>First Name:</strong>
        <a
          href="/profile/firstName"
          style={{ marginLeft: "10px", textDecoration: "none" }}
        >
          <button>{user.firstname}</button>
        </a>
      </div>
      <div
        style={{ marginBottom: "20px", display: "flex", alignItems: "center" }}
      >
        <strong>Last Name:</strong>
        <a
          href="/profile/lastName"
          style={{ marginLeft: "10px", textDecoration: "none" }}
        >
          <button>{user.lastname}</button>
        </a>
      </div>
      <div
        style={{ marginBottom: "20px", display: "flex", alignItems: "center" }}
      >
        <strong>Email:</strong>
        <a
          href="/profile/email"
          style={{ marginLeft: "10px", textDecoration: "none" }}
        >
          <button>{user.email}</button>
        </a>
      </div>
      <div
        style={{ marginBottom: "20px", display: "flex", alignItems: "center" }}
      >
        <strong>Phone:</strong>
        <a
          href="/profile/phone"
          style={{ marginLeft: "10px", textDecoration: "none" }}
        >
          <button>{user.phone}</button>
        </a>
      </div>
      <div style={{ marginBottom: "20px" }}>
        <strong>Role:</strong>
        <span style={{ marginLeft: "10px" }}>{user.role}</span>
      </div>
      <div style={{ marginBottom: "20px" }}>
        <strong>Account Status:</strong>
        <span style={{ marginLeft: "10px" }}>{user.status}</span>
      </div>
    </div>
  );
}
