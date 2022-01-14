## Mocking and Stubbing with Python
Python includes a built in ability to do mocking that is compatible with pytest. 
1. First thing you want to do is download pytest
```cli
pip install pytest
```
2. next create your code that needs to be tested
```python
# for this example we will make a divider class that is injected into a calculator class
class Divider:
    def division(self, num):
        return num / 2
```
```python
from package_a.module_a import Divider

class Calculator:
    def __init__(self, divider: Divider):
        self.divider = divider

    def even_odd(self, num):
        if self.divider.division(num) % 2 == 0:
            return "even"
        else:
            return "odd"
```
3. You can then write out your tests like normal
```python
divider = module_a.Divider()
calculator = module_b.Calculator(divider)


def test_even_result():
    assert calculator.even_odd(12) == "even"


def test_odd_result():
    assert calculator.even_odd(10) == "odd"
```
4. to create a basic stub you need to add the patch annotation to the test method. Inside the annotation you provide the link to what it is you are mocking, in our case the division method in the divider class, and the return value you want it to produce. Also, you must pass in an argument to the test method for the annotation to work
```python
# make sure to add the following to the top of your module: from unittest.mock import patch

@patch("package_a.module_a.Divider.division", return_value=2)
# passing in a argument called "our_mock" so our stub can work
def test_mock_even_result(our_mock):
    assert calculator.even_odd(10) == "even"


@patch("package_a.module_a.Divider.division", return_value=3)
def test_mock_odd_result(our_mock):
    assert calculator.even_odd(12) == "odd"

# you can also use magic mock to determine the return value, without the need to use the patch annotation or pass in an extra argument

# this also gives you easy access to mocking tests: verifying whether the state and/or behaviors acted as expected
def test_mock_verify_behavior():
    # notice we reference the division method in the divider object here, and use the MagicMock class to set the return value for the method
    calculator.divider.division = MagicMock(return_value=3)
    result = calculator.even_odd(10)
    calculator.divider.division.assert_called()


# this test makes sure the correct argument was passed through the method. useful when there is code you can't "see"
def test_mock_verify_state():
    calculator.divider.division = MagicMock(return_value=3)
    result = calculator.even_odd(10)
    calculator.divider.division.assert_called_with(10)
```
5. You can now write unit tests for your service and control methods by mocking the return values of any injected classes!