import React, {Component} from 'react'
import {NavLink} from 'react-router-dom'


const Home = () => {
    return (
        <div>
            <h1>
            Welcome to this quiz
            </h1>                         
            <NavLink to="/numbers">Go to Numbers</NavLink>
    </div>
    )
}

export default Home;