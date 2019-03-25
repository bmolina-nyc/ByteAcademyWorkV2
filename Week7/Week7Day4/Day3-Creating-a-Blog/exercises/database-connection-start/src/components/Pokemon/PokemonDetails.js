import React, {Component} from 'react';
import axios from 'axios'

class PokemonDetails extends Component{

    state = {
        name: null,
        abilities: null,
        moves: null,
        image: null,
        id: null 
    }

    componentDidUpdate(){
        if (this.props.id){
            if(!this.state.name || this.state.id !== this.props.id)
            axios.get('https://pokeapi.co/api/v2/pokemon/' + this.props.id)
            .then(response => {
            const name = response.data['name']
            const abilities = response.data['abilities']
            const moves = response.data['moves'].slice(0,5)
            const image = response.data['sprites']['front_default']
            const id = this.props.id
            this.setState({name: name, abilities: abilities, moves: moves, image: image, id: id })
        })
      }
    }

    render(){
  
        if (this.state.abilities){
            var abilities = this.state.abilities.map ((el, idx) => {
                return <div key={idx}>{el['ability']['name'] + " "}</div>
            })
        }

        if (this.state.moves){
            var moves = this.state.moves.map(el => {
             return <div>{el['move']['name'] + " "}</div> 
            })
        }

        let pokemon = <p></p>   
        if (this.state.name){
            pokemon = (
                <div>
                    <h1>{this.state.name}</h1>
                    <img src={this.state.image} height="200px" width="200px"/>
                    <br></br>                    <br></br>

                    <article className="singlePokemon"> 
                       <p><b>Abilities:</b></p>
                        {abilities}
                    </article>
                   
                    <article className="singlePokemon">
                        <p><b>Top Moves:</b></p>
                        {moves}
                    </article>
                    
                </div>
            )
        }
        return pokemon
    }
}

export default PokemonDetails;