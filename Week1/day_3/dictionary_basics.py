""" dictionaries are, at their core, just key value pairs """

def function_called_by_key():
    return "this also works"
""" you have a lot of flexibility with how you create your dictionaries """
my_dictionary = {
    "key": "value",
    1: 100,
    "string key": 2,
    3: "a string value",
    None: "This still works",
    "I want to call a function": function_called_by_key(),
    function_called_by_key(): "does this work?",
    function_called_by_key: 0
}

print(my_dictionary["key"])
print(my_dictionary[1])
print(my_dictionary[None])
print(my_dictionary["I want to call a function"])
print(my_dictionary[function_called_by_key()])
print(my_dictionary["this also works"])
print(my_dictionary[function_called_by_key])

"""
You can use the items() method to return all the key value pairs as tuples.
They are given to you inside an iterable dictionary item
"""
def get_value_pairs(my_dictionary: dict):
    for pair in my_dictionary.items():
        print(pair)

get_value_pairs(my_dictionary)

""" 
you can either reference your a new key value like you are trying to acccess it and use the assignment
operator to assign a value to it, or you can use the update method and pass a dictionary object with the new
key value pair you want as the argument 
"""

# this is the short hand way
my_dictionary["This is a new key value"] = "this is the new value added with the new key"

print(my_dictionary["This is a new key value"])

# this is the slightly longer way
my_dictionary.update({"this is another new key": "this is another new value"})

print(my_dictionary["this is another new key"])

"""
the setdefault method will do one of two things:
if the key you provide already exists inside your dictionary it will return its associated value
if the key you provide does not already exist inside your dictoinary it will instead assign the value you
provided as the value for the new key value pair
"""
print(my_dictionary.setdefault("this is another new key", "I want to change the value to this new string"))
print(my_dictionary.setdefault(10, "I want to change the value to this new string"))

"""
you can get your values by either using the get method or by passing the key inside square brackets
like you are trying to access an index position
"""

# using get method
print(my_dictionary.get("key"))
# accessing the key directly
print(my_dictionary["key"])

"""
you can use the keys method to return an iterable collection of the keys in your dictionary, and likewise,
you can use the values method to return an iterable collection of the values in your dictionary
"""

print(my_dictionary.keys())
print(my_dictionary.values())
