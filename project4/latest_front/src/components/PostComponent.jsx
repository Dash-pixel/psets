import React from 'react';
import {UserProfile} from '../pages/userProfile';
import CommentsSection from './CommentsSection';
import ContentOrEdit from './ContentOrEdit';
import moment from 'moment';
import PostedBy from './post_components/PostedBy';
import Button from './Button';
import axios from 'axios';
import Heart from './Heart';

const PostComponent = (props) => {
  const [data, setData] = React.useState({
    'likes': props.props.like_count,
    'liked': props.props.liked,
    'comments': null,
    'com_visible': false,
    'edit_mode': false,
    'edit_value': props.props.content,
    'text_content': props.props.content
  });
  function toggleLike() {
    axios.post(`/api/like/${props.props.id}`)
      .then(new_likes => {
        setData(old => ({
          ...old,
          likes: new_likes.count,
          liked: new_likes.liked
        }));
      });
  };
  async function openComments() {
    if (!data.com_visible) {
      await fetchComments();
    }
    setData(old => ({ ...old, 'com_visible': !old.com_visible }));
  };
  function fetchComments() {
    axios.get(`/api/comments/${props.props.id}`)
      .then(comments => {
        setData(old => ({
          ...old,
          'comments': comments,
        }));
      });
  };
  function writeComment() {
    axios.post(`/api/comments/${props.props.id}`, {
      body: data.commentValue
    })
      .then(() => setData((old) => {
        return ({ ...old, 'commentValue': '', });
      }))
      .then(() => fetchComments());
  };
  const handleComment = (event) => {
    return setData(old => {
      return ({
        ...old,
        'commentValue': event.target.value
      });
    });
  };
  const toggleEdit = () => {
    setData(old => { return ({ ...old, 'edit_mode': !old.edit_mode }); });
  };
  const editContent = () => {
    axios.post(`/api/edit/${props.props.id}`, {
      body: data.edit_value,
    })
    .then(() => setData(old => {return({ ...old, 'edit_mode': false, 'text_content': data.edit_value}); }));
  };
  const handleEdit = (event) => setData((old) => {
    return ({ ...old, 'edit_value': event.target.value });
  });

  return (
    <div className='bg-light-bg rounded-lg p-2 m-2 w-96 h-auto'>
      <div>
        <div className="text-2xl font-bold text-light-txt">{props.props.title}</div>
        <div className="card-subtitle mb-2 created_at">{moment(props.props.created_at).fromNow()}</div>
        <ContentOrEdit 
          editContent={editContent} 
          handleEdit={handleEdit} 
          content={data.text_content} 
          edit_mode={data.edit_mode}
          edit_value={data.edit_value}
        />
        <Heart liked={data.liked} onClick={toggleLike} count={data.likes}/>

        <Button onClick={toggleLike} icon="bi bi-hand-thumbs-up" label={`Like ${data.likes}`}/>

        <Button onClick={openComments} icon="bi bi-chat-left-text" label="Comments"/>

        {localStorage.getItem('userId') == props.props.user_id && (
        <Button onClick={toggleEdit} icon="bi bi-pencil-square" label="Edit Post"/>
        )}

      </div>

      <PostedBy userId={props.props.user_id} username={props.props.user__username} UserProfile={UserProfile} />

      {data.com_visible && // костыль, изменить
        <CommentsSection
          comments={data.comments}
          post_id={props.props.id}
          commentValue={data.commentValue}
          handleComment={handleComment}
          writeComment={writeComment} 
      />}
    </div>
  );
};

export default PostComponent;
