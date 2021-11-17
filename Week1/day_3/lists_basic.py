# lists are the most flexible data structure for you as a developer
# you can make changes to it, add duplicates, and it is indexable

# give your list a name, then you can place the elements you want inside it between square brackets
# separate the elements with a comma
my_basic_list = [1, 2, 3, 4]

print(my_basic_list[0])

# this adds some object into our list at the index position we determine
# .insert(index_position, element_you_want_to_add)
my_basic_list.insert(4, 5)

print(my_basic_list)

my_basic_list.insert(0, 0)

print(my_basic_list)

# the append method will take your element and add it to the end of the list
my_basic_list.append(6)

print(my_basic_list)

another_list = [7, 8, 9, 10]

third_list = [11, 12, 13]

# the extend method lets you append the elements inside another iterable data structure into your list
my_basic_list.extend(another_list)
# this is how you could append a single element into your list
my_basic_list.append(third_list[1])
my_basic_list.append(third_list[1])

print(my_basic_list)

# the remove method will remove the FIRST element it finds that matches the argument you provide
my_basic_list.remove(12)

print(my_basic_list)

print(my_basic_list.pop(11))
print(my_basic_list)

# the clear method will remove all data from your list, leaving it blank
my_basic_list.clear()
print(my_basic_list)

my_basic_list.append("a string")

# you can also use the del key word to remove an element from a specified position
del my_basic_list[0]

print(my_basic_list)

# you can mix and match your data types inside of a list
# you can add type annotations to your list and even indicate the types of data you expect to add to it
my_basic_list: list[str | int] = ["a", "b", "c", "a", "a", "b", 1, 2, 3]

print(my_basic_list.count("a"))
print(my_basic_list.count("b"))

# the index method gives you flexibility on where you search through your list
# you can indicate the specific index positions you wish to check, and if the element is not in those index positions
# you will get an error
print(my_basic_list.index("c", 0, 4))

# you can use the sort method to organize your data
my_basic_list = [2, 5, 1, 7, 6, 32, -1]
print(my_basic_list)
my_basic_list.sort()
print(my_basic_list)
# you can set reverse to True to make the list ordered from greatest to smallest as opposed to smallest to greatest
my_basic_list.sort(reverse=True)
print(my_basic_list)

# this information is more complex, so we need to create a key to determine how to organize the data
my_basic_list: list[list] = [[2, "c"], [1, "b"], [3, "a"]]

print(my_basic_list)


# we can create a method to work as the key for our sort method. This one tells the sort to look at the first element
# inside the list
def organize_by_number(elements):
    return elements[0]


my_basic_list.sort(key=organize_by_number)

print(my_basic_list)


# if we use this key instead the sort will organize the lists by their second element, which in this case will be
# letters
def organize_by_letter(elements):
    return elements[1]


my_basic_list.sort(key=organize_by_letter)
print(my_basic_list)


# you can do the same thing for classes. Best practice is to create an identifier variable that can be used to organize
# your objects
class Person:
    # this person_id will be used to organize our Person objects
    person_id = 1
    # we added this for fun to keep track of our objects
    person_list = []

    def __init__(self, age: int, name: str):
        self.id = Person.person_id
        self.age = age
        self.name = name
        # make sure to change the value of the identifier so that everyone has a unique one
        Person.person_id += 1
        Person.person_list.append(self)

    def __str__(self):
        return "My name is {} and I am {} years old".format(self.name, self.age)

    def sort_by_id(self):
        return self.id


tim = Person(28, "Tim")
shelly = Person(56, "Shelly")
bob = Person(2, "Bob")

my_basic_list = []
my_basic_list.append(shelly)
my_basic_list.append(tim)
my_basic_list.append(bob)
print(my_basic_list[0])
print(my_basic_list[1])
print(my_basic_list[2])

my_basic_list.sort(key=Person.sort_by_id)

print(my_basic_list[0])
print(my_basic_list[1])
print(my_basic_list[2])

# this shows that our person list is populated each time we create a person
print(Person.person_list)

# if you ever need to reverse a list you can use the reverse method
my_basic_list = ["these", "words", "are", "in", "order"]
print(my_basic_list)
# you could use the code below to reverse your list, but this would get tiresome to constantly write
# reversed_list = []
# for word in my_basic_list[::-1]:
#     reversed_list.append(word)
# print(reversed_list)

# you can use the reverse method instead to do the same thing
my_basic_list.reverse()
print(my_basic_list)

# you can use the copy method if you need to duplicate your list for some reason
copied_list = my_basic_list.copy()
print(my_basic_list)
print(copied_list)



