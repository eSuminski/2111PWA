package com.rev.objects.concrete_inheritance;

public class Parent {
    String parentString;

    public Parent(String parentString){
        // even though we are not explicitly calling it, the super() is being called first thing in this
        // constructor because the Parent class is implicitly inheriting the Object class
        this.parentString = parentString;
    }

    public void parentMethod(){
        System.out.println("this came from the parentMethod inside the Parent class");
    }
}
