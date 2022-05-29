import React, {useState, useEffect} from "react";
import {Link} from 'react-router-dom';
import '../css/Posts.css';

const PostList = () => {
  let [posts, setPosts] = useState([])

  useEffect(() => {
    getPosts()
  }, [])

  let getPosts = async () => {
    let response = await fetch('api/posts/')
    let data = await response.json()
    setPosts(data)
  }

  return (
      <div className="posts-list">
        {posts.map((post, index) => (
            <Link to={`posts/${post.id}`}>
              <div className="card-border">

                <div className="card" style={{backgroundImage: `url(${post.main_picture})`}}>

                    <div className="card-title-date">
                      <h3 key={index} className='card-title'>{post.title}</h3>
                      <p className="card-date">{post.updated}</p>
                    </div>

                    <div className="card-body">
                      <p className="card-text">{post.beginning}</p>
                    </div>

                </div> 
                  
              </div>
            </Link>
        ))}
      </div>
  )
};

export default PostList;