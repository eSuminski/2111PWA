/*
always make sure to leave the package declaration at the top of your class filed:
you don't technically need it, but you will quickly run into problems if you have more
than one class
*/
package com.suminski.classroom;


/* 
the line of code below is the class declaration: this indicates that we have a class that will be working as a blueprint 
(potentially) for instantiating objects to run our code. There are a few things you need to declare a class:

public: this is the access modifier, which tells your code where the class can and can not be accessed
class: this is the keyword that tells Java you are creating a class
MyFirstClass: this is the name of the class
notice that everything associated with the class is inside of curly braces
 */
public class MyFirstClass {
    /*
    All functions in Java are tied to classes or interfaces: there are no loose functions
    like in Python. The anatomy of creating a method is a little more complex than a class:
    
    public: same as above, this indicates where the function can be used
    static: this is a non-access-modifier keyword, which in this case means the method can be
    called without instantiation object of the class
    void: this is the return type of the method. Can be int, String, etc. You simply have to declare the return type
    main: this is the name of the method: the main method is what you call the entry point for your app
    (String[] args): the parameters of the method go inside (). For the main method you NEED String[] args
    make sure your method is encased in {}
    */
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
