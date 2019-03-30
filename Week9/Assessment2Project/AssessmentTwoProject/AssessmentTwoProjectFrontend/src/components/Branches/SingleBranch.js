import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';


class SingleBranch extends Component{

    state = {
        branchName: null,
        city: null,
        state: null,
        zip: null,
        id: null,
        submitted: null,
        deleted: null
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000' + this.props.location.pathname,{
            method: 'get',
            mode: 'cors',
            headers: {"Content-Type": "application/json"},
        })
        .then(response => response.json())
        .then(data => { 
            const branch = data['branch'][0]
            this.setState({
                branchName: branch['branchName'],
                city: branch['city'],
                state: branch['state'],
                zip: branch['zip'],
                id: branch['id']
            })
        })
    }

    onFormSubmit = (e) => {
        e.preventDefault()
        const branchName = document.getElementById("branchName").value 
        const city = document.getElementById("city").value 
        const state = document.getElementById("state").value 
        const zip = document.getElementById("zip").value 

        fetch('http://127.0.0.1:5000/updatebranch/' + this.state.id, {
            method: 'put',
            mode: "cors",
            headers: {"Content-Type": "application/json, Access-Control-Allow-Origin"},
            body: JSON.stringify({branchName: branchName, city: city, state: state, zip:zip})
        }).then(response => response.json())
          .then(data => console.log(data["Message"]))
          .then(this.setState({submitted: true }))
    }


    onDelete = (e) => {
        e.preventDefault()
        fetch('http://127.0.0.1:5000/deletebranch/' + this.state.id, {
            method: 'put',
            mode: "cors",
            headers: {"Content-Type": "application/json"},
        }).then(response => response.json())
        .then(data => console.log(data["Message"]))
        .then(this.setState({deleted: true }))
    }
    


    render(){
        if (this.state.submitted || this.state.deleted){
            return <Redirect to='/' />
          }

        if (this.state.branchName === null){
            return <p>Not Loaded</p>
        } else {
        return(
            <div>
                Branch: {this.state.branchName}
                <br/>
                City, St: {this.state.city}, {this.state.state}
                <br/>
                Zip: {this.state.zip}

                <h2>Edit this Branch</h2>
                <form>
                    Branch<input type="text" id="branchName"></input>
                    City<input type="text" id="city"></input>
                    State<input type="text" id="state"></input>
                    Zip<input type="text" id="zip"></input> 
                    <br/>
                    <button onClick={this.onFormSubmit}>Click to Edit</button>
                </form>
                <button id="delete" onClick={this.onDelete}>Click to Delete</button>
            </div>
            )
        }
    }
}

export default SingleBranch;
