package dev.revature.testngbasics;

import org.testng.Assert;
import org.testng.annotations.*;

public class BasicTesting {
    // a testng test is considered passing if it does not throw an exception

    // use this annotation to set up any parameters for your tests
    @BeforeClass
    void setup(){
        System.out.println("Anything in a BeforeClass method will run before any tests are run");
    }

    // use this if you need to do specific setup before tests
    @BeforeMethod
    void beforeEachTest(){
        System.out.println("Anything in a BeforeMethod method will run before EACH test");
    }

    // use if you need to reset data after all tests
    @AfterClass
    void tearDown(){
        System.out.println("I run after all the tests are finished");
    }

    // use if you need to reset data after a test
    @AfterMethod
    void afterEachTest(){
        System.out.println("I print after EACH test");
    }

    // use the priority property if you want to order your tests
    @Test(priority = 1)
    void testName(){
        //test code goes in here
        int x  = 5 + 5;
        // use the Assert class to check your results
        // the methods provided by the Assert class will throw exceptions if the assertion fails
        System.out.println("test 1");
        Assert.assertEquals(x, 10);
    }

    @Test(priority = 2)
    void showingOffOtherAnnotations(){
        // this test will pass because it does not throw an exception
        System.out.println("test 2");
    }

}
