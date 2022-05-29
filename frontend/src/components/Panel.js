import { IoListSharp, IoCloseSharp } from "react-icons/io5";
import { Link } from "react-router-dom";
import React, { useState } from "react";
import { SidePanelData } from './SidePanelData';
import '../css/Panel.css';

function Panel() {
    const [sidePanel, setSidePanel] = useState(false)
    const showSidePanel = () => setSidePanel(!sidePanel)
    return (
        <>
        <div className="panel">
            <Link to='#' className="panel-bars">
                <IoListSharp size={45} onClick={showSidePanel}/>
            </Link>
        </div>
        <nav className={sidePanel ? 'nav-panel active' : 'nav-panel'}>
            <ul className='nav-panel-items' onClick={showSidePanel}>
                <li className="panel-toggle">
                    <Link to='#' className="panel-bars">
                        <IoCloseSharp/>
                    </Link>
                </li>
                    {SidePanelData.map((item, index) => {
                    return (
                        <li key={index} className={item.cName}>
                            <Link to={item.path}>
                                {item.icon}
                                <span>{item.title}</span>
                            </Link>
                        </li>
                    )  
                    })}
            </ul>
        </nav>
        </>
    );
}

export default Panel