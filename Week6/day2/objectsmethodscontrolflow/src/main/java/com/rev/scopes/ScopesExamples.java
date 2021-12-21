package com.rev.scopes;

public class ScopesExamples {
    /*
    There are four scopes in Java:

    Class/Static (variables and methods are accessed via the class)
    Instance/Object ( variables and methods are accessed via the object)
    Method (available within the method it is initialized in)
    Block (available within the local block of code it is initialized in)

     */
    static String myStaticScopeString; // this is part of the static/class scope
    String myInstanceScopeString; // this is part of the instance/object scope (accessed via the "this" keyword)

    public static void myStaticMethod(){
        String phrase = "this is a method scope string, only available within this method"; // this string is in the method scope
        for (int x = 0; x < 1; x++){ // the x variable is part of the block scope: it will no longer be available after this loop
            System.out.println("the x variable I created for this loop is part of the block scope");
        }
    }
}
