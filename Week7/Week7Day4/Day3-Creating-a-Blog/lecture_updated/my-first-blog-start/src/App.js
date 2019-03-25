import React, { Component } from 'react';
import {Route} from 'react-router-dom';

import Blog from './containers/Blog/Blog';
import Home from './containers/Home/Home';
import Layout from './hoc/Layout/Layout';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Layout>
          <Route path="/blog" component={Blog}/>
          <Route path="/" component={Home}/>
        </Layout>
      </div>
    );
  }
}

export default App;