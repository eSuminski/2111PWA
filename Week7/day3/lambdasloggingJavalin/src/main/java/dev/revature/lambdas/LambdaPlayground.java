package dev.revature.lambdas;

public class LambdaPlayground {
    public static void main(String[] args) {
        // this will make the mathematics lambda add 5 to the number we provide as an argument when addFive.mathematics is called
        MyFunctionalInterface addFive = num -> num + 5;
        System.out.println(addFive.mathematics(6));
        // this will make the mathematics lambda subtract 5 from the number we provide as an argument when minusFive.mathematics is called
        MyFunctionalInterface minusFive = num -> num - 5;
        System.out.println(minusFive.mathematics(6));
        // use {} when you have a multi-line lambda. make sure to add a ; at the end of the {}
        MyFunctionalInterface multipleLinesOfCode = num -> {
            num = num + 5;
            num = 4;
            return num;
        };
        System.out.println(multipleLinesOfCode.mathematics(5));
    }

    // lambda creation steps
    // 1. create functional interface (see MyFunctionalInterface)
    // 2. give your lambda function a name, return type, and parameters in your functional interface
    // 3. in your main (or wherever you need to call your lambda) create a variable that defines the lambda logic
    // 4. call your lambda with that variable
}
