"""
Testing is a practice you should expect to become a daily part of your coding experience. It provides two great benefits
for you as a developer: it helps you ensure your code does exactly what you would expect it to do, and it helps prevent
you from adding feature creep into your application
"""
from abc import abstractmethod, ABC

"""
first we need something to actually test
"""


class Calculator(ABC):

    @abstractmethod
    def addition(self, num_one: int, num_two: int):
        pass

    @abstractmethod
    def subtraction(self, num_one: int, num_two: int):
        pass

    @abstractmethod
    def division(self, num_one: int, num_two: int):
        pass


""" 
after that we would want to create an implementation class and have it inherit all the methods we need to test.
Normally we would just add the pass keyword and then write our tests, but we have written the code out here so the
tests can run
"""


class CalculatorImp(Calculator):

    def addition(self, num_one: int, num_two: int):
        if isinstance(num_one, int) and isinstance(num_two, int):
            return num_one + num_two
        else:
            return "you can't do math on strings"

    def subtraction(self, num_one: int, num_two: int):
        if isinstance(num_one, int) and isinstance(num_two, int):
            return num_one - num_two
        else:
            return "you can't do math on strings"

    def division(self, num_one: int, num_two: int):
        # changed this to floor division to make sure we get an int back instead of a float
        if isinstance(num_one, int) and isinstance(num_two, int):
            return num_one // num_two
        else:
            return "you can't do math on strings"


"""
then we need to create an object of the thing we want to test
"""
calculator = CalculatorImp()

"""
now we can write our tests
"""


def test_addition():
    result = calculator.addition(5, 5)
    assert result is 10


def test_subtraction():
    result = calculator.subtraction(5, 5)
    assert result is 0


def test_division():
    result = calculator.division(10, 5)
    assert result is 2


"""
we have tests that handle our functions working with the correct inputs, but what if something goes wrong? We need to 
write tests to make sure our code can handle "edge cases", like strings being passed into our methods instead of ints
"""


def test_try_to_add_string():
    result = calculator.addition("1", 1)
    assert result is "you can't do math on strings"


def test_try_to_subtract_string():
    result = calculator.subtraction("1", 1)
    assert result is "you can't do math on strings"


def test_try_to_divide_string():
    result = calculator.division("10", 5)
    assert result is "you can't do math on strings"


"""
we could keep going and going with these tests, but we will stop here.
"""

"""
The reason you need to know how to write good tests is because companies will expect you to know how to do
Test Driven Development (TDD)

This is a development mindset where your tests drive your development. The process looks like this:

step 1: create an "interface" for your application. In Python this would be an abstract class: you will also
        want to have a class that implements its abstract methods, but while writing your tests you can have the
        pass keyword as a placeholder for your method implementations.

step 2: create tests that will validate your function both works as intended, and fails as intended. 

step 3: implement your methods in a way that they will pass all of your tests. Good test designs are key for this
        to be meaningful.
        
step 4: repeat this process as necessary 
"""
