package com.rev.objects.concrete_inheritance;

public class Parent {
    String parentString;

    public Parent(String parentString){
        this.parentString = parentString;
    }

    public void parentMethod(){
        System.out.println("this came from the parentMethod inside the Parent class");
    }
}
