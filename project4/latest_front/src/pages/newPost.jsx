import React, { useState } from 'react';

export function NewPost(event) {
    const [formData, setFormData] = useState({
        name: '',
        text: ''
      });
    
      const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
          ...prevFormData,
          [name]: value
        }));
      };
    
      const handleSubmit = (event) => {
        event.preventDefault();
    
        axios.post('/api/new_post', {
          body: JSON.stringify(formData),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then(() => {
            // Optionally reset the form or show a success message
            setFormData({
              name: '',
              text: ''
            });

            window.location.href = `/all_posts`;
          })
          .catch((error) => {
            console.error('Error:', error);
            // Optionally show an error message
          });
      };
    
      return (
        <div className="container mt-5">
          <h2>Create a Post</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="nameInput">Post title</label>
              <input
                type="text"
                className="form-control"
                id="nameInput"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="textInput">Post</label>
              <textarea
                className="form-control"
                id="textInput"
                name="text"
                rows="3"
                value={formData.text}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            <button type="submit" className="btn btn-light">
                <i className="bi bi-check-circle"></i> Submit
            </button>
          </form>
        </div>
      );
}