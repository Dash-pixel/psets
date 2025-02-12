import axios from 'axios';
import React, { useEffect } from 'react';

const ProfileHeader = (props) => {
  const [profile, setProfile] = React.useState();
  
  useEffect(() => {
    axios.get(`/api/user_profile/${props.user}`)
    .then(variable => {
      
      return setProfile(variable)})
  }, [props.user])

  function toggleFollow(){
    axios.post(`/api/subscribe/${props.user}`, {
    })
    .then(subscrib => {
      setProfile(oldsubscib => ({
        ...oldsubscib,
        'followers':subscrib.followers
      }));
    });
  }

  return(
    <div className="container" id="profile">
        <div className="row">
            <div className="col-md-12 text-center">
                {profile && <><h1> {profile.username} </h1>
                <p><strong>Followers:</strong> <span id="followerCount">{profile.followers}</span></p>
                <p><strong>Following:</strong> <span id="followingCount">{profile.following}</span></p>
                </>}
                {profile && (window.userId != profile.id) && 
                  <button id="followBtn" className="btn btn-light" onClick={toggleFollow}>
                    <i className="bi bi-person-plus"></i> Follow
                  </button>
                }
            </div>
        </div>
    </div>
  )
};


export default ProfileHeader;
