package com.rev.objects.concrete_inheritance;

public class Child extends Parent{
    String childString;

    public Child(String parentString, String childString){
        // we use the super keyword to pass any necessary arguments up into the parent constructor so that it can
        // handle creating any properties for our object that are from the Parent class
        super(parentString);
        this.childString = childString;
    }

    public static void main(String[] args) {
        Child child = new Child("this is the parent string", "this is the child string");
        // we now have access to the parent properties and methods in our child class
        System.out.println(child.parentString);
        System.out.println(child.childString);
        child.parentMethod();
    }
}
