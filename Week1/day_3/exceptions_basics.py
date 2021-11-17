"""
Exceptions are a reality that every programmer must deal with. They are actually useful tools for a developer, not
something to try and avoid entirely. Think of exceptions as ways to control what your application does when something goes wrong
"""

# print(5/0) this will crash our program with a ZeroDivisionError
import traceback

"""
You can use try/except blocks to handle exceptions when they arise in your code. You want to try and be as
specific with the exceptions you want to catch when you create these blocks of code.
"""

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(str(e))
    print("you can't divide by zero!")

try:
    1 + "2"
except TypeError as e:
    print(str(e))
    print("You can't add a string to a number")

try:
    # 1/0
    1 + "2"
except ZeroDivisionError as e:
    print(str(e))
except TypeError as e:
    print(str(e))

"""
best practice when it comes to catching exceptions is to be as specific as possible. If you can't be specific, or if
you need to have a catach-all, then you can use an except statement without an indicated exception you are trying to catch
"""

try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(str(e))
except:
    print("Something unexpected happened: check the logs!")

"""
You can add a finally block that always runs even if an exception occurs. you can use the traceback.format_exc()
method to determine where the exception happened inside your code
"""

try:
    1 / 0
except ZeroDivisionError:
    print(traceback.format_exc())
finally:
    print("this will always run, whether an exception happens or not")

"""
you can create a custom exception by creating a class, giving it a message variable, and thats it!
"""


class MyCustomException(Exception):
    def __init__(self, message: str):
        self.message = message

# an example of how you could use a custom exception
try:
    username = "dfnoeufnienknpwewkewckpww"
    if len(username) > 10:
        raise MyCustomException("your message for the exception goes in here")
    else:
        print("code continues")
except MyCustomException as e:
    print("we successfully raised our custom exception")
    print(str(e))

# you can use a try/finally block without an interceding except block
try:
    print("I work without an except block")
finally:
    print("this always runs")
