import { Redirect } from 'react-router-dom';
import React from 'react';

function loggedin(props) {
  if (window.sessionStorage.getItem('api_key')) {
    return (<div className="LoggedIn"> {props.children} </div>)
  }
  else {
    return (<div className="LoggedIn"></div>)
  }
}

export default loggedin;
