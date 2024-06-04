import React, { useEffect, useState } from "react";

export default function UserSocialLinks({ user }) {
  return (
    <div
      style={{ padding: "20px", backgroundColor: "#fff", borderRadius: "5px" }}
    >
      <ul style={{ listStyleType: "none", padding: "0" }}>
        <li
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #ddd",
          }}
        >
          <span>Website:</span>
          <span>{user.website}</span>
        </li>
        <li
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #ddd",
          }}
        >
          <span>GitHub:</span>
          <span>{user.github}</span>
        </li>
        <li
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #ddd",
          }}
        >
          <span>Twitter:</span>
          <span>{user.twitter}</span>
        </li>
        <li
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #ddd",
          }}
        >
          <span>Instagram:</span>
          <span>{user.instagram}</span>
        </li>
        <li
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #ddd",
          }}
        >
          <span>Facebook:</span>
          <span>{user.facebook}</span>
        </li>
      </ul>
    </div>
  );
}
