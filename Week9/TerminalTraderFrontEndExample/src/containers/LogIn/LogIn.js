import React, {Component} from 'react';

class LogIn extends Component {

  loginClick = (event) => {
    event.preventDefault()
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value
    this.props.loginFunc(username, password);
  }

  render () {
    return (
      <div className="LogIn">
        <form>
          <div className="row">
            <label htmlFor="username">Username: </label>
            <input name="username" id="username" placeholder="username" />
          </div>
          <div className="row">
            <label htmlFor="password">Password: </label>
            <input name="password" id="password" type="password" placeholder="password" />
          </div>
          <div className="row">
            <button onClick={this.loginClick}>Log In</button>
          </div>
        </form>
      </div>
    );
  }
}

export default LogIn;
