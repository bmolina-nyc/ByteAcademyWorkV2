import React, { Component} from 'react';
import Branch from './Branch';
import {Link, Redirect} from 'react-router-dom';

class Branches extends Component {
    state = {
        loaded: false,
        submitted: false,
        branches: []
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/branches', {mode: 'cors'})
          .then(response => response.json())
          .then(data => this.setState({branches: data.branches}))
          .then(this.setState({loaded: true }))
    }

    onFormSubmit = (e) => {
        e.preventDefault()
        
        const branchName = document.getElementById("branchName").value 
        const city = document.getElementById("city").value 
        const state = document.getElementById("state").value 
        const zip = document.getElementById("zip").value 
        fetch('http://127.0.0.1:5000/addbranch',{
            method: 'post',
            mode: "cors",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({branchName: branchName, city: city, state: state, zip:zip})
        }).then(response => response.json())
        .then(data => this.setState({
            submitted: true
        })).then(console.log("Branch Added"))
    }
  



    render() {

        if (this.state.submitted){
            return <Redirect to='/' />
        }

        const branches = this.state.branches.map( (branch, idx) =>{
            return <Link key={idx} to={'/branch/' + (branch.branch_pk) }>
            <Branch key={idx} id={branch.branch_pk} branch={branch}/>
         </Link>
        })
        return (
            <div>
            <h2>Add a branch</h2>
            <form>
                Branch<input type="text" id="branchName"></input>
                City<input type="text" id="city"></input>
                State<input type="text" id="state"></input>
                Zip<input type="text" id="zip"></input> 
                <br/>
                <button onClick={this.onFormSubmit}>Click to add</button>
            </form>
            <h2>Click to see a Branch</h2>
            {this.state.loaded && branches}
            </div>
        );
    }
}


export default Branches;
