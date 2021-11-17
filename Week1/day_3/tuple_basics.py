"""
tuples are immutable data structures that can contain other objects. They are indexable, they are also iterable
so you can search through them using a for loop. They also allow duplicates.
"""

my_simple_tuple = ("these", "elements", "are", "stuck")

""" the count and index methods work the same way as you would expect in a list """
print(my_simple_tuple.count("are"))

print(my_simple_tuple.index("elements", 0, 2))

print(my_simple_tuple[3])

""" use tuples when you need a collection of objects that are constant, but also easy to access """