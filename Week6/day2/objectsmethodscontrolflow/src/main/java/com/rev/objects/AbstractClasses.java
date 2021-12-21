package com.rev.objects;

// to make a class abstract add the non access modifier keyword "abstract" to the class declaration
public abstract class AbstractClasses {
    /*
    Java supports abstract classes: these are classes that cannot in themselves be instantiated (can't use the new
    keyword with them). They are useful when you need to reuse code in multiple locations and when you need to have
    similar methods with different implementations in different classes. This is part of something called polymorphism.
     */

    // abstract classes can have properties (variable) that can be inherited by other classes
    public String abstractVariable;
    public static int abstractNumber = 5;

    // to make a method abstract you add the non access modifier keyword "abstract" to it
    public abstract void speak();

    // abstract classes can also have concrete methods
    public void printMessage(){
        System.out.println("this is available to all classes that inherit from this abstract class");
    }

    // static (or class) methods are those that are called by the Class itself, not any instantiated objects
    public static void classMethod(){
        System.out.println("I can print this message only by utilizing the class: not the object");
    }

    // you need static methods to access static variables
    public static void seeAbstractNumber(){
        System.out.println("the static property called abstractNumber has the value: " + abstractNumber);
    }
}
