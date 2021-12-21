package com.rev.control_flow;

public class ControlFlowPlayground {
    public static void main(String[] args) {
        // the most basic control flow option is the if statement: if the statement it is provided is true then it
        // will execute some code
        int x = 5; // if we change this value then the if block of code below will not run
        if (x == 5){
            System.out.println("x does indeed equal 5");
        }

        // you can also use else statements with your ifs: they will execute if the statement provided for the
        // if is false
        if (x == 6){
            System.out.println("x does indeed equal 5");
        } else {
            System.out.println("x does NOT equal 5");
        }

        // use else if when you want to check multiple conditions all together
        if (x == 7){
            System.out.println("x does indeed equal 7");
        // you can added extra checks with else if
        } else if (x == 8){
            System.out.println("x ACTUALLY equals 8");
        } else {
            System.out.println("x does not equal 7 or 8");
        }

        // you can use for loops to iterate through collections of data
        int[] nums = {1,2,3,4,5};
        for (int y = 0;y < nums.length;y++){
            System.out.println(nums[y]);
        }

        // if your are iterating through a collection that implements the iterable interface you can use an
        // enhanced for-loop to iterate through it
        for (int y : nums){
            System.out.println(y);
        }

        // use enhanced for-loops when you are working with collections that implement the iterable interface, but
        // you will still have use for the regular for loop

        for (String myString = "a"; myString.length() < 10; myString = myString + myString){
            System.out.println(myString);
        }

        // while loops are useful when you need code to repeat WHILE a condition is true
        int z = 0;
        while (z < 10){
            System.out.println(z);
            z++;
        }

        // you can also use a do-while loop: this loop will always run at least once, even if the while condition
        // is false
        do {
            System.out.println(z);
        } while (z < 10);

        // switch statements take a variable and executes code based upon the given value
        // unless you add break statements to the cases then any cases that fall after the case that is initially
        // run will also execute
        int a = 3;
        switch(a){
            // this is similar to if (a == 1)
            case 1:{
                System.out.println("variable a = 1");
                break;
            }
            case 2:{
                System.out.println("variable a = 2");
                break;
            }
            case 3:{
                System.out.println("variable a = 3");
                break;
            }
            case 4:{
                System.out.println("variable a = 4");
                break;
            }
            case 5:{
                System.out.println("variable a = 5");
                break;
            }
            default:{
                System.out.println("this will run if no other conditions are meet");
            }
        }

    }
}
