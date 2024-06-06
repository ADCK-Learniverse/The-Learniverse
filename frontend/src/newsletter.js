export default function sendNewsletter(emailAddress) {

  if (!emailAddress || typeof emailAddress !== 'string' || !emailAddress.includes('@')) {
    console.error('Invalid email address:', emailAddress);
    alert('Please enter a valid email address.');
    return;
  }


  const url = `http://127.0.0.1:8000/owner_panel/newsletter?email=${encodeURIComponent(emailAddress)}`;


  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Response data:', data);
      if (data === 'Already subscribed') {
        alert('You are already subscribed to the newsletter.');
      } else {
        alert('Subscription successful!');
      }
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      alert('There was an error with your subscription. Please try again.');
    });
}
