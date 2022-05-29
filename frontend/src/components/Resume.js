import axios from "axios"
import React, {useState, useEffect} from 'react';
import '../css/Resume.css';

const Resume = () => {
  let [resume, setResume] = useState(null)

  useEffect(() => {
    let getResume =  async () => {
      const response = await axios.get(
        'http://127.0.0.1:8000/api/resume/');
        setResume(response.data[0])
    }
    getResume()
  }, [])

  return (
    <div>
      <div className="resume-container">
        <div className="resume-elements">
          <h1>{resume?.name_surname}</h1>
          <h4>Kontakt:</h4>
          <p>e-mail: {resume?.email_info}</p>
          <p>LinkedIn</p>
        </div>

        <div className='resume-elements'>
          <h3 className="element-title">Doświadczenie</h3>
              {resume?.competences.map((competence,index) => {
                if (competence?.choice === 1){
                  return (
                    <div>
                      <h4 key={index}>Stanowisko: {competence?.title}</h4>
                      <h4 key={index}>Firma: {competence?.company}</h4>
                      <p key={index}>{competence?.start_date} - {competence?.end_date}</p>
                      <p>Branża: {competence?.type}</p>
                      <p key={index}>{competence?.details}</p>
                      <br/>
                    </div>
                  )
                } else {return (null)}
              })}    
        </div>
        
        <div className='resume-elements'>
          <h3 className="element-title">Edukacja</h3>
              {resume?.competences.map((competence,index) => {
                if (competence.choice === 1){
                  return (
                    <div>
                      <h4 key={index}>Profil: {competence.title}</h4>
                      <h4 key={index}>Uczelnia: {competence.company}</h4>
                      <p key={index}>{competence.start_date} - {competence.end_date}</p>
                      <p key={index}>{competence.details}</p>
                      <br/>
                    </div>
                  )
                } else {
                  return (null)
                }                
              })}    
        </div>

        <div className='resume-elements'>
          <h3 className="element-title">Certyfikaty</h3>
              {resume?.competences.map((competence,index) => {
                if (competence.choice === 1){
                  return (
                    <div>
                      <h4 key={index}>Nazwa: {competence.title}</h4>
                      <h4 key={index}>Firma: {competence.company}</h4>
                      <p key={index}>{competence.start_date} - {competence.end_date}</p>
                      <p key={index}>{competence.details}</p>
                      <br/>
                    </div>
                  )
                } else {
                  return (null)
                }
              })}    
        </div>

        <div className='resume-elements'>
          <h3 className="element-title">Hobby</h3>
              {resume?.competences.map((competence,index) => {
                 if (competence.choice === 1){
                   return (
                     <div>
                      <h4 key={index}>Nazwa: {competence.title}</h4>
                      <h4 key={index}>Firma: {competence.company}</h4>
                      <p key={index}>{competence.start_date} - {competence.end_date}</p>
                      <p key={index}>{competence.details}</p>
                      <br/>
                    </div>
                  )
                } else {
                  return (null)
                }
              })}    
        </div>

      </div>
    </div>
  );
};

export default Resume;