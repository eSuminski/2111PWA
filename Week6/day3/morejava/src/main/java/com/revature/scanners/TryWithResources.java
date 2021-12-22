package com.revature.scanners;

import java.util.InputMismatchException;
import java.util.Scanner;

public class TryWithResources {
    public static void main(String[] args) {
        // this is the old way of using scanners
//        Scanner scanner = new Scanner(System.in);
//        scanner.close();
        // any class that implements the AutoCloseable interface can be initialized inside a try block and it will
        // auto close itself when the execution of the block is finished
        // try with resource blocks do NOT need a catch or finally block of code, but if something can go wrong
        // it is good practice to include them anyways
        try(Scanner scanner = new Scanner(System.in)){
            System.out.print("Please tell me your name: ");
            String name = scanner.nextLine();
            System.out.println("Hello " + name + "!");
            System.out.println("What is your favorite number?: ");
            int num = scanner.nextInt();
            System.out.println("I like the number " + num + " as well!");
            // notice we don't have to manually close the scanner: it is automatically done for us
        // if we try entering something other than an int on line 18 then we will get this exception
        } catch (InputMismatchException e){
            System.out.println("Something went wrong!");
        }
    }
}
