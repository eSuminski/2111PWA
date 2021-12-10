# JavaScript Cheat Sheet
### Basic JavaScript
- most common client-side scripting language
    - with node.js it can be used server-side
- high level
    - memory management is automated
    - garbage collection is handled for the developer
- multi-paradigm
    - can be written functionally
    - can be written using OOP design
- interpreted
    - line by line compilation and execution
- case sensitive
    - should seperate statemets with ;
- can place inside html via script tags
    - can reference it exeternally:
```html
<script src="./script.js"></script>
```
### Data Types
- string
- number
- bigInt
- boolean
- null
- undefined
- symbol (es6 datatype, not common)
### Scopes
- global
    - no key word
- function
    - var (not recommended because of hoisting)
- block
    - const
    - let
### Truthy Falsey
- falsey
    - empty string = false
    - undefined variable = false
    - null variable = false
    - Nan = false (always false)
    - 0 = false
- truthy
    - anything not above

### Type Coercion
- JavaScript is a loosely typed language: it will automatically try and coerce your data types when they do not match
- + operator
    - when used with a string your code will convert everything to a string and do string concatonation
- logical operators (||, &&, !)
    - these will convert types into booleans
- comparison operators (>, <, etc)
    - converts to numbers if it can to get a boolean value back
    - also happens with bitwise, arithmetic, and loose equality operators

### Equality operators
- == is the loose equality operator
    - coerces types first
- === is the strict equality operator
    - does not coerce types
    - generally the better option

### For Loops
```javascript
// for-of loops iterate over an array or array like object
let myArray = [1,2,3,4];
for (let number of myArray){
    console.log(number);
}

// for-in loops iterate through the keys of an object
let myObject = {key1:"value", key2:10};
for (let key in myObject){
    console.log(myObject[key]);
}

// can do a normal for loop as well

for (let i = 0; i < 10; i++){
    console.log(i);
}

```

## Control Flow
- if
- else
- for-in
- for-of
- while
- do-while
    - code will always run at least once, even if the while statement is false
```javascript
let x = 10;
do{
    console.log(x);
} while (x < 10)
```

### If
```javascript
let something = {}
if(something){
    console.log("because of truthy/falsey the something object is coerced into a true boolean")
}
```
### DOM Manipulation/Access
- textContent
    - used to return/set the text inside an element: this includes extra white space and special characters
    - innerText will not display extra white space or special characters, so textContent is recommended instead
- innerHTML
    - used to return/set text content and tags within an element
- cloneNode
    - used to clone an element
    - give it a boolean true argument and all child nodes will be copied as well