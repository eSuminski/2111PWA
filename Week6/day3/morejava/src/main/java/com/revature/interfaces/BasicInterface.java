package com.revature.interfaces;

// to create an interface you use the "interface" keyword instead of the "class" keyword
public interface BasicInterface {
    // all interface variables are public static final variables
    // this is true even if you don't declare the variable public static final
    String interfaceString = "this is my interface string";

    // interface methods are by default public abstract, so neither keyword is needed
    void myAbstractMethod();

    // default interface methods have a default implementation that can be overridden by any implementing classes
    default void myDefaultMethod(){
        System.out.println("this is the default implementation: it can be changed by any class that inherits it");
    }

    // static methods can only be called by referencing the interface itself
    static void myStaticMethod(){
        System.out.println("I can call this method via the interface: it can not be overridden");
    }
}
