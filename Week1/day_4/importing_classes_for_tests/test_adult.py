"""this is how you import a class and test it"""
from day_2.class_basics import Adult

adult = Adult("Eric", 9823)

# tou can run this test by using the command: pytest day_4\importing_classes_for_tests\test_adult.py
def test_speak():
    desired_string = "Hello! My name is Eric and I am 9823 years old"
    assert adult.speak() == desired_string
