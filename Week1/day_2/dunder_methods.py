# you are already familiar with the __init__ dunder method: it is used to create the variables inside an object

# there are other dunder methods that can be useful to you as a developer

class ShowDunderMethods:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # this will now be returned any time we try and print our objects
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"



my_class = ShowDunderMethods("Timmy", 12)
print(my_class)


# dunder methods (or magic methods) are useful methods built into python that you can create unique implementation for common actions
