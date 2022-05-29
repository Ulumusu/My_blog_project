import React from "react";
import { IoHomeSharp, IoHelpSharp, IoCardSharp } from "react-icons/io5";

export const SidePanelData = [
    {
        title: 'Github.io',
        path: '/git',
        icon: <IoHomeSharp />,
        cName: 'nav-text'
    },
    {
        title: 'Posty',
        path: '/',
        icon: <IoHomeSharp />,
        cName: 'nav-text'
    },
    {
        title: 'O mnie',
        path: '/about/',
        icon: <IoHelpSharp />,
        cName: 'nav-text'
    },
    {
        title: 'CV',
        path: 'resume/',
        icon: <IoCardSharp />,
        cName: 'nav-text'
    },
    {
        title: 'LinkedIn',
        path: '/contact/',
        icon: <IoCardSharp />,
        cName: 'nav-text'
    }, 
];