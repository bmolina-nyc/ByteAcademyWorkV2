import React from 'react';


const Employee = (props) => (
    <div className="employee">
        <div>
            {props.employee.fName} {props.employee.lName}
        </div>
    </div>
)

export default Employee;


