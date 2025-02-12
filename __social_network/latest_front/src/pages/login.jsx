import axios from "axios";
import { useState } from "react";
import React from 'react';

export function Login() {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        });
    
      // Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,  // Spread the existing formData state
      [name]: value,  // Update the specific field that changed
    });
  };

  // Handle form submission (login)
  const handleLogin = () => {
    axios.post('/api/login', {
        username: formData.username,  // Send the username
        password: formData.password,  // Send the password
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((auth) => {
        // Clear form data after successful login
        setFormData({
          username: '',
          password: '',
        });

        // Store the auth token and user ID
        localStorage.setItem('authToken', auth.token);
        localStorage.setItem('userId', auth.id);

        // Redirect to a protected route (optional)
        window.location.href = `/user_profile/${auth.id}`;
      })
      .catch((error) => {
        console.error('Error:', error);
        // Optionally, display an error message to the user
      });
  };

  return(
    <div className="container">
        <div className="row justify-content-center">
        <div className="col-md-6 col-lg-4">
            <div className="card mt-5 shadow-sm">
            <div className="card-body">
                <h3 className="text-center mb-4">Log In</h3>

                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input
                    className="form-control"
                    name = 'username'
                    placeholder="Enter your email"
                    required
                    value={formData.username}
                    onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                    type="password"
                    className="form-control"
                    id="password"
                    placeholder="Enter your password"
                    required
                    name = 'password'
                    value={formData.password}
                    onChange={handleChange}
                    />
                </div>
                <button type="submit" className="btn btn-primary btn-block" onClick={handleLogin}>Log In</button>
                <div className="text-center mt-3">
                <small>
                    Don't have an account? <a href="/register">Register here</a>
                </small>
                </div>
            </div>
            </div>
        </div>
        </div>
    </div>
  );
};
