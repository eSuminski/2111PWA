# to create a function you need three things: def function_name(parameters)

def basic_function():
    # any code associated with your function is tabbed underneath it
    return "this is a basic function"  # use the return keyword to indicate what you are returning from the method


print(basic_function())

# functions are a great way to assign data to variables
value = basic_function()
print(value)


def basic_function_with_params(num_1, num_2):
    return num_1 + num_2


print(basic_function_with_params(3, 4))
print(basic_function_with_params("three", "four"))


# to tell your ide what type of data you want you can use type annotations

def function_with_type_annotations(number_1: int, number_2: int) -> int:
    return number_1 + number_2


print(function_with_type_annotations(1, 2))
print(function_with_type_annotations("one", "two"))


# python supports varargs, this allows you to write a function that takes in a variable amount of data
# you add a * in front of the paramater name to indicate it is a vararg
# make sure you put your vararg at the end of the parameter list
def function_with_vararg(*args: int) -> int:
    value = "0"
    for num in args:
        value += num
    return value


print(function_with_vararg("1", "2", "3", "4"))


# print(function_with_vararg("1",2,"three",4)) your interpreter will try to run this, but you will run into a type error

# you can also put in a key word argument (kwarg) by adding two * in front of the parameter name
# this function is expecting to have a username and password key that we will provide a value to
def function_with_kwargs(**kwargs):
    print(kwargs["username"])
    print(kwargs["password"])


# the keys are decalred inside the method as arguments, and their value is also defined inside as an argument
function_with_kwargs(username="myUsername", password="myPassword")


def another_kwarg_function(**kwargs):
    for element_one, value in kwargs.items():
        print(f"the key is {element_one} and the value is {value}")


# make sure you provide the key and value pair
another_kwarg_function(name="Eric", profession="Eric")


# you can use the match/case key words to control the flow of your code
def using_match_case(number: int) -> str:
    match number:
        case 1:
            return "You entered the number 1"
        case _:
            return "There were no matches"


print(using_match_case(2))


# this is basically the same thing as above
def multiple_options(number: int) -> str:
    if number is 1:
        return "you entered the number 1"
    else:
        return "There were no matches"


print(multiple_options(2))


# you can nest functions inside of each other

def function_within_a_function():
    my_variable = "Eric Suminski"

    def function_within_function(a_variable: str) -> str:
        return "Hello {}".format(a_variable)

    return function_within_function(my_variable)


def function_that_takes_in_function(my_function) -> str:
    my_new_variable = "Luke Suminski"
    return_value = my_function(my_new_variable)
    return return_value


def passed_into_other_function(a_string: str) -> str:
    return f"Hello {a_string}"


print(function_within_a_function())
print(function_that_takes_in_function(passed_into_other_function))
