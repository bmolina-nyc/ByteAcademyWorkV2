import React, {Component} from 'react'


const ValidationComponent = (props) => {

    return (
        <div>
            { props.textLength <= 5 ?  <b> Text too short </b> : <b> Text long enough</b>}
        </div>
    )

}

export default ValidationComponent;