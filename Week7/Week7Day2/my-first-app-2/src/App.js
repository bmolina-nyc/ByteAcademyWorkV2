import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import Person from './components/Person';


class App extends Component {

  state = {
    persons: [
        {id: 'aa', name: 'Gabby', age: 27},
        {id: 'bb', name: 'Carter', age: 100},
        {id: 'cc', name: 'Kenso', age: 50},
        {id: 'dd', name: 'Greg', age: 40}
    ],
    otherState: 'some other value',
    showPersons: true 
}

switchNameHandler = (newName) => {
  this.setState({
      persons: [
          {name: newName, age: 27},
          {name: 'Carter Adams', age: 50},
          {name: 'Kenso Trabing', age: 99},
          {name: 'Greg Smith', age: 10000}
      ]
  })
}

nameChangedHandler = (event, id) => {
  const personIndex = this.state.persons.findIndex(person =>{
      return person.id === id
  });
  const person = {
    ...this.state.persons[personIndex]
  }
  person.name = event.target.value 
  const persons = [...this.state.persons]
  persons[personIndex] = person

  this.setState({persons: persons})
}

togglePersonsHandler = () => {
  this.setState({
    showPersons: this.state.showPersons === true ? false : true
  })
}

deletePersonsHandler = (personId) => {
  const persons = this.state.persons.filter( (el)=> {return el.id !== personId })
  // const persons = [...this.state.persons]
  // persons.splice(personIndex, 1)
  this.setState({persons: persons})
}

  render() {
    const style ={
      backgroundColor: 'white',
      font: 'inherit',
      border: '10px solid blue',
      padding: '8px',
      cursor: 'pointer'
  };

  let persons = null;
  if (this.state.showPersons){
    persons = (
      <div>
        {this.state.persons.map((person, index) => {
          return <Person 
          clicked={() => this.deletePersonsHandler(person.id)}
          name = {person.name}
          age =  {person.age}
          key =  {person.id}
          changed = {(event)=> this.nameChangedHandler(event, person.id)}
          />
        })}
      </div>
    )
  }

    return (
      <div className="App">
        {/* Here we will start by deleting the default entries */}
       
        <h1>Hi, I'm a React App </h1>
        <p> This is really working</p>
        <button 
        style={style}
        onClick={this.togglePersonsHandler}
        >
        Toggle Persons
        </button>
        {persons}   
      </div>
    );
  }
}

export default App;
