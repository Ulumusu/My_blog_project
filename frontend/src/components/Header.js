import React from 'react';
import Panel from './Panel';
import '../css/Header.css';

const Header = () => {
  return (
    <div className='header-container'>
      <Panel/>
      <h1 className='blogName'>UluBlog</h1>
    </div>
  );
};

export default Header;
