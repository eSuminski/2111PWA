package com.rev.acess_modifiers;

// this class is public: it can be accessed anywhere in our code
public class AcessModifiers {
    /*

    There are four access modifiers in Java:

    public
    protected
    default
    private

     */
    // available within the same package and in any classes that inherit from this one
    protected String myProtectedString = "this string is available for use within the same package " +
            "and in any classes that inherit this one";
    // available within the same package (any classes that inherit must be in same package to use directly)
    String myDefaultString = "this string is only available within this package. Any classes that inherit from this" +
            "class will not be able to access this string unless they are also located in this package";
    // only available directly for use within this class
    private String myPrivateString = "this string is only available within this class: it can not be accessed directly" +
            "in any other place";
}
