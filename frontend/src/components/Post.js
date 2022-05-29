import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import '../css/Post.css';

const Post = () => {

    let postId = useParams();
    let [post, setPost] = useState(null)

    useEffect(() => {
      let getPost =  async () => {
        let response = await fetch(`/api/posts/${postId.id}`)
        let data = await response.json()
        console.log(data)
        setPost(data)
      }

      getPost()
  }, [postId.id])

    return (
      <div className="post-box">
        <div className="post-container">

          <div className="post-picture" style={{backgroundImage: `url(${post?.main_picture})`}}>

            <div className="post-title-date">
              <h3 className='post-title'>{post?.title}</h3>
              <p className="post-date">{post?.updated}</p>
            </div>
          </div> 
          <div className="post-body">
            <p className="post-beginning">{post?.beginning}</p>
            <br/>
            <p>{post?.main_text}</p>
            <div className='next-picture'>
              {post?.texts.map((texts,index) => (
                <div>
                  <div className='text-picture-container'>
                    <img key={index} src={texts.picture} alt='another picture in post' className='text-picture'/>
                  </div>
                  <p key={index}>{texts.text}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
};

export default Post;
