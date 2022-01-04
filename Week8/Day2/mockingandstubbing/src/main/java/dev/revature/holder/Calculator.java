package dev.revature.holder;

import dev.revature.injection.Maths;

public class Calculator {

    public Maths maths;

    public Calculator(Maths maths){
        this.maths = maths;
    }

    public String evenOdd(int num, int num2){
        int result = this.maths.division(num, num2);
        if (result%2 == 0){
            return "even";
        } else {
            return "odd";
        }
    }
}
