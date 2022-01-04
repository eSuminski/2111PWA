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
}
