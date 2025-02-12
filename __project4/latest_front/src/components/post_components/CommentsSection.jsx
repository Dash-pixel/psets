import React, {useContext} from 'react';
import { TokenContext } from '../TokenWrapper';


const CommentsSection = (props) => {
  const {token} = useContext(TokenContext);

  var comments = null;
  if (props.comments){
    comments = props.comments.map(comment=> {
    return(
      <li className="list-group-item" key={comment.id}>
        {comment.comment}
      </li>)})
  };
  return(
    <>
      {comments && <ul className="list-group mb-3">{comments}</ul>}
      <div className="input-group mb-3">
      {token.token &&
        <>
          <input
            type="text"
            className="form-control"
            aria-describedby="basic-addon2"
            value={props.commentValue}
            onChange={props.handleComment}
            onKeyDown={(event) => {
              if (event.key === 'Enter') {
                props.writeComment();
              }
            }}
          />
            <div className="input-group-append" >
              <button className="btn btn-outline-secondary" onClick={props.writeComment}>Post Comment</button>
            </div>
        </>
      }
      </div>
    </>
  )
};


export default CommentsSection;
