package com.revature.scanners;

import java.util.Scanner;

public class Scanners {
    public static void main(String[] args) {
        // to get user input from the terminal you use the Scanner Class
        // make sure to pass System.in as the argument when you create your scanner
        Scanner scanner = new Scanner(System.in);
        // prompt the user for some input
        System.out.print("Please tell me your name: ");
        // then use the scanner.nextLine() to get their input and assign it to a variable
        String name = scanner.nextLine();
        // you now can use the user's input in your code
        System.out.println("Hello " + name + "!");
        System.out.print("Give me a number please: ");
        // we can indicate that we are expecting an int, code will throw an InputMismatchException if we give the
        // wrong input type
        int num = scanner.nextInt();
        System.out.println("You chose the number " + num);
        // make sure to close the scanner ONLY when you are absolutely done with it
        // your will get an exception if you try and reopen a scanner
        scanner.close();
    }
}
