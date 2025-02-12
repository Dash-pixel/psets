import React from 'react';
import LoadPosts from '../components/LoadPosts';

export function AllPosts(event) {
  return(<>
    <LoadPosts url='all_posts' />
  </>);
}
;
