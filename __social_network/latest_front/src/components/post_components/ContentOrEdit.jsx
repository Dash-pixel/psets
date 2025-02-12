import React from 'react';

const ContentOrEdit = (props) => {
    if (!props.edit_mode) {
      return (<p className="card-text content">{props.content}</p>);
    }
    else {
      return (
        <p className="card-text content">
          <textarea cols="40" rows="10" className="form-control" onChange={props.handleEdit} value={props.edit_value} />
          <br />
          <button className="btn btn-light" onClick={props.editContent}>
            <i className="bi bi-check-circle"></i> Submit
          </button>
        </p>
      );
    }
  };

export default ContentOrEdit;

/*
              <ContentOrEdit 
              editContent={editContent} 
              handleEdit={handleEdit} 
              content={props.props.content} 
              edit_mode={data.edit_mode}
              edit_value={data.edit_value}
            />
*/