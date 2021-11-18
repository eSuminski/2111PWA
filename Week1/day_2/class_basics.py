# to create a class you use the class keyword, give the class a name, and then a :
from abc import ABC, abstractmethod


class MyClass:
    # you can have state and behavior in a class
    # you set the state of the objects you will create inside your __init__ dunder method
    def __init__(self):
        print("this is run every time we create a MyClass object")


my_class_1 = MyClass()
my_class_2 = MyClass()


class SetState:
    def __init__(self, string_value: str, int_value: int):
        self.string_value = string_value
        self.int_value = int_value


my_set_state_obj = SetState("my string", 5)
print(my_set_state_obj.string_value, my_set_state_obj.int_value)


class HasFunction:
    def __init__(self, my_string: str):
        self.my_string = my_string
        print("our HasFunction class object was created")

    def get_my_string(self):
        return self.my_string


my_class = HasFunction("this is my string")
# to access the get_my_string method we first have to reference the object, and then we cana ccess the method
print(my_class.get_my_string())
# the line of code below is identical to the line above: the one below is what Python is doing under the hood
print(HasFunction.get_my_string(my_class))


class AbstractClass(ABC):

    @abstractmethod
    def inherited_method(self):
        pass


class Inheritor(AbstractClass):

    def inherited_method(self):
        print("I inherited this from the AbstractClass")


class InheritorTwo(AbstractClass):

    def inherited_method(self):
        print("I print something different than the Inheritor class")


my_inheriting_class = Inheritor()
my_inheriting_class_two = InheritorTwo()
my_inheriting_class.inherited_method()
my_inheriting_class_two.inherited_method()


# you can use the constructor of the parent class inside of the child class (the class that inherits)
class Person:
    # first you create the parent init method
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass


class Adult(Person):
    def __init__(self, name: str, age: int):
        # thie line of code calls the constructor of the parent class
        super().__init__(name, age)

    def speak(self):
        return "Hello! My name is {} and I am {} years old".format(self.name, self.age)



adulet = Adult("Eric", 127)
print(adulet.speak())


class TrueAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        # this tells the interpreter to ignore this method: it does not need to be defined at this time
        pass


class InheritsAbstractMethod(TrueAbstractClass):
    def my_abstract_method(self):
        return "I was given this method by the abstract class I inherited from"


class ClassVariablesExample:
    # this is a class variable: it is shared across all objects of this type
    my_class_variable = 0

    def __init__(self):
        ClassVariablesExample.my_class_variable += 1

    def check_my_class_variable(self):
        return f"The class variable is {ClassVariablesExample.my_class_variable}"


first_object = ClassVariablesExample()
second_object = ClassVariablesExample()
print(first_object.check_my_class_variable())
print(second_object.check_my_class_variable())


class HasClassMethod:
    # this is a class variable: the class method can only interact with it, not the object's self variables
    count = 0

    def __init__(self, num: int):
        HasClassMethod.count += 1
        self.num = num

    # this method can ONLY interact with class variables: it can not access individual objects' variables
    @classmethod
    def check_count(cls):
        return f"the class count is {cls.count}"

    # this method can interact with both class variables and its own variables
    def check_num(self):
        return "My num is {}".format(self.num)


new_object = HasClassMethod(5)
new_object_two = HasClassMethod(10)
print(new_object.check_num(), new_object.check_count())
print(new_object_two.check_num(), new_object_two.check_count())


class HasStaticMethod:
    count = 0

    def __init__(self, my_string: str):
        self.my_string = my_string

    @staticmethod
    def my_static_method():
        return "This method is usefl for utility only: it can not interact with the class or individual object's variables"


# there are four types of methods you can create with classes:
# abstract methods are those that have their implementation set in a class that inherits it
# static methods are those that are attached to the class but can not interact with class or object variables
# class methods are those that are attached to the class that can interact with class variables but not any object variables
# if you do not declare a method to be one of the above it is a normal method that can access both class and object variables

# Python supports multiple inheritance: this usually does not cause problems, but if you are not careful it can create a mess in your code

class One:
    def __init__(self, my_string: str):
        self.my_string = my_string
        print("dunder method was called from class One")


class Two:
    def __init__(self, my_number: int):
        self.my_number = my_number
        print("dunder method was called from class Two")


class Three(One, Two):
    def __init__(self, my_string: str, my_number: int):
        One.__init__(self, my_string)
        Two.__init__(self, my_number)
        print("Child init method was called")


my_three_class = Three("a string", 0)

# The Diamond Problem: Imagine you have 4 classes: A, B, C, D. B and C inherit class A, and class D inherits both B and C...

# The diamond problem can be solved, so to speak, but it requires a lot of programming gymnastics that you should not be doing
# in the first place. Moral of the story: try to limit your multiple inheritance

# best practice: do not have "grandparent" classes
