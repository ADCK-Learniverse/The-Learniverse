import React, { useEffect, useState } from 'react';
import UserProfileCard from './UserProfileCard';
import UserSocialLinks from './UserSocialLinks';
import UserDetails from './UserDetails';
import CoursesStatus from './CoursesStatus';
import Navbar from "../Navbar/Navbar";

let token = localStorage.getItem('token');


export default function ProfilePage() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/teacher_panel/profile", {
          headers: {
            Authorization: `Bearer ${token.replace(/^"|"$/g, '')}`,
          },
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        const userInfo = data['User info'][0];
        setUser({
          firstname: userInfo['First name'],
          lastname: userInfo['Last name'],
          email: userInfo['Email'],
          phone: userInfo['Phone number'],
          role: userInfo['Role'],
          status: userInfo['Status'],
          location: userInfo.location,
          website: userInfo.website,
          github: userInfo.github,
          twitter: userInfo.twitter,
          instagram: userInfo.instagram,
          facebook: userInfo.facebook,
        });
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchProfile();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <section style={{ background: 'linear-gradient(135deg, #1c1c3c, #3a3a80)', color: '#fff00', padding: '142px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '35px' }}>
        <Navbar location={"profile"} />
        <div style={{ display: 'flex', marginBottom: '190px' }}>
          <div style={{ flex: '1', marginRight: '20px', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
            <UserProfileCard user={user} />
            <UserSocialLinks user={user} />
          </div>

          <div style={{ flex: '2' }}>
            <UserDetails user={user} />
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <CoursesStatus />
              <CoursesStatus />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}



