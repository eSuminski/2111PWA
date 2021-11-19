# Python Review
## What is Python
1. high level programming language
    - it has automatic memory management
        - example: garbage collection is automated
        - example: developers don't directly work with pointers
2. Dynamic programming language
    - developers do not declare variable types: the type is assigned automatically
        - developers can use type annotations, but these have no effect on the code itself. They are there to help the developer better read their code
3. Strongly typed language
    - Python will not implicitly coerce variables into new types
        - 10 + "hello" will cause an exception in your code
4. Interpreted language
    - Python code is compiled and executed line by line, not all at once
        - this is also called Just In Time Compilation

## Python Scopes
Python uses LEGB scoping:
1. Local
2. Enclosing
3. Global
4. built_in
```python
# built-in
id()
str()
len()

# if no enclosing variable is found it checks the global namespace for a variable
my_variable = "my global variable"

if True:
    # if no local variable is found it looks for an enclosing variable
    my_variable = "my enclosing variable"
    if True:
        # Python looks for a global variable first
        my_variable = "my local variable"
        print(my_variable)
```

## Strings
- Strings are immutable.
- Strings are created by doing x = "some string"
    - also valid: x = 'some string' OR x = """some string"""
        - avoid using triple double quotes for strings, save them for things like comments in your code
- String slicing "Hello"[2:5:-1]

## Functions
functions are reusable blocks of code. Be mindful that dynamic type assignment can sometimes create unexpected outcomes for your functions.
1. use the def keyword to indicate you are creating a function
2. give your function a name
3. declare any parameters
4. add a colon to the end
5. write the code for your function
```python
def my_function(parameter):
    return parameter + 1
```
functions can also take variable arguments (*args) and key word arguments (**kwargs)
- var args are useful when you don't know how many arguments are going to be supplied to the function
- key word arguments are useful for assigning key values to arguments
```python
# function with var args
def my_var_args_function(*args):
    for element in args:
        print(element)

my_var_args_function(1,2,3,4) # will print each element one by one

# function with key word argument
def my_kwarg_function(**kwargs):
    print(["name"])

my_kwarg_function(name="Sally") # will print Sally
```

## Classes and Objects
Everything in Python is an Object: there are no primitives
- Classes are blue prints for creating objects
- Objects have state (variables) and behaviors (methods)
    - function and method = the same thing, semantic term
    - usually, functions are called methods when attached to a class
    - methods take self as their first parameter
```python
class Person:

    class_variable = "class variables are shared across all objects"

    # the init dunder method is used to set an objects' state when it is created
    # similar to a constructor in java
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# this creates a person object with the name timmy and the age 30
my_person = Person("timmy", 30)
```
- Classes can inherit state and behavior from other Classes
```python
class ParentClass:
    def __init__(self, parent_variable):
        self.parent_variable = parent_variable

class ChildClass(ParentClass):
    def __init__(self, parent_variable, child_variable):
        # super() is a reference to the parent class
        super().__init__(parent_variable)
        self.child_variable = child_variable
```
- classes can be made abstract
    - useful when you need to reimplement code in multiple places

```python
from abc import ABC, abstractmethod
class Speech(ABC):
    
    # this tells python the method needs to be implemented by any inheriting classes
    @abstractmethod
    def speak(self):
        pass

class Adult(Speech):

    # this method needs to be defined in the child class
    def speak(self):
        return "I can speak like an adult"

class Baby(Speech):

    # this method needs to be defined in the child class
    def speak(self):
        return "crying noises"
```
- Python supports multiple inheritance
```python
class A:
    def __init__(self, a_variable):
        self.a_variable = a_variable

class B:
    def __init__(self, b_variable):
        self.b_variable = b_variablee

class C(A,B):
    def __init__(self, a_variable, b_variable, c_variable):
        A.__init__(self, a_variable)
        B.__init__(self, b_variable)
        self.c_variable = c_variable
```
- Classes can have class methods and static methods
    - class methods can interact with class variables but not object variables (no self passed into method)
    - static methods can not interact with class or object variables. Used for utility purposes
