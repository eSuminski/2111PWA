## Java Introduction
- high level
    - automatic memory management (no developer pointers, garbage collection handled for you)
- compiled
    - source code is all compiled together and then it can be run
- statically typed
    - must declare variable types
- strongly typed
    - can not coerce data types
- OOP
    - makes use of classes and objects
- Write Once, Run Anywhere
    - Anyone with a JRE and JVM can run a java app
- rich open source community
    - vast ammount of libraries you can add to your program
## class/object
|class|object|
|-----|------|
|declared using class keyword| declared using new keyword|
|declared once|declared as many times as needed|
|no memory allocated when created|memory allocated when created|
|blueprint for creating objects|instatiated class|
## jdk, jre, jvm
- JVM
    - the jvm takes compiled java code and runs it. if a computer has a jvm it can run java code
- JRE
    - the jre contains the runtime libraries necessary for a java app to run, and it houses the jvm too
- JDK
    - the jdk contains developer tools (compiler, debuger, documentation tools, etc.) that allow for the creation of java apps
## Pillars of Object Oriented Programming
- Abstraction
    - you don't need to know why code works to be able to use it
- Polymorphism
    - objects can behave differently in different contexts
        - Overriding and Overloading are clear examples
        - Overriding happens when you take method from a parent and change its implementation in a child class
        - Overloading is where you have a method with the same name but different parameters that all do different things
- Inheritance
    - classes can acquire behaviors(methods) and attributes(fields) other than those defined in their class
        - child class can inherit variables and methods from parent
- Encapsulation
    - classes can protect their behaviors and attributes by making them private and designating specific means of interacting with their content
    - this provides a level of protection for the class: it prevents unintentional interaction with class data
## Abstract Class vs Interface
|Abstract|Interface|
|--------|---------|
|class can't be instantiated|contract can't be instantiated|
|instance variable/access modifiers|public static final variables|
|concrete methods allowed|abstract, default, and static methods|
|can only inherit one class|can implement multiple interfaces|
## Operators
```java
+ // addition
- // subtraction
/ // division
* // multiplication
% // modulus (the remainder in division)
++ // increase value by 1
-- // decrease value by 2

// comparison operators return a True or False value

== // equal to
!= // not equal to
> // greater than
< // less than
>= // greater or equal to
<= // less than or equal to

// logical operators are used further facilitate the comparison operators

&& // logical and returns true of both statements are true
|| // logical or returns true if one of the statements is true
! // not operator reverses the desired outcome: will return false if the expression is true, and vice versa
```
## Variable Scopes
1. Class/static scope
    - available to all instances of the class by invoking the class itself
    - the static keyword makes a variable class scope
    - class scope methods/variables can not interact with instance variables/methods
2. Instance/object scope
    - available to the instance of an object
    - "this" keword is used to interact with an instance variable
    - instace variables do not cross objects: they are unique per object
3. Method scope
    - available within the method it is instantiated in
    - the variable no longer exists after the method is finished, so it can not be used outside the method
4. Block scope
    - available within the {} it is instantated in
    - usually your controlflow statements
## access modifiers
|modifier|access|
|-------|-------|
|public|anywhere|
|protected|within same package and sub-classes|
|default (no keyword)|within same package|
|private|within same class|
## Non-Access Modifiers
|modifier|effect|
|--------|------|
|abstract|can't be instantiated (class) or must be implemented (method)|
|static| ties properties and behaviors to the class|
|final| final classes can't be extended, variables can't be changed, methods can't be overridden|
|synchronized|helps prevent deadlock in threading|
|transient| make a variable non-serializable|
## stack & heap
- the heap is where objects are stored in memory (and the string pool)
- the stack is where local variables references and method invocations are stored
    - a new stack frame is created for each method invocation
## Primitive Types
|type|size|