# first we declare the variable name, then we can declare the string literal
my_string = "whatever I want my string to be"

# there are a few different ways to do string interpolation
# string interpolation is simply making changes to your strings

# one of the easiest ways to do this is by string concatenation
greeting = "Hello"
name = "Eric"
print(greeting + name)
print(greeting + " " + name)

# there is also string formatting: you can use the f"" method or you can use the .format() method
full_greeting = f"Hello {name}!"
full_greeting_2 = "Hello {}!".format(name)
print(full_greeting_2)

# you can work with subsets of your string by doing string slicing

# in this example the first print statement will give us the first name
# the second print statement will give us the last name
full_name = "Eric Suminski"
print(full_name[0:4])
print(full_name[5:13])


# if I want to look at every other letter...
print(full_name[0::2])

# the string slicing positions are as follows: string[starting position: end position: increment amount]

# you can reverse a string by setting the increment to -1

print(full_name[::-1])

a = "Eric"
b = "Sam"
print("let's see if this works: {} and {}".format(a, b))

print(len(full_name))
