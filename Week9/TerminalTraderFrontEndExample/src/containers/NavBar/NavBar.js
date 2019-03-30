import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import LoggedIn from '../LoggedIn/LoggedIn'
import LoggedOut from '../LoggedOut/LoggedOut'

class NavBar extends Component {
  render () {
    return (
      <nav className="NavBar">
        <Link to="/">Home</Link>
        <LoggedOut>
          <Link to="/login">Login</Link>
        </LoggedOut>
        <LoggedIn>
          <Link to="/balance">Balance</Link>
        </LoggedIn>
        <LoggedIn>
          <Link to="/logout">Log Out</Link>
        </LoggedIn>
      </nav>
    )
  }
}

export default NavBar;
