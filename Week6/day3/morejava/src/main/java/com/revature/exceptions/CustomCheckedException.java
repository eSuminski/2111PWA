package com.revature.exceptions;

// here we have created a custom CHECKED exception because we are extending the Exceptoin class
public class CustomCheckedException extends Exception{
    public CustomCheckedException(String message){
        super(message);
    }
}
