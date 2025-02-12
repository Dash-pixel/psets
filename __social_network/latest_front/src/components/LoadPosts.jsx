import React, { useEffect } from 'react';
import PostComponent from './PostComponent';
import axios from 'axios';


const LoadPosts = ({url}) => { // i need to make load posts container scrollable with fixed height
  const  [newPostList, setNewPostList] = React.useState([]); 
  const scrollRef = React.useRef(null);
  const lastPost = React.useRef(null);
  var headers = {};

  if (localStorage.getItem('authToken')) {
    headers = {'Authorization': `Token ${localStorage.getItem('authToken')}`};
  }

  useEffect(() => {
    axios.get(`/api/${url}`) 
    .then(postArray => {
      setNewPostList(() => postArray.map(item => {
      return(<PostComponent props={item} key={item.id}/>)
      }));
      lastPost.current = postArray[postArray.length-1].id 
    });
    
  }, [url]); 



  const scrolled = () => {
    if (scrollRef.current && lastPost.current) {
      const { scrollTop, scrollHeight, clientHeight } = scrollRef.current;
      if (scrollTop + clientHeight + 10 >= scrollHeight) {
        axios.get("/api/"+ url + `?from=${lastPost.current}`)
        .then(postArray => {
          if (postArray.length){
            lastPost.current = postArray[postArray.length-1].id;   
            setNewPostList((old) => {
              return [...old, ...postArray.map(item => {
                return(<PostComponent props={item} key={item.id}/>)
                })];
            })
          }
          else{
            lastPost.current = null;
          }
     
        });
      }
    }
  }

  return(<div id="selected-posts" onScroll={scrolled} ref={scrollRef}>
    <div className='flex flex-wrap'>
      {newPostList}
    </div>
  </div>);
};

export default LoadPosts;
