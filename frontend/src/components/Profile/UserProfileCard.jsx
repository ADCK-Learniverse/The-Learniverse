import React, { useEffect, useState } from 'react';
import defaultProfilePic from "../../assets/defaultProfile.png";

export default function UserProfileCard({ user }) {
  return (
    <div style={{ display: 'flex', marginBottom: '20px' }}>
      <div style={{ flex: '1', padding: '20px', backgroundColor: '#fff', borderRadius: '5px', textAlign: 'center' }}>
        <img
          src={user.picture|| defaultProfilePic}
          alt='avatar'
          style={{ width: '150px', borderRadius: '50%' }}
        />
        <p>{user.position}</p>
        <p>{user.location}</p>
      </div>
    </div>
  );
}
