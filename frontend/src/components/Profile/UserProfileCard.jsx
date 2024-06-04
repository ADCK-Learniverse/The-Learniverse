import React, { useEffect, useState } from 'react';


export default function UserProfileCard({ user }) {

  return (
    <div style={{ marginBottom: '20px', padding: '20px', backgroundColor: '#fff', borderRadius: '5px', textAlign: 'center' }}>
      <img
        src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
        alt="avatar"
        style={{ width: '150px', borderRadius: '50%' }}
      />
      <p>{user.position}</p>
      <p>{user.location}</p>
    </div>
  );
}
