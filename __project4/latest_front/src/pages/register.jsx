import axios from 'axios';
import { useState } from 'react';
import React from 'react';

import {useParams} from 'react-router-dom';

export function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [PassErr, setPassErr] = useState({
    diff: false,
    tooShort: false,
    noSpecialChars: false
  })

  const handleChange = (event) => {
    const { id, value } = event.target;
    setFormData({
      ...formData,
      [id]: value,
    });
  };

  const handleSubmit = (event) => {
    setPassErr(prevState => ({
      ...prevState,
      tooShort: password.length <= 8,
      diff: password !== confirmPassword,
    }));

    if(PassErr.diff || PassErr.tooShort || PassErr.noSpecialChars){
      console.log('bija')
      return
    }

    axios.post('/api/register', {
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((auth) => {
        setFormData({
          username: '',
          email: '',
          password: '',
          confirmPassword: '',
        });
        localStorage.setItem('authToken', auth.token);
        localStorage.setItem('userId', auth.id);
        window.location.href = `/user_profile/${auth.id}`;
      })
      .catch((error) => {
        console.error('Error:', error);
      });

  };


  return(
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-md-6 col-lg-4">
          <div className="card mt-5 shadow-sm">
            <div className="card-body">
              <h3 className="text-center mb-4">Register</h3>
                <div className="form-group">
                  <label htmlFor="username">Username</label>
                  <input onChange={handleChange}
                    type="text"
                    className="form-control"
                    id="username"
                    placeholder="Enter your username"
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="email">Email address</label>
                  <input onChange={handleChange}
                    type="email"
                    className="form-control"
                    id="email"
                    placeholder="Enter your email"
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="password">Password</label>
                  <input onChange={handleChange}
                    type="password"
                    className="form-control"
                    id="password"
                    placeholder="Enter your password"
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="confirmPassword">Confirm Password</label>
                  <input onChange={handleChange}
                    type="password"
                    className="form-control"
                    id="confirmPassword"
                    placeholder="Confirm your password"
                    required
                  />
                </div>
                {PassErr.tooShort && (
                  <div className="alert alert-warning" role="alert">
                    Password is too short. It must be longer than 6 characters.
                  </div>
                )}
                {PassErr.diff && (
                  <div className="alert alert-warning" role="alert">
                    Passwords do not match.
                  </div>
                )}
                {PassErr.noSpecialChars && (
                  <div className="alert alert-warning" role="alert">
                    Password must contain at least one special character.
                  </div>
                )}
                <button onClick={handleSubmit} className="btn btn-primary btn-block">Register</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};