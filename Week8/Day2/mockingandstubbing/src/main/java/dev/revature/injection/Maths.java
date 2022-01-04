package dev.revature.injection;

public class Maths {

    public int division(int num, int num2){
        if (num == 1 & num2 == 1){
            throw new ArithmeticException("adding this to show mocking exception");
        } else{
            return num/num2;
        }

    }
}
