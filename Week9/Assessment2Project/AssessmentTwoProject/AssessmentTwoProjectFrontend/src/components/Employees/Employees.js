import React, { Component} from 'react';
import Employee from './Employee';
import {Redirect, Link} from 'react-router-dom';


class Employees extends Component {
    state = {
       loaded: false,
       submitted: false,
       employees: []
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/employees', {mode: 'cors'})
          .then(response => response.json())
          .then(data => this.setState({employees: data.employees}))
          .then(this.setState({loaded: true }))
      }

      onFormSubmit = (e) => {
          e.preventDefault()
          const fname = document.getElementById("fname").value 
          const lname = document.getElementById("lname").value 
          const title = document.getElementById("title").value 
          const dob = document.getElementById("dob").value 
          const branches_pk = document.getElementById("branches_pk").value 

          fetch('http://127.0.0.1:5000/addemployees',{
              method: 'post',
              mode: "cors",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify({fName: fname, lName: lname, title: title, dob:dob, branches_pk: branches_pk })
          }).then(response => response.json())
          .then(data => this.setState({
              submitted: true
          }))
      }
    

    render() {
        if (this.state.submitted){
          return <Redirect to='/' />
        }

        const employees = this.state.employees.map( (employee, idx) => {
            return <Link key={idx} to={'/employee/' + (employee.employee_pk) }>
               <Employee key={idx} id={employee.employee_pk} employee={employee}/>
            </Link>
        })

    //  Employees page needs a form to add employees 

        return (
            <div>

            <h2>Add an Employee</h2>
            <form>
                First Name<input type="Text" id="fname"></input>
                Last Name<input type="Text" id="lname"></input>
                Title Name<input type="Text" id="title"></input>
                DOB Name<input type="Text" id="dob"></input>
                Bank PK <input type="Text" id="branches_pk"></input>
                <button onClick={this.onFormSubmit}>Click to Add</button>
            </form>

            <h2>Click to see an employee</h2>
            {this.state.loaded && employees}
            </div>
        );
    }
}

export default Employees ;
