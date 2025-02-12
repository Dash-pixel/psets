import React from 'react';

function PostedBy({ userId, username, UserProfile }) {
  return (
    <p className="">
      Posted by
      <span className="font-bold">
        <a href={`user_profile/${userId}`} data-user={userId} onClick={UserProfile}>
          {username}
        </a>
      </span>
    </p>
  );
}

export default PostedBy;