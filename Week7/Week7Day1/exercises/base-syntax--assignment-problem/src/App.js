import React, { Component } from 'react';
import './App.css';
import UserInput from './Components/UserInput';
import UserOutput from './Components/UserOutput';

class App extends Component {

  state = {
    username: 'Bruce'
  }


 
  onChange = (event) => {
    this.setState({username: event.target.value})
  }

  render() {
    const background = {
      font: 'inherit'
    }
    // const originalName = document.getElementById('input').getAttribute('placeholder')
    return (
      <div className="App" style={background}>
        <UserInput change={this.onChange} value={this.state.username} />
        <hr/>
        <UserOutput username={this.state.username}/>
      </div>
    );
  }
}

export default App;
