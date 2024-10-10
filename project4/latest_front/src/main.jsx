import axios from 'axios';
import './main.css';
import { createRoot } from 'react-dom/client';
import { UserProfile } from './pages/userProfile';
import { AllPosts } from './pages/allPosts';
import { Following } from './pages/following';
import { NewPost } from './pages/newPost';
import {BrowserRouter, Routes, Route} from "react-router-dom"
import {Nav} from './components/Nav'
import { Register } from './pages/register';
import { Login } from './pages/login';
import { Logout } from './pages/logout';
import { TokenWrapper } from './components/TokenWrapper';


const root = createRoot(document.getElementById('root'));

axios.interceptors.request.use((config) => {
  config.withCredentials = true;
  if (window.csrfToken)
  {
    config.headers = {
      ...config.headers,
      'X-CSRFToken': window.csrfToken
    };
  }
  return config;
});

axios.interceptors.response.use((response) => response.data, (error) => {
  if (error.response.status === 401) {
    axios.get('/api/refresh_token')
  }

})

root.render(
    <BrowserRouter>
      <TokenWrapper>    
        <Nav/>
        <Routes>
          <Route path="/" element={<Following />} />
          <Route path="/all_posts" element={<AllPosts />} />
          <Route path="/following" element={<Following />} />
          <Route path="/user_profile/:id" element={<UserProfile />} />
          <Route path="/new_post" element={<NewPost />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
      </TokenWrapper>
    </BrowserRouter>
);

//<Route path="/" element={<Home />} />
