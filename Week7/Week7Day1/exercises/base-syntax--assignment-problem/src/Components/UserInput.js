import React from 'react'

const UserInput = (props) => {
    const inputStyle = {
            width: '30%'
    }
    

        return(
            <div>
                <h3>My UserInput Component</h3>
                <input id="input" style={inputStyle} type="text"  placeholder={props.value} onChange={props.change}></input>
            </div>
        )
}

export default UserInput