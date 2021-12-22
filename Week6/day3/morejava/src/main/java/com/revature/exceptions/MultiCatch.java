package com.revature.exceptions;

import java.util.InputMismatchException;
import java.util.Scanner;

public class MultiCatch {
    public static void main(String[] args) {
        // the scanner will be closed even if an exception is thrown
        try(Scanner scanner = new Scanner(System.in)){
            System.out.print("Please enter a whole number: ");
            int num = scanner.nextInt();
            System.out.println("Please enter another whole number: ");
            int num2 = scanner.nextInt();
            System.out.println(num/num2);
        // this will run if we don't enter an int for either number
        } catch (InputMismatchException ime){
            System.out.println("Wrong input type! Please try again.");
        // this will run if we make the second number 0
        } catch (ArithmeticException ae){
            System.out.println("You can't divide by zero! Please try again");
        // this will run if we get any other exceptions. It is a catch all block that should only be placed after
        // any specific exceptions we wish to catch
        } catch (Exception e){
            System.out.println("Something unexpected happened!");
            e.printStackTrace();
        // any code in a finally block will exectute after your try/catch blocks, even if an exception is thrown
        } finally {
            System.out.println("this will always run, even if one of the exceptions above is thrown");
        }
    }
}
