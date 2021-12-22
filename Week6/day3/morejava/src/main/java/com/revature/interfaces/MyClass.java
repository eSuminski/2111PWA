package com.revature.interfaces;

// if you implement multiple interfaces you separate them with commas
public class MyClass implements BasicInterface, AnotherInterface{
    public static void main(String[] args) {
        System.out.println(MyClass.interfaceString); // the variable is static by default
//        MyClass.interfaceString = "something new";// it is also final by default: trying this will break our program
        MyClass object = new MyClass();
        object.myAbstractMethod();
        object.myDefaultMethod();
        BasicInterface.myStaticMethod();
        System.out.println(MyClass.interfaceNum);
    }

    @Override
    public void myAbstractMethod() {
        System.out.println("I got this method from the interface I implement");
    }


    @Override
    public void myDefaultMethod() {
        System.out.println("this is my newly implemented default method");
    }
}
