# Day 3 - ES6: teamplateStrings, taggedTemplates, restSpreadOperations, additional JS methods, loops, iterables, promises, classes

## Topics covered: 
### 1) Classes

[Class Basics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- Classes are in fact "special functions", and just as you can define function expressions and function declarations, the class syntax has two components: class expressions and class declarations.
- One way to define a class is using a class declaration. To declare a class, you use the `class` keyword with the name of the class ("Rectangle" here).
```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```
- A class expression is another way to define a class. Class expressions can be named or unnamed. The name given to a named class expression is local to the class's body.(it can be retrieved through the class's (not an instance's) name property, though).
```javascript
// unnamed
let Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle"

// named
let Rectangle = class Rectangle2 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle2"
```

[constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#Constructor)
- The constructor method is a special method for creating and initializing an object created with a class. There can only be one special method with the name "constructor" in a class. A SyntaxError will be thrown if the class contains more than one occurrence of a constructor method.

[class methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#Prototype_methods)
- In this example, the calcArea is a class method for the class Rectangle 
```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.calcArea();
  }
  // Method
  calcArea() {
    return this.height * this.width;
  }
}

const square = new Rectangle(10, 10);

console.log(square.area); // 100
```

[static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#Static_methods)
- The static keyword defines a static method for a class. Static methods are called without instantiating their class and cannot be called through a class instance. Static methods are often used to create utility functions for an application.
```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.hypot(dx, dy);
  }
}

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);

console.log(Point.distance(p1, p2)); // 7.0710678118654755
```

[getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
-The get syntax binds an object property to a function that will be called when that property is looked up.
```javascript
let obj = {
  log: ['a', 'b', 'c'],
  get latest() {
    if (this.log.length == 0) {
      return undefined;
    }
    return this.log[this.log.length - 1];
  }
}

console.log(obj.latest);
// expected output: "c"
```

[setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
- The set syntax binds an object property to a function to be called when there is an attempt to set that property.
```javascript
let language = {
  set current(name) {
    this.log.push(name);
  },
  log: []
}

language.current = 'EN';
language.current = 'FA';

console.log(language.log);
// expected output: Array ["EN", "FA"]
```

[extending classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
[inheritance](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
- The extends keyword is used in class declarations or class expressions to create a class which is a child of another class.
- The child class will inherit the properties and methods of a parent class 
```javascript
class ChildClass extends ParentClass { ... }
```

[prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- JavaScript is often described as a prototype-based language — to provide inheritance, objects can have a prototype object, which acts as a template object that it inherits methods and properties from.
- An object's prototype object may also have a prototype object, which it inherits methods and properties from, and so on. 


### 2) Arrays

[.find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
- The find() method returns the value of the first element in the array that satisfies the provided testing function. Otherwise undefined is returned.
``` javascript
const array1 = [5, 12, 8, 130, 44];

const found = array1.find(function(element) {
  return element > 10;
});

console.log(found);
// expected output: 12
```

[.findIndex()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
- findIndex() is similar to find() except that the index of the searched value is returned instead of the actual value 

[.from()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
- The Array.from() method creates a new, shallow-copied Array instance from an array-like or iterable object.
```javascript
console.log(Array.from('foo'));
// expected output: Array ["f", "o", "o"]

console.log(Array.from([1, 2, 3], x => x + x));
// expected output: Array [2, 4, 6]
```

[.of()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of)
- The Array.of() method creates a new Array instance with a variable number of arguments, regardless of number or type of the arguments.
```javascript
Array.of(7);       // [7] 
Array.of(1, 2, 3); // [1, 2, 3]
```

### 3) Template Strings

[innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
- The Element property innerHTML gets or sets the HTML or XML markup contained within the element.
```javascript
const content = element.innerHTML;
element.innerHTML = htmlString;
```

[document / the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- The Document Object Model (DOM) connects web pages to scripts or programming languages. Usually that means JavaScript, although modelling HTML, SVG, or XML documents as objects is not part of the JavaScript language, as such.
- The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects. DOM methods allow programmatic access to the tree; with them you can change the document's structure, style, or content. Nodes can also have event handlers attached to them; once an event is triggered, the event handlers get executed.

[template strings with HTML](https://wesbos.com/template-strings-html/)

[functions within template strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#Tagged_templates)
- A more advanced form of template literals are tagged templates. Tags allow you to parse template literals with a function.
- The first argument of a tag function contains an array of string values. The remaining arguments are related to the expressions.
- In the end, your function can return your manipulated string (or it can return something completely different as described in the next example).

### 4) Tagged Templates 

[abbr tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
- The HTML Abbreviation element (<abbr>) represents an abbreviation or acronym; the optional title attribute can provide an expansion or description for the abbreviation. If present, title must contain this full description and nothing else.


[appendChild()](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
- The Node.appendChild() method adds a node to the end of the list of children of a specified parent node
- If the given child is a reference to an existing node in the document, appendChild() moves it from its current position to the new position
```javascript
// Create a new paragraph element, and append it to the end of the document body
let p = document.createElement("p");
document.body.appendChild(p);
```

### 5) Rest and Spread Operators

[spread operatior](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
- Spread syntax allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected.
```javascript
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];

console.log(sum(...numbers));
// expected output: 6
```

[rest operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- The rest parameter syntax allows us to represent an indefinite number of arguments as an array.
```javascript
function sum(...theArgs) {
  return theArgs.reduce((previous, current) => {
    return previous + current;
  });
}

console.log(sum(1, 2, 3));
// expected output: 6

console.log(sum(1, 2, 3, 4));
// expected output: 10
```

[slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
- The slice() method returns a shallow copy of a portion of an array into a new array object selected from begin to end (end not included). The original array will not be modified.
```javascript
const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

console.log(animals.slice(2));
// expected output: Array ["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
// expected output: Array ["camel", "duck"]

console.log(animals.slice(1, 5));
// expected output: Array ["bison", "camel", "duck", "elephant"]

```

### 6) Promises 
Use the code below as a reference for the following topics 
```javascript
  // Your promise will either resolve (succed) or reject(error) 
  const p = new Promise((resolve, reject) => {
    setTimeout(() => {
       const postPromise = fetch('url link')
      if (postPromise) {
          resolve(postPromise);
      } else {
      // make sure to pass the Error object so that you can actually find the correct line of the error message 
      reject(Error('Err something went wrong...'));
      }
    }, 1000);
  });

  // because we do not parse out the data as json - it gets passed as a response instead
  p
    .then(data => {
      console.log(data);
    })
    .catch(err => {
      console.error(err);
    });


  console.log(p);

```

[Promises basics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- Promises are intermediate topic in JS, so be patient as you read through the docs
- A Promise is an object representing the eventual completion or failure of an asynchronous operation.
- Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a function.
- Promises are often used when you are calling a JSON API or making an AJAX call 
- Promise constructor takes a function as an argument of the variable resolve and reject 

[Resolve](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
- The Promise.resolve() method returns a Promise object that is resolved with a given value. If the value is a promise, that promise is returned; if the value is a thenable (i.e. has a "then" method), the returned promise will "follow" that thenable, adopting its eventual state; otherwise the returned promise will be fulfilled with the value.

[Reject](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)
- The Promise.reject() method returns a Promise object that is rejected with a given reason.

[fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline, such as requests and responses. It also provides a global fetch() method that provides an easy, logical way to fetch resources asynchronously across the network.

[.then](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
- The then() method returns a Promise. It takes up to two arguments: callback functions for the success and failure cases of the Promise.

[.catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch



### Exercises
1) Array Cardio 2 - additional JS Methods
2) Jumping Letter - lets practice more CSS. Make the letters jump whenever you hover your mouse over it
3) API Exercise - create you own lookup ticker function for the JS version of terminal trader


