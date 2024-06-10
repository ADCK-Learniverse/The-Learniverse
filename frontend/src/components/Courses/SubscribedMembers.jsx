import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Navbar from "../Navbar/Navbar";
import Loader from "../Loader/Loader";

export default function SubscribedMembers() {
  const { courseID } = useParams();
  const navigate = useNavigate();
  const token = JSON.parse(localStorage.getItem("token"));

  const [subscribers, setSubscribers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log(`courseID: ${courseID}`); // Verify courseID

    if (!token) {
      navigate('/login');
      return;
    }

    const fetchSubscribers = async () => {
      try {
        if (!courseID) {
          throw new Error('Invalid courseID');
        }

        const response = await fetch(`http://127.0.0.1:8000/courses/subscribers/${courseID}`, {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Failed to fetch subscribers: ${response.statusText} - ${errorText}`);
        }

        const data = await response.json();
        console.log("Fetched subscribers data:", data); // Log fetched data
        setSubscribers(data.Subscribers);
      } catch (err) {
        console.error("Error fetching subscribers:", err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchSubscribers();
  }, [courseID, token, navigate]);

  if (loading) return <Loader />;
  if (error) return <div>Error: {error.message}</div>;
  if (!subscribers.length) return <div>No subscribers found.</div>;

  return (
    <section style={{ background: 'linear-gradient(135deg, #1c1c3c, #3a3a80)', color: '#fff', padding: '100px 0', height: '100vh' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '50px' }}>
        <Navbar location="course/subscribed-members" />

        <div style={{ marginBottom: '50px', textAlign: 'center' }}>
          <h1 style={{ color: '#fff', fontSize: '3rem' }}>Subscribed Members</h1>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', alignItems: 'center' }}>
          {subscribers.map((subscriber, index) => (
            <div key={index} style={{
              background: 'rgba(255, 255, 255, 0.1)',
              borderRadius: '8px',
              padding: '10px 20px',
              width: '300px',
              textAlign: 'center',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              backdropFilter: 'blur(10px)',
              color: '#fff',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}>
              <p style={{ fontSize: '1.5rem', fontWeight: 'bold', margin: 0 }}>{subscriber[0]}</p>
              <p style={{ fontSize: '1.5rem', margin: 0 }}>{subscriber[1]}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
