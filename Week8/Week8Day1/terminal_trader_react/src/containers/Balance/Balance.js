import React, {Component} from 'react';
import apiRequest from '../../client/apiRequest';

class Balance extends Component {
  state = {update: null, balance: null}

  componentDidMount = () => {
    if (this.state.balance === null) {
      apiRequest(`/api/${window.sessionStorage.getItem('api_key')}/balance`)
        .then(response=>response.json()).then(json=>{
          if (json.balance || json.balance === 0) {
            this.setState({balance: json.balance, update: "balance received"})
          }
          })
    }
  }

  render() {
    return(
      <div classname="Balance">
        your balance is ${this.state.balance}
      </div>
    )
  }
}

export default Balance
