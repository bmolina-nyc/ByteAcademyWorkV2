import React from 'react';
import {Redirect} from 'react-router-dom';

function logout(props) {
  props.logoutFunc();
  return (
    <Redirect to='/login' />
  )
}

export default logout;
