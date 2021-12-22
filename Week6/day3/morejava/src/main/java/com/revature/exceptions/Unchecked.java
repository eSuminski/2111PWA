package com.revature.exceptions;

public class Unchecked {
    public static void main(String[] args) {
        // we all know you can't divide by zero, but it doesn't mean someone won't try it
        // this will give us the ArithmeticException, which is an unchecked exception. This means
        // we do not need to catch it in a try/catch block, but if we don't the exception will kill our
        // application, so it is good practice to catch unchecked exceptions.
        System.out.println(10/0);
    }
}
