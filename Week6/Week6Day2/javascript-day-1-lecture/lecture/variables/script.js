"use strict";

let number = 0
console.log(number)

number = 20;
console.log(number)

const name = 'Carter';
console.log(name)
name = 'Adams';

const person = {
  name: 'Eric Cartman',
  age: 13,
  food: 'Cheesy Poofs'
}

console.log(person)
console.log(person.age)
console.log(person['age'])

person.age = 20;
console.log(person.age)

const frozen_person = Object.freeze(person)

frozen_person.age = 33;
console.log(frozen_person.age = 20)

console.log(pizza)
const pizza = 'Deep Dish';
