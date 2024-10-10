import React from 'react';
import LoadPosts from '../components/LoadPosts';
import ProfileHeader from '../components/ProfileHeader';

import {useParams } from 'react-router-dom';

export function UserProfile() {
  const { id } = useParams();
  return(<>
    <ProfileHeader user={id} />
    <LoadPosts url={`user_posts/${id}`} />
  </>);
};
//<LoadPosts url={`user_posts/${id}`} />
//<ProfileHeader user={id} />
// <LoadPosts url={`user_posts/${id}`} />