import React from 'react';
import LoadPosts from '../components/LoadPosts';

export function Following(event) {
  return(<>
    <LoadPosts url='following_posts' />
  </>);
}
;
