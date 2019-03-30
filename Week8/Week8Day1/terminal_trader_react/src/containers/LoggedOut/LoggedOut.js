import { Redirect } from 'react-router-dom';
import React from 'react';

function loggedout(props) {
  if (!window.sessionStorage.getItem('api_key')) {
    return (<div className="LoggedOut"> {props.children} </div>)
  }
  else {
    return (<div className="LoggedOut"></div>)
  }
}

export default loggedout;
