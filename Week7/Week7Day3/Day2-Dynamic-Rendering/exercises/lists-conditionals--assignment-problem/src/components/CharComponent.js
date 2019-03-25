import React from 'react'

const CharComponent = (props) => {

    return(
        <div onClick={props.clicked} id="charComponent" >{props.letter}</div>
    )
}

export default CharComponent