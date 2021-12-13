basic_dicitonary = {"key":"vlaue", "another key": "another value"}

print(basic_dicitonary) # prints key value pairs as a single string literal

print(basic_dicitonary.items()) # converts the key value pairs into a tuple and returns them inside a list

print(basic_dicitonary.keys()) # returns a list of keys

print(basic_dicitonary.values()) # returns a list of values

basic_dicitonary.setdefault("new key", "value") # returns the value of the key if it already exists in the dictionary, creates a new key and sets its value if it does not exist

print(basic_dicitonary["new key"]) # returns the value of the key

del basic_dicitonary["key"] # deletes the key value pair