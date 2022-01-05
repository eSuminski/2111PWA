# Python Cheat Sheet
### Basic Python
- High level language
    - Python automates memory management for you
    - allows for faster development, but the tradeoff is optimization
- Dynamic language
    - Python handles type assignment for you
- Strongly typed
    - Python will not implicitly change variable data types after they are set
- Interpreted language
    - Python code is compiled and executed line by line
    - Usually slower than a "compiled" language, but it allows for more modular testing of your code
### Identifiers
identifiers are the names you give to the different parts of your code, like the variables, functions, classes, etc. Here are the best practices for naming conventions:
- Classes and Exceptions: PascalCase (no spaces, uppercase first letter for each unique word)
- Constants: SCREAMING_SNAKE_CASE (no spaces, all uppercase letters, underscore seperates unique words)
- Everything else: snake_case (no spaces, all lowercase letters, underscore seperates unique words) 

To create an identifier you simply have to use the assignment operator (=) and define what you want the identifier to reference. Example:
```python 
my_num = 1 
```
### Keywords
Python uses these keywords to provide functionality in your code. Do not use them as identifiers:
#### control flow
```Python
for # used if you want something to loop
in # use this when you want to reference something inside another element
while # use this when you want to loop for specified conidtion
match # use this when you want some input to be matched to code execution
case # used with the match keyword to determine the code execution
```
#### exceptions
```Python
try # this is used to start your try except block. Use this when you think something can go wrong
except # use this to handle things going wrong
finally # use this when you need something to happen whether your code executes successfully or not
raise # use this to raise an exception
```
#### importing
```Python
from # use this to specify where you are importing your code from
import # use this to import your code
as # you can set a reference to whatever it is you are importing
```
#### logical operators
```Python
is # use this when you want a True result when A and B reference the same memory location
is not # use this when you want a True result when A and B do not reference the same memory location
and # use this when you want to set up multiple trigger conditions
or # use this when you want to set up multiple optional trigger conditions
if # use this when you want code to run under specified conditions
elif # use this when you want code to run under conditions not covered by the if statement
else # use this to run code if your if and elif statements do not run
True # boolean indicating something is true
False # boolean indicating something is false
```
#### others
```Python
None # default function return value
pass # use this to ignore code
def # used to create functions
class # used to create classes
assert # used for testing to get a boolean result
break # used to escape a loop
```
### Operators
```Python
+ # addition
- # subtraction
* # multiplication
/ # division
** # power of
% # modulus
// # floor division
== # comparison operator (checks if A and B have the same value)
> # greater than
< # less than
>= # greater then or equal to
<= # less than or equal to
```