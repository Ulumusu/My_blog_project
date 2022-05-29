import React, {useState, useEffect} from 'react';
import axios from "axios"
import '../css/About.css';

const AboutMe = () => {
  let [about, setInfo] = useState(null)

  useEffect(() => {
    let getInfo =  async () => {
      const response = await axios.get(
        'http://127.0.0.1:8000/api/about/');
        setInfo(response.data[0])
    }
    getInfo()
  }, [])

  return (
      <div className="about-container">
        <div className='about-elements'>
          <h1 className='about-title'>O mnie</h1>
          <p>{about?.beginning}</p>

          <div className='next-picture'>
              {about?.parts.map((part,index) => (
                <div>
                  <div className='about-picture-container'>
                    <img src={part?.picture} alt='Main picture' className='about-picture'/>
                  </div>
                  <br></br>
                  <p key={index}>{part?.text}</p>

                </div>
              ))}
          </div>
        </div>
      </div>
  )
};

export default AboutMe;