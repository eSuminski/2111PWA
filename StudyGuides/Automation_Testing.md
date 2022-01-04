# Automation Testing
## Test Suite vs Test Case
- Test Suite: a collection of tests
- Test Case: a single test
## Requirements Traceablity Matrix
This is a document that provides detailed information about what is being tested, how it was tested, its testing status, and who is doing the testing.
![requirements traceability matrix](requirement_traceability_matrix_example.png)
## TestNG data provider
testNG has a built in report generation system you can leverage when running your tests, and it requires very minimal setup to access. The easy way to do this in intellij is to edit the run configuration
1. go to edit configuration
2. navigate to the testNG section in the leftmost panel
3. go to the listeners tab in the configuration menu
4. check the "use default listeners" box
5. click apply and ok

Now when you run your test suite (assuming you did this for the whole suite, not just a class or two) you will get an html generated report. Alternatively, you can create a testng.xml file and configure it to run your tests.

1. create a file called testng.xml in the root folder
2. add the following lines to the file:
```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
```
3. next add your test suites to the xml
```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
<suite name = "Test Suite name">

</suite>
<!-- you can have multiple suites in a file -->
```
4. next add your different tests to the suites
```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
<suite name = "Test Suite name">
    <test name = "Functionality being tested">
        
    </test>
</suite>
```
5. finally, add whatever classes hold the actual tests
```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
<suite name = "Test Suite name">
    <test name = "Functionality being tested">
        <classes>
            <class name = "dev.suminski.tests.BasicTests" />
        </classes>
    </test>
</suite>
```
6. you can then set up your configuration to "run" the xml file, which will prompt testNG to run the tests you specified and codify their results in its generated reports (as long as you turn on the basic listener)
## Mockito for Java (Stubbing)
There may come a point while testing where it becomes tedious to constantly ping your database for tests, or you want to run unit tests on the second or third layer of your application (the service or controler layer). You can mock your tests to achieve this. Mockito is a framework that allows you to do this with Java.
1. first add the necessary dependencies to your pom.xml (you will need to grab the testNG compatable version of Mockito if using testNG)
```xml
        <!-- https://mvnrepository.com/artifact/org.testng/testng -->
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>7.4.0</version>
            <scope>test</scope>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.mockito/mockito-testng -->
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-testng</artifactId>
            <version>0.4.13</version>
            <scope>test</scope>
        </dependency>
```
2. You will then need your methods you are testing. for this example I am using a simple math function inside a class that is injected into a calculator class
```java
public class Mathy {
    public int mathematics(int num){
        return num / 2;
    }
}

public class Calculator {
    
    public Mathy mathy;
    
    public Calculator (Mathy mathy){
        this.mathy = mathy;
    }

    public String evenOdd(int num){
        int result = mathy.mathematics(num);
        if (result % 2 == 0){
            return "even";
        } else {
            return "odd";
        }
    }
}
```
3. once your classes and methods are set you need to create a test class. Create the two classes but set them to null at the start
```java
public class MockingTests {
    public Mathy mathy;
    public Calculator calculator;
}
```
4. Use the @BeforeAll annotation to create a setup method. Inside this method you are going to initialize the Mathy class as a Mockito object and pass in the Mathy class as an argument. This will allow you to mock the data you give and receive from the class
```java
@BeforeAll
public static void setup(){

    // because I am mocking the mathy class I instantiate it as a mock class
    mathy = Mockito.mock(Mathy.class);
    // I can then inject the mocked class and it works
    calculator = new Calculator(mathy);

}
```
5. You can now write your tests for the calculator method we are testing, but instead of having to pass in real values you can use Mockito to determine what goes into the method and what comes out
```java
@Test
public void mockReturnControl(){
    // look how I can control the return value here:
    // normally I would mock the value returned from a database, or something else that it is
    // impractical to constantly run test methods on
    Mockito.when(mathy.mathematics(5)).thenReturn(3); // this method would ACTUALLy return 2, but I can control the return
    String result = calculator.evenOdd(5); // this method passes the 5 into our mocked object that then calls the mathematics method which we have mocked
    Assert.assertEquals("odd", result); // this test will pass because 3 is an odd number
}

@Test
public void isEven(){
    Mockito.when(mathy.mathematics(12)).thenReturn(6); // this is the result we would expect, so we make it the return value
    String result = calculator.evenOdd(12);
    Assert.assertEquals("even", result);
}

@Test
public void isOdd(){
    Mockito.when(mathy.mathematics(10)).thenReturn(5); // this is the result we would expect, so we make it the return value
    String result = calculator.evenOdd(10);
    Assert.assertEquals("odd", result);
}

 @Test
    public void checkMathematicsCalledWithCorrectInput(){
        Mockito.when(mathy.mathematics(9)).thenReturn(4);
        calculator.evenOdd(9);
        // verify will throw an exception if the mock object does not call the method with desired input
        // this is true mocking: checking that both the correct method and input are used
        Mockito.verify(mathy).mathematics(9);
    }

    @Test
    public void checkMathematicsCalledCorrectAmountOfTimes(){
        calculator.evenOdd(10);
        calculator.evenOdd(11);
        calculator.evenOdd(11);
        calculator.evenOdd(12);
        // use the times method if you want to check the amount of times a method with input is used
        Mockito.verify(mathy, VerificationModeFactory.times(2)).mathematics(11);
    }
```
6. run your tests and adjust your code as needed!
## Behavior vs State verification
We've talked about behavior and state verification in our application, but it also applies to our project as a whole. Behavior verification should be familiar to us: you are testing to make sure your project's functionality is working as intended. State verification, on the other hand, is a test to make sure that your database has ACTUALLY changed (or not changed) as you intended. These tests are fundamentally different from behavior tests: they are not interested in whether the function works as intended or not. All they are verifying is whether the STATE of the database (or object, etc) is what we expect it to be.
## Web Service Testing
This is what we have been doing with Postman, Cucumber, Behave, and Selenium. It is validating that our http requests are being recieved, handled, and responded to properly.