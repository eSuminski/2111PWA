package com.revature.tests.holder;

import dev.revature.holder.Calculator;
import dev.revature.injection.Maths;
import org.mockito.Mockito;
import org.mockito.internal.verification.VerificationModeFactory;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class MockingAndStubbing {

    public static Maths maths;
    public static Calculator calculator;

    @BeforeClass
    public void setup(){
        maths = Mockito.mock(Maths.class);
        calculator = new Calculator(maths);
    }

    @Test
    public void controlReturnValueWithStubbing(){
        // this is an example of stubbing: we determine the result of the method with a given input
        //  this is very useful for creating unit tests for your service layer
        Mockito.when(maths.division(10,5)).thenReturn(3);
        String result = calculator.evenOdd(10,5);
        Assert.assertEquals(result,"odd");
    }

    @Test
    public void determineReturnValue(){
        // this is how you would actually want to set up your stub: return what you ACTUALLY expect back and check that
        // the logic of your service layer method works as intended
        Mockito.when(maths.division(10,5)).thenReturn(2);
        String result = calculator.evenOdd(10,5);
        Assert.assertEquals(result,"even");
    }

    @Test
    public void checkMethodCallAndInputs(){
        // this is an example of mocking: instead of predetermining the result of a method we are checking to make sure
        // that the path of execution is working as expected
        String result = calculator.evenOdd(20,5);
        Mockito.verify(maths).division(20,4);
    }

    @Test
    public void checkNumberOfMethodCalls(){
        // here we are checking to make sure our division method was called the correct number of times with the
        // correct inputs. This can be a useful test if you have a method that is called multiple times within another
        // method
        calculator.evenOdd(30,2);
        calculator.evenOdd(30,2);
        calculator.evenOdd(30,2);
        Mockito.verify(maths, VerificationModeFactory.times(3)).division(30,2);
    }

}
