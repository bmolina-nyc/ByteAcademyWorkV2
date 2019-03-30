import React, { Component } from 'react';
import './App.css';
import NumberComponent from './components/NumberComponent'
import Home from './components/Home';
import {Route, BrowserRouter} from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Route exact path="/" component={Home}/>
          <Route path="/numbers" component={NumberComponent}/>
        </div>
      </BrowserRouter>

    );
  }
}

export default App;
