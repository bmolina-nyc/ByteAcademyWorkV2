import React from 'react'

const UserOutput = (props) => {
    const textStyle={
        margin: '40px',
        padding: '10px'
    }
    const name={
        color: 'red'
    }
        return(
            <div>
            <h4 >My UserOutput Component</h4>
            <h4 >My name is <b style={name}>{props.username}</b></h4>
                <p style={textStyle}>This is paragraph one</p>
                <p style={textStyle}>This is paragraph two</p>
            </div>
        )  
}

export default UserOutput