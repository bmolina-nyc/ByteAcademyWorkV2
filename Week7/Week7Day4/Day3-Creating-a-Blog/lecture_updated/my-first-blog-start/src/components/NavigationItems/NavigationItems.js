import React from 'react';
import NavigationItem from '../NavigationItem/NavigationItem'
import './NavigationItems.css'


const NavigationItems = () => (
    <ul className="NavigationItems" >
        <NavigationItem link="/blog"> Blog </NavigationItem>
        <NavigationItem link="/"> Home </NavigationItem>
    </ul>
)

export default NavigationItems