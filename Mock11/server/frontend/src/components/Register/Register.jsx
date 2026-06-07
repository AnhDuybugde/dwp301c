import React, { useState } from "react";

function Register() {
  const [formData, setFormData] = useState({
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: ""
  });

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Registering user", formData);
  };

  return (
    <main className="register-page">
      <h1>Sign-up</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input id="username" name="username" value={formData.username} onChange={handleChange} required />

        <label htmlFor="firstName">First Name</label>
        <input id="firstName" name="firstName" value={formData.firstName} onChange={handleChange} required />

        <label htmlFor="lastName">Last Name</label>
        <input id="lastName" name="lastName" value={formData.lastName} onChange={handleChange} required />

        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" value={formData.email} onChange={handleChange} required />

        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" value={formData.password} onChange={handleChange} required />

        <button type="submit">Register</button>
      </form>
    </main>
  );
}

export default Register;
