import React from 'react';
import Logo from '../Logo/Logo'
import NavigationItems from '../NavigationItems/NavigationItems';

// import './ToolBar.css'

const Toolbar = (props) => (
    <header className="Toolbar">
    <div className="Logo">
    <Logo link='/'/>
    </div>
        <NavigationItems/>
    </header>
)

export default Toolbar;
