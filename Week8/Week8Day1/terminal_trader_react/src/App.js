import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Route} from 'react-router-dom';
import HomeView from './containers/HomeView/HomeView';
import NavBar from './containers/NavBar/NavBar';
import LogIn from './containers/LogIn/LogIn';
import LogOut from './containers/LogOut/LogOut';
import Balance from './containers/Balance/Balance';
import apiRequest from '../src/client/apiRequest'
import logo from './logo.svg';
import './App.css';

class App extends Component {

  state = { update: "" }

  login = (username, password) => {
    apiRequest("/api/getkey", "post", {username: username, password: password})
      .then(response => response.json()).then(json => {
        if (json.api_key) {
          window.sessionStorage.setItem('api_key', json.api_key)
          window.sessionStorage.setItem('username', json.username)
          console.log(json)

          this.setState({update: "logged in"})
        }
      })
  }

  logout = () => {
    console.log("LOGOUT") 
    window.sessionStorage.setItem('api_key', '')
    this.setState({update: "logged out"})
  }



  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <NavBar />
          <main>
            <Route exact path="/" component={HomeView} />
            <Route path="/login" render={() => <LogIn loginFunc={this.login} />} />
            <Route path="/logout" render={() => <LogOut logoutFunc={this.logout} />} />
            <Route path="/balance" component={Balance} />
          </main>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
