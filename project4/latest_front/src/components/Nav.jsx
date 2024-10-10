import{ useEffect, useState, useContext } from 'react';
import { TokenContext } from './TokenWrapper';
import NavLinkItem from './NavLinkItem';
import { NavLink } from 'react-router-dom';

export const Nav = () => {
  const {token} = useContext(TokenContext);
  return (
    <nav className="sticky top-0 left-0 right-0 bg-light-bg shadow-md">
      <div className="px-4 py-2 flex flex-wrap">
        <div className='pr-4 h-full'>
          <NavLink className="text-3xl font-raleway font-extrabold italic" to="/">Net_worker
          </NavLink> 
        </div>
        <div className="px-4 py-2 flex flex-wrap h-full">
          <NavLinkItem to="/all_posts">All Posts</NavLinkItem>
          {token.token ? (
            <>
              <NavLinkItem to={`/user_profile/${token.id}`}>User Profile</NavLinkItem>
              <NavLinkItem to="/following">Following</NavLinkItem>
              <NavLinkItem to="/new_post">New Post</NavLinkItem>
              <NavLinkItem to="/logout">Log out</NavLinkItem>
            </>
          ) : (
            <>
              <NavLinkItem to="/register">Register</NavLinkItem>
              <NavLinkItem to="/login">Log in</NavLinkItem>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Nav;
