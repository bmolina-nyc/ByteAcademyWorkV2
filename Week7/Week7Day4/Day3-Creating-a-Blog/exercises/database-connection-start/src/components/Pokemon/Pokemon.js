import React from 'react';
import './Pokemon.css'

const Pokemon = (props) => {
    return(
       
        <article className="eachPokemon" onClick={props.clicked}>
        <div>    
        <h3>{props.name}</h3>
        </div>

        </article>
    )
}


export default Pokemon;