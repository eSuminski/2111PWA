package com.rev.methods;

public class MethodBasics {
    // to make an object do something you need to create methods.
    /*

    anatomy of a method:
    1. access modifier keyword (if any)
    2. non-access modifier keyword (if any)
    3. return type (void if nothing is returned)
    4. method name (use camelCase)
    5. parameters inside ()
    6. code inside {}

     */
    // this method has an access modifier and return type
    public void printToConsole() {
        System.out.println("this is a simple method that prints a message to the console");
    }

    // you can add parameters to your methods
    public void printUniqueMethodToConsole(String phrase) {
        System.out.println(phrase);
    }

    // it does not have to be just one
    public void doAddition(int num1, int num2) {
        System.out.println(num1 + num2);
    }

    // you use the "return" keyword to indicate what you are getting back from the method
    public String returnPhrase(String phrase) {
        return "your phrase is: " + phrase;
    }

    // you can mix and match your parameter types, but your return value MUST match what you declare
    public String returnAdditionAsString(String phrase, int num1, int num2) {
        // this method returns a string phrase that we enter pluse the addition of the two numbers concatonated on
        return phrase + (num1 + num2);
    }

    public boolean isThisTrue(int num) {
        if (num == 5) {
            return true;
        } else {
            return false;
        }
    }

    // java supports varargs (variable arguments) which are useful when you can't be sure how many
    // inputs your method is going to receive
    // make sure you only pass in the data type you indicate as the parameter

    public void varArgs(int... args) {
        for (int x = 0; x < args.length; x++) {
            System.out.println(args[x]);
        }
    }

    // fun fact: your main method expects a variable string argument: this is required for your main method to work
    // you could make your main method like this: main(String... args) but you can't make a varargs method
    // like this: varArgs(int[] args)
    public static void main(String[] args) {
        MethodBasics object1 = new MethodBasics();
        object1.printToConsole();
        System.out.println();
        object1.printUniqueMethodToConsole("this is my unique phrase that is required for the method");
        System.out.println();
        object1.doAddition(1, 2);
        System.out.println();
        System.out.println(object1.returnPhrase("this is the phrase I added"));
        System.out.println();
        System.out.println(object1.returnAdditionAsString("I am doing math: ", 1, 2));
        System.out.println();
        System.out.println(object1.isThisTrue(5));
        System.out.println();
        System.out.println(object1.isThisTrue(4));
        System.out.println();
        object1.varArgs(1, 2, 3, 4, 5);
    }
}