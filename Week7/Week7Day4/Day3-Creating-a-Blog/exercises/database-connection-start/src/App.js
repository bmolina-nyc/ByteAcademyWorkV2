import React, { Component } from 'react';
import './App.css';
import Pokemon from './components/Pokemon/Pokemon'
import PokemonDetails from './components/Pokemon/PokemonDetails'
import axios from 'axios';

class App extends Component {
  
  state = {
    pokemon:[]
  }

  //api pokemon call
  componentDidMount(){
    // axios.get('https://pokeapi.co/api/v2/pokemon/?limit=5')
    axios.get('https://pokeapi.co/api/v2/pokemon/')
    .then(response => {
    const pokemonResults = response.data.results
    this.setState({pokemon: pokemonResults})
    })
  }

  selectedPokemon = (id) => {
    this.setState({
      selectedPokemonId: id
    })
  }


  render() {
    const pokemon = this.state.pokemon.map((pokeObject, idx)=>{
      return <Pokemon 
        key={idx+1}
        name={pokeObject.name}
        clicked={()=>this.selectedPokemon(idx+1)}
      />

    })

    return (
      <div className="App">
        <div>
        <section className="Pokemon">
          {pokemon}
        </section>
        <section>
          <PokemonDetails id={this.state.selectedPokemonId} />
        </section>
      </div>
    </div>
    );
  }
}

export default App;
