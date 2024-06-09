import React, { useEffect, useState } from 'react';
import defaultProfilePic from "../../assets/defaultProfile.png";
import { Link } from 'react-router-dom'; // Import Link from react-router-dom

export default function UserProfileCard({ user }) {
  return (
    <div style={{ display: 'flex', marginBottom: '30px' }}>
      <div style={{ flex: '1', padding: '20px', backgroundColor: '#fff', borderRadius: '5px', textAlign: 'center' }}>
        <Link to={`/profile/picture`}>
          <img
            src={user.picture || defaultProfilePic}
            alt='avatar'
            style={{ width: '150px', borderRadius: '50%' }}
          />
        </Link>
        <p>{user.position}</p>
        <p>{user.location}</p>
      </div>
    </div>
  );
}
