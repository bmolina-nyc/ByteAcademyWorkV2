import React from 'react';


const Branch = (props) => (
    <div className="branch">
        {props.branch.branchName}, {props.branch.city}, {props.branch.state}
    </div>
)

export default Branch