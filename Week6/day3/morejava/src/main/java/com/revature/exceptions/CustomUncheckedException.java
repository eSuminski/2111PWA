package com.revature.exceptions;

// to make an UNCHECKD exception we extend the RuntimeException class
public class CustomUncheckedException extends RuntimeException{
    public CustomUncheckedException (String message){
        super(message);
    }
}
