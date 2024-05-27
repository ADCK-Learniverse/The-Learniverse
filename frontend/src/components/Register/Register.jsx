// import { Link, useNavigate } from 'react-router-dom';
// import { useState } from 'react';
// import { useAuth } from '../hooks/registrationHook';
// import Loader from '../Loader/Loader'; // Ensure Loader component exists
// // import './Register_style.css'; // Make sure the CSS file path is correct if needed
//
// export default function Register() {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [firstname, setFirstname] = useState('');
//   const [lastname, setLastname] = useState('');
//   const [phonenumber, setPhonenumber] = useState('');
//   const { isLoading, error, register } = useAuth();
//   const navigate = useNavigate();
//
//   const handleSubmit = (e) => {
//     e.preventDefault();
//
//     if (!email || !password || !firstname || !lastname || !phonenumber) {
//       alert('All fields are required.');
//       return;
//     }
//
//     const formData = new FormData();
//     formData.append('email', email);
//     formData.append('password', password);
//     formData.append('firstname', firstname);
//     formData.append('lastname', lastname);
//     formData.append('phonenumber', phonenumber);
//
//     register(formData)
//       .then(() => {
//         alert('Successful registration');
//         navigate('/');
//       })
//       .catch((error) => {
//         alert('Registration failed: ' + error.message);
//       });
//   };
//
// //   return (
// //     <div className="registration-container">
// //       <section className="login-wrapper vh-100">
// //         <div className="container py-5 h-100">
// //           <div className="row d-flex justify-content-center align-items-center h-100">
// //             <div className="col-12 col-md-8 col-lg-6 col-xl-5">
// //               <div className="card bg-dark text-white" style={{ borderRadius: '1rem' }}>
// //                 <div className="card-body text-center">
// //                   <h2 className="fw-bold mb-2 text-uppercase">Login</h2>
// //                   <p className="text-white-50 mb-5">Please enter your email and password!</p>
// //                   <form onSubmit={handleSubmit}>
// //                     <div className="form-outline form-white mb-4">
// //                       <input
// //                         type="email"
// //                         id="typeEmailX"
// //                         className="form-control form-control-lg"
// //                         onChange={(e) => setEmail(e.target.value)}
// //                       />
// //                       <label className="form-label" htmlFor="typeEmailX">Email</label>
// //                     </div>
// //                     <div className="form-outline form-white mb-4">
// //                       <input
// //                         type="password"
// //                         id="typePasswordX"
// //                         className="form-control form-control-lg"
// //                         onChange={(e) => setPassword(e.target.value)}
// //                       />
// //                       <label className="form-label" htmlFor="typePasswordX">Password</label>
// //                     </div>
// //                     <p className="small mb-5 pb-lg-2">
// //                       <a className="text-white-50" href="#!">Forgot password?</a>
// //                     </p>
// //                     <button className="btn btn-outline-light btn-lg px-5" type="submit">Login</button>
// //                   </form>
// //                   <div className="d-flex justify-content-center text-center mt-4 pt-1">
// //                     <a href="#!" className="text-white"><i className="fab fa-facebook-f fa-lg"></i></a>
// //                     <a href="#!" className="text-white"><i className="fab fa-twitter fa-lg mx-4 px-2"></i></a>
// //                     <a href="#!" className
