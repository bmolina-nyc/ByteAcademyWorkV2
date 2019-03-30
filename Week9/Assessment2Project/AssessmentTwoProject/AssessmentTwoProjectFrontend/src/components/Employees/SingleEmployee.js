import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
class SingleEmployee extends Component {

    state = {
        employee: null,
        submitted: null,
        deleted: null,
        message: null
     }
  
     componentDidMount() {
            fetch('http://127.0.0.1:5000' + this.props.location.pathname,{
                method: 'get',
                mode: 'cors',
                headers: {"Content-Type": "application/json"},
            })
            .then(response => response.json())
            .then(data => {
                this.setState({
                    employee: data['employee'][0]
            })})
        }

        onFormSubmit = (e) => {
            e.preventDefault()
            const fname = document.getElementById("fname").value 
            const lname = document.getElementById("lname").value 
            const title = document.getElementById("title").value 
            const dob = document.getElementById("dob").value 
            const branches_pk = document.getElementById("branches_pk").value 
  
            fetch('http://127.0.0.1:5000/updateemployee/' + this.state.employee.id, {
                method: 'put',
                mode: "cors",
                headers: {"Content-Type": "application/json, Access-Control-Allow-Origin"},
                body: JSON.stringify({fName: fname, lName: lname, title: title, dob:dob, branches_pk: branches_pk })
            }).then(response => response.json())
              .then(data => console.log(data["Message"]))
              .then(this.setState({submitted: true }))
        }

        onDelete = (e) => {
            e.preventDefault()
            fetch('http://127.0.0.1:5000/deleteemployee/' + this.state.employee.id, {
                method: 'put',
                mode: "cors",
                headers: {"Content-Type": "application/json, Access-Control-Allow-Origin"},
            }).then(response => response.json())
            .then(data => console.log(data["Message"]))
            .then(this.setState({deleted: true }))
        }
        




    render(){
        if (this.state.submitted || this.state.deleted){
            return <Redirect to='/' />
          }

        if (this.state.employee === null){
            return <p>Not Loaded</p>
        } else {
            return (
                <div>
                    First Name: {this.state.employee.fName}
                    <br/>
                    Last Name: {this.state.employee.lName}
                    <br/>
                    Title: {this.state.employee.title}
                    <br/>
                    DOB: {this.state.employee.dob}
                    <br/>
                    Branch_PK: {this.state.employee.branches_pk}

                    <h2>Edit this Employee</h2>
                <form>
                    First Name<input type="Text" id="fname"></input>
                    Last Name<input type="Text" id="lname"></input>
                    Title Name<input type="Text" id="title"></input>
                    DOB Name<input type="Text" id="dob"></input>
                    Bank PK <input type="Text" id="branches_pk"></input>
                    <br/>
                    <button onClick={this.onFormSubmit}>Click to Edit</button>
                </form>

                <button id="delete" onClick={this.onDelete}>Click to Delete</button>
                </div>
            )
        }
    }
}




export default SingleEmployee;