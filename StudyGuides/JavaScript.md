### Functions
```javascript
// basic function
function myFunction(){
    return "return value goes here"
}

// can have parameters
function withParams(num1, num2){
    return num1 + num2
}

// anonymous functions are similar to regular functions: they are assigned to a variable
let myFunc = function(){
    console.log("this works as a function")
}
myFunc(); // this will print the message to the console

// there are also self-invoking functions, or Immediately Invoked Function Expressions. They run after they are defined
(function(){
    console.log("runs right away");
})();

// callback functoins are passed as an argument
function callbackFunc(number){
    return number + 5
}

// higher order functions take in callback functions as an argument
function higherOrderFunction(num, callbackFunc){
    console.log(callbackFunc(num))
}
myFunc(3, callbackFunc) // will return 8, because higherOrderFunction passes the number 3 into the callbackFunc function which adds the number with 5. This also works with anonymous functions

// a closure is a function that can access variables and arguments in its outer function, even after a function return
function greeting(){
    let message = "Hello!"

    function sayHello(){
        console.log(message)
    }

    return sayHello()
}
greeting() // prints Hello! to the console

```

### Objects
Objects are key/value pairs in JavaScript, and the most common way of making them is by using object literal syntax
```javascript
let myObject = {key:"value"};

// both options below will print "value" to the console
console.log(myObject.key);
console.log(myObject["key"]);

// either option below will reasign the value of key
myObject.key = "new value";
myObject["key"] = "new value;
```

### Document Object Model
Web Browsers create a virtual version of your HTML page called the Document Object Model (DOM). You can think of it like a tree that branches out the more there is to your web page. Each element on the page is linked to another, either as a child (think a paragraph element inside a div container) or as a sibling (think two div containers next to each other). JavaScript allows you to manipulate the DOM and make web pages dynamic.

### Traversing the DOM
There are some common ways of traversing elements in the DOM:
```javascript
document.body.firstElementChild // returns the first child of the node, in this case the first child element of the body element
document.body.lastElementChild // returns the last child of the node, in this case the last child element of the body element
document.body.nextElementSibling // returns the next sibling element of the node
document.body.previousElementSibling // returns the previous sibling element of the node
document.body.parentElement // returns the parent element of the node
```
You can also be specific with how you select elements in the DOM
```javascript
document.getElementById("id goes here") // returns an element with the given ID
document.getElementsByClassName("class goes here") // returns an array like object with all the relevent elements inside
document.getElementsByName("name goes here") // returns an array like object with all the relevent elements inside
document.getElementsByTagName("tag goes here") // returns an array like object with all the relevent elements inside
```
Once you've made references to your elements in your JavaScript you can manipulate them
```javascript
document.createElement("tag goes here")// creates a brand new element
body.removeChild(element) // removes an element from the dom
body.appendChild(element)// makes an element the last child element of the node, in this case the body element
body.replaceChild(newElement, oldElement)// replaces a child element with a new one
body.insertBefore(newElement, element) // places a new element as a sibling before a currrent child element
```

### Event Listeners
you can assign event listeners to elements in the DOM: they will bubble by default (lowest level child event will proc first, then event propagation will work its way up the dom) but you can make events capture instead (parent node event will proc first, then event propagation will work its way down the dom)
```javascript
function action(){
    return "this text will be returned when the element is clicked"
}
element.addEventListener("click",action) // will bubble by default

element.addEventListener("click",action, true) // will capture instead of bubble

element.removeEventListener("click", action); // arguments must match a previously created event listener to remove it
```

### Async/Await
Because JavaScript is an event driven language there is a risk of blocking the event que (think latency issues, long loading time, things like this). You can avoid blocking the que by returing promise objects with your functions. Promises are empty objects that will eventually hold the data you want. You can use promises with functions that have the keyword async added to them: this allows you to write code that LOOKS  synchronous from the developers perspcetive, but in reality they are waiting for the data to populate their promise object.
```javascript
async function getData(){
    // you use await to pause execution till a promise is fulfilled or rejected (request fails)
    let data = await requestData()
}
```

### Fetch API
The Fetch API is a built in function for browsers that allows you to make http requests via your web pages.
```javascript
// notice the await used here: this request should be made via an async function
const response = await fetch("url", {method:"POST", body:"usually some JSON"})
// to access the response body you should assign it to a variable. In this case we are parsing a json, could be text, form data, or something else
const body = await response.json()
```
