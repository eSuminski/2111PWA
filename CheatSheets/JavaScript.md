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
    - var (not recommended)
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
- logical operators (|, &, etc.)
    - these will convert types into booleans
- comparison operators (>, <, etc)
    - converts to numbers if it can to get a boolean value back

### Equality operators
- == is the loose equality operator
    - coerces types first
- === is the strict equality operator
    - does not coerce types
    - generally the better option