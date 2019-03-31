import React from 'react';
import NavigationItem from '../NavigationItem/NavigationItem'
// import './NavigationItems.css'


const NavigationItems = () => (
    <ul className="NavigationItems" >
        <NavigationItem link="/branches"> Branch </NavigationItem>
        <NavigationItem link="/employees"> Employees </NavigationItem>
        <NavigationItem link="/"> Home </NavigationItem>
    </ul>
)

export default NavigationItems;
