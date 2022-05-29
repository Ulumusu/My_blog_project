import './css/App.css'
import Footer from './components/Footer'
import PostList from './components/Posts'
import Header from './components/Header'
import Post from './components/Post'
import Resume from './components/Resume'
import AboutMe from './components/AboutMe'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';


function App () {
  return (
    <Router>
        <div className='app'>
          <div className='header-container'>
            <Header/>
          </div>
          <div className='rest-container'>
            <Routes>
              <Route path="/" exact element={<PostList/>} />
              <Route path="posts/:id" element={<Post/>} />
              <Route path='resume/' element={<Resume/>} />
              <Route path='about/' element={<AboutMe/>} />
            </Routes>
          </div>
        </div>
    </Router>
  );
}

export default App;