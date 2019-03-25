import React from 'react';
import NavigationItems from '../NavigationItems/NavigationItems';

import './ToolBar.css'
import Logo from '../Logo/Logo'


const Toolbar = (props) => (
    <header className="Toolbar">
    <div className="Logo"><Logo link="google.com"/></div>
        <NavigationItems/>
    </header>
)

export default Toolbar; 