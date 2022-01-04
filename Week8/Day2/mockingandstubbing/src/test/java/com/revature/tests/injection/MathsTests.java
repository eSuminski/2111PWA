package com.revature.tests.injection;

import dev.revature.injection.Maths;
import org.testng.Assert;
import org.testng.annotations.Test;

public class MathsTests {
    public static Maths maths = new Maths();

    @Test
    public void checkDivision(){
        Assert.assertEquals(maths.division(10,5), 2);
    }

    @Test(expectedExceptions = ArithmeticException.class, expectedExceptionsMessageRegExp = "adding this to show mocking exception")
    public void checkException(){
        maths.division(1,1);
    }
}