```python
class MyClass:
    class_variable = 7

    @classmethod
    def check_class_variable(cls):
        return MyClass.class_variable
    
    @staticmethod
    def utility():
        return "use these when you want to add utility to a class"
```
- classes have access to dunder methods (double underline methods, or magic methods)
- these are methods that you as a developer are encouraged to reimplement for your own purposes
    - they are methods that help determine how your objects react to common operations
```python
class MyClass:
    def __init__(self):
        print("You can execute code when an object of this class is created")
    
    def __str__(self):
        return "reimplementing this method will determine what is returned when you try and print or call str() on this object"
# this list is not exhaustive
```

### Collections
Python's most common data structures for containing objects are lists, sets, tuples, and dictionaries
|Collection|Mutable|Duplicates|Indexable|Formatting|
|----------|-------|----------|---------|----------|
|list      |Yes    |Yes       |Yes      |my_list = []|
|Set       |Yes    |No        |No       |my_set = {}|
|Tuples    |No     |Yes       |Yes      |my_tuple = ()|
|Dictionary|Yes    |No (keys) |version  |my_dictionary = {key:value}|
#### Lists
- mutable
- allows duplicates
- maintains order of entry
- indexable (my_list[2] returns the element in index position two of the list)
#### Sets
- mutable
- does not allow duplicates
- does not maintain order of entry
- not indexable
#### Tuples
- immutable
- allows duplicates
- indexable (my_tuple[2] returns the element in index position two of the tuple)
#### Dictionary
- mutable
- holds key:value pairs
- does not allow duplicate keys
- allows duplicate values

## Exceptions
Exceptions are raised when code does not execute as intended. They are objects that are created to contain information about what went wrong. Some built-in exceptions to remember:

- Exception
    - the parent class of all exceptions in Python
- NameError
    - occurs when you reference a variable that does not exist
- LookupError
    - parent class of KeyError and OutOfBoundsError
- TypeError
    - Something of the wrong type is being used
- ValueError
    - Right type but the value is inappropriate

- You can create custom errors for your application
```python
class CustomError(Exception):
    # add a message variable so you can deliver custom messages when the exception is raised
    def __init__(self, message):
        self.message = message
```
- Use try/except blocks when you think your code might fail
```python
try:
    print(variable_that_does_not_exist)
except NameError:
    return "you referenced a variable that does not exist"
```
- you can use the raise key word to force an exception
```python
try:
    if True:
        raise CustomException("message goes here")
# you can create a reference to the exception
except CustomException as e:
    return str(e) # this returns the message we created
```

### Importing
You can import modules (files) and packages (folders that hold modules) using the from and import key words
```python
from package import module
from another_package.another_module import Class

module.function()

Class.class_method()
```

### Pip, PyPi, Venv
pip is a package managment software that comes with a Python download from the main Python website. It can download packages from the Python package repository PyPi. If you use pip to download a package it will install it globally on your computer by default. To prevent an overabundance of packages on your computer, you can create a virtual enviornment (venv) to store packages in that is unique to the project you are working on. This allows for easier management of packages.

### Test Driven Development
Test Driven Development (TDD) is a design philosophy in which tests direct your development.
1. Create an interface (Abstract class in Python)
    - decide what functions are needed, and what their parameters should be
2. Create tests for the interface
3. Implement the interface in a way that it passes all your tests
4. Repeat and refine as needed

### Pytest
A testing framework for Python that works well for TDD. 
1. run the command pip install pytest
2. create a module for your tests
3. create an object in your code that you will be testing
4. write test functions for that object
    - make sure to start their names with "test" (test_....)
5. run the command pytest path\to\module\with\tests.py to run your tests
    - can instead run the command on the package with multiple modules of tests to run all of them

A few notes about tests:
- If you create a test without using an assert key word the test will pass if it does not raise an exception
- the assert keyword checks a logical statement: if the result is false the test raises an exception

### Flask
Still need to implement

### HTTP & JSON
Still need to implement

### Postman
still need to implement