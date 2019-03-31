import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import Home from './containers/Home/Home';
import Branches from './components/Branches/Branches';
import Employees from './components/Employees/Employees';
import SingleEmployee from './components/Employees/SingleEmployee';
import SingleBranch from './components/Branches/SingleBranch';
import Toolbar from './components/ToolBar/ToolBar';
// import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Toolbar /> 
        <Switch>
           <Route exact path = "/" component={Home}/>
           <Route exact path = "/employees" component={Employees}/>
           <Route exact path = "/branches" component={Branches}/>
           <Route path = "/employee/:id" component={SingleEmployee} />
           <Route path = "/branch/:id" component={SingleBranch} />
        </Switch>
      </div>
    );
  }
}

export default App;
