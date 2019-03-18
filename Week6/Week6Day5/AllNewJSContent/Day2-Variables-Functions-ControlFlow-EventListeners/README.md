# DAY 2 - ES6: Variables, Functions, Control Flow, Event Listeners

## Topics covered: 
### 1) Variables

[`let` vs. `const` - mutable vs. immutable variables](https://wesbos.com/let-vs-const/)

[mutability of objects saved as `const` variables](https://jack.ofspades.com/es6-const-not-immutable/index.html)

[Object.freeze()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
- The Object.freeze() method freezes an object. A frozen object can no longer be changed; freezing an object prevents new properties from being added to it, existing properties from being removed, prevents changing the enumerability, configurability, or writability of existing properties, and prevents the values of existing properties from being changed.

[Temporal Dead Zone](https://stackoverflow.com/questions/33198849/what-is-the-temporal-dead-zone)
- Always make sure to declare your variables before using them, otherwise, you will run into an error and hit the temporal dead zone. 

[console.log()](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)
- There are many uses of console. The most common is `console.log()`, however, other common uses include `console.table()` and `console.alert()`

### 2) Functions

[Logical operators && and ||](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators)
- `&&` is the logical operator for 'and' while `||` is the logical operator for 'or' 

[Ternary Operators for shortened if/else statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
- The ternary operator is the shortcut for creating if statements
- In this example, `isMember` is the variable we are checking, the statement after the `?` is the return value of the condition if true, while the statement after `:` is the return value of the condition if false 
```javascript
function getFee(isMember) {
  return (isMember ? "$2.00" : "$10.00");
}

console.log(getFee(true));
// expected output: "$2.00"

console.log(getFee(false));
// expected output: "$10.00"

console.log(getFee(1));
// expected output: "$2.00"
```

[Template Strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
- Below is an example of how to create template strings 
```javascript
const name = 'Snickers';
const age = 2;
const sentence = `My dog ${name} is ${age * 7} years old.'`;
console.log(sentence);
// The expected output would be 'My dog Snickers is 14 years old.'
```

[switch statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
- The switch statement evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case, as well as statements in cases that follow the matching case.
```javascript
let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}
```


[JS functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
- Here is the default way of creating a function 
```javascript
function multiply(x, y) {
   return x * y;
} 
```
- An arrow function expression is a syntactically compact alternative to a regular function expression, although without its own bindings to the this, arguments, super, or new.target keywords.
- Arrow function expressions are ill suited as methods, and they cannot be used as constructors.
```javascript
    // Now lets look at arrow functions with some built-in JS methods 
    const ages = [23,62,45,234,2,62,234,62,34];

    // Now console.log the ages which are greater than 62 - we will use the method 
    // .filter() which creates a new array from an existing one 
    // this basically means that if age is greater than 60, then add it to the old array 
    const old = ages.filter(age => age >= 60);
    console.log('The ages above 60 are: ',old);
```
- Arrow function can either have a 'concise' body or the the usual block body. In a concise body, only an expression is specified, which becomes the implicit return value. You don't need to use a return statement 
```javascript
let func = x => x * x;                  
// concise body syntax, implied "return"

let func = (x, y) => { return x + y; }; 
// with block body, explicit "return" needed
```

[array methods .map() and .filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- There are numerous built-in JS methods, two of the most frequently used ones are .map() and .filter()
- .map() allows the user to create a new array with the results of calling a provided function on every element in the calling array
```javascript
const array1 = [1, 4, 9, 16];

// pass a function to map
const map1 = array1.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]
```
- While filter() creates a new array with all elements that pass the test implemented by the provided function
```javascript
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```

### 3) Iterables and Loops

[Control flow](https://developer.mozilla.org/en-US/docs/Glossary/Control_flow)

[Loops and iterations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)

[if, else if, else conditional statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- Below are the common structures for creating conditional statements
```javascript
function testNum(a) {
  if (a > 0) {
    return "positive";
  } else {
    return "NOT positive";
  }
}

console.log(testNum(-5));
// expected output: "NOT positive"
```

[for-of-loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
-The `for...of` statement creates a loop iterating over iterable objects, including: built-in String, Array, Array-like objects (e.g., arguments or NodeList), TypedArray, Map, Set, and user-defined iterables
```javascript
let iterable = [10, 20, 30];

for (let value of iterable) {
  value += 1;
  console.log(value);
}

// Output:
// 11
// 21
// 31
```

[for-in-loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

```javascript
const obj = {a: 1, b: 2, c: 3};
    
for (const prop in obj) {
  console.log(`obj.${prop} = ${obj[prop]}`);
}

// Output:
// "obj.a = 1"
// "obj.b = 2"
// "obj.c = 3"
```

### 4) Event Listeners / getElementById

[document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- The Document method querySelector() returns the first Element within the document that matches the specified selector, or group of selectors.
- In the example below, in this example, the first element in the document with the class "myclass" is returned
```javascript
const el = document.querySelector(".myclass");
```

[addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) 
- The EventTarget method addEventListener() sets up a function that will be called whenever the specified event is delivered to the target.
- addEventListener() works by adding a function or an object that implements EventListener to the list of event listeners for the specified event type on the EventTarget on which it's called.
- The example below demonstrates how to use addEventListener() to watch for mouse clicks on an element

```HTML
<table id="outside">
  <tr><td id="t1">one</td></tr>
  <tr><td id="t2">two</td></tr>
</table>
```
```javascript
// Function to change the content of t2
function modifyText() {
  const t2 = document.getElementById("t2");
  if (t2.firstChild.nodeValue == "three") {
    t2.firstChild.nodeValue = "two";
  } else {
    t2.firstChild.nodeValue = "three";
  }
}

// Add event listener to table
const el = document.getElementById("outside");
el.addEventListener("click", modifyText, false);
```

['this' as a DOM event handler](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this#As_a_DOM_event_handler)
- In most cases, the value of this is determined by how a function is called. It can't be set by assignment during execution, and it may be different each time the function is called
- When a function is used as an event handler, its `this` is set to the element the event fired from 
```javascript
// When called as a listener, turns the related element blue
function bluify(e) {
  // Always true
  console.log(this === e.currentTarget); 
  // true when currentTarget and target are the same object
  console.log(this === e.target);
  this.style.backgroundColor = '#A5D9F3';
}

// Get a list of every element in the document
const elements = document.getElementsByTagName('*');

// Add bluify as a click listener so when the
// element is clicked on, it turns blue
for (let i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', bluify, false);
}
```

[this.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) 
- Using classList is a convenient alternative to accessing an element's list of classes as a space-delimited string via element.className.
```javascript
const div = document.createElement('div');
div.className = 'foo';

// our starting state: <div class="foo"></div>
console.log(div.outerHTML);

// use the classList API to remove and add classes
div.classList.remove("foo");
div.classList.add("anotherclass");

// <div class="anotherclass"></div>
console.log(div.outerHTML);
```

[SetTimeOut](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- The setTimeout() method sets a timer which executes a function or specified piece of code once the timer expires.
- The following example sets up two simple buttons in a web page and hooks them to the setTimeout() and clearTimeout() routines. Pressing the first button will set a timeout which calls an alert dialog after two seconds and stores the timeout id for use by clearTimeout(). You may optionally cancel this timeout by pressing on the second button.
```HTML
<p>Live Example</p>
<button onclick="delayedAlert();">Show an alert box after two seconds</button>
<p></p>
<button onclick="clearAlert();">Cancel alert before it happens</button>
```
```javascript
let timeoutID;

function delayedAlert() {
  timeoutID = window.setTimeout(window.alert, 2000, 'That was really slow!');
}

function clearAlert() {
  window.clearTimeout(timeoutID);
}
```
[toggle method on classList](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle ) 
- The toggle() method of the DOMTokenList interface removes a given token from the list and returns false. If token doesn't exist it's added and the function returns true.


### 5) Webpack

[Why use Webpack?](https://blog.andrewray.me/webpack-when-to-use-and-why/)

[Installation](https://webpack.js.org/guides/installation)

[Getting Started](https://webpack.js.org/guides/getting-started/)

## Exercises
1) Rock - Paper - Scissors -> here you will create a basic game using the console
2) Basic calculator -> Be able to create a basic calculator which allows you to input 2 numbers and either multiply or divide them
3) Array Cardio - additional JS methods 
4) Above-and-Beyond - Exercises which are important to know, but not important for class lecture
5) Webpack build - Build a webpack application with the eventListener.html file as the main component. Make sure to minify the JS file 