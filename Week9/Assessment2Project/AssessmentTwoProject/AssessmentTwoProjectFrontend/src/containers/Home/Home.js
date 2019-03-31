import React, { Component } from 'react';

import './Home.css';

class Home extends Component {

    onFormLogin = (e) => {
        e.preventDefault()
        const username = document.getElementById("username").value 
        const password = document.getElementById("password").value 
 
        fetch('http://127.0.0.1:5000/login', {
                method: 'post',
                mode: "cors",
                headers: {"Content-Type": "application/json, Access-Control-Allow-Origin"},
                body: JSON.stringify({username: username, password: password})
            }).then(response => response.json())
            .then(data => window.api_key = data['api_key'])
    }

    render () {
        return (
            <div>
            <h1>Admin Login</h1> 
                <form>
                    Username<input type="username" id="username"></input>
                    Password<input type="password" id="password"></input>
                    <button onClick={this.onFormLogin}>Click to Login</button>
                </form>
            </div>
         
        );
    }
}

export default Home;
