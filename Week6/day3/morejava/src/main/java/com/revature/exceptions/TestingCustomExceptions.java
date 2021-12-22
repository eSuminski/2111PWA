package com.revature.exceptions;

public class TestingCustomExceptions {
    public static void main(String[] args) {
        // we are still able to throw our custom unchecked exception here without a try/catch block
        if (2>1){
            throw new CustomUncheckedException("I can throw this without a try/catch block catching it");
        }
        try{
            if (2>1){
                throw new CustomCheckedException("the application can not be built unless this is in a try catch block");
            }
        } catch (CustomCheckedException e){
            System.out.println(e.getMessage());
        }

//        duckingMethod(); this will prevent my application from being built unless I place it inside a try/catch block


    }

    public static void duckingMethod() throws CustomCheckedException{
        throw new CustomCheckedException("I don't need to have my checked exception inside a try catch block here");
    }
}
