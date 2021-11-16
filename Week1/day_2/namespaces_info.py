from importing_global_variable import my_global_variable

# if we were importing from another folder the line would read from folder.file_name import global_variable
# namespace/scope is how Python tries to determine the value of your variables: it follows the LEGB acronym

# B = built-in: this scope is provided by Python itself. It is the key words you use when writing your code. They
# are built into the language and can be accessed at any place in your code

# if True:
#     while True:
#         if True:
# and on and on and on

# G = global. The global scope  is anything defined in the file itself. You can export and import global variables
# classes, anything you define within the file itself

# global variables are usually constant values, and so are named with SCREAMING_SNAKE_CASE.
MY_VARIABLE = "This is in the global scope"
print(my_global_variable)


def function_using_global_variable():
    # you can use the global keyword to access global variables
    global MY_VARIABLE
    return MY_VARIABLE + " how did you get in here?"


print(function_using_global_variable())


# E = enclosing. You really only see this when you have a function defined inside another function

def enclosed_namespace_example():
    # because we have another function in here this code block is now in the enclosing namespace
    enclosed_variable = "this is inside the enclosed space"

    def another_function():
        # notice you can actually access the enclosed variable inside this local space
        return enclosed_variable

    print(another_function())


enclosed_namespace_example()


# L = local. This is the namespace that is inside a code block. All variables within a local space are accessable to each other
# be aware that once a local block of code has executed it is no longer available.

def function_1():
    my_variable = "this is inside its own local namespace"
    # the variable above is no longer accessible once the function is finished


def function_2():
    my_variable_2 = "this is also inside its own local namespace"
    # the variable above is no longer accessible once the function is finished

# Python will check the namespaces in the order of: local, enclosed, global, built-in
