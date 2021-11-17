# sets are very useful when you need to filter out redundant data. Sets are mallable, so you can add and remove
# elements from them, but they do not allow duplicates, and they are not indexable. This is because sets do not
# maintain the order of their elements

# these words will be in a random order
my_basic_set = {"I", "declare", "a", "thumb", "war"}
print(my_basic_set)
# be aware that some numeric values will keep their order, but this is not the norm
my_numeric_set = {1,2,3,4,5}
print(my_numeric_set)

my_basic_set.add("5")
my_basic_set.add("6")
my_basic_set.add("7")
my_basic_set.add("8")

print(my_basic_set)

# an easy way to get information from your set is to use the pop method
# pop will return a random element (first element in the set, which is randomly determined when you create/add to your
# set) from your set

print(my_basic_set.pop())
print(my_basic_set.pop())
print(my_basic_set)
# this is actually a simple way to create a randomizer: might be useful in the future

# there are two ways to remove elements from a set: discard and remove
# the difference between the two is that remove will raise an exception if the method does not actually remove anything
# but the discard method will not

print(my_basic_set)
# this line of code will cause an exception because there is no "me" in the set
# my_basic_set.remove(("me"))

# this is a low-stakes way of removing objects from your set: because no exception will be thrown if the data already
# does not exist in your set it is better suited for situations where you do not need confirmation that the object was
# removed
my_basic_set.discard("me")

# use the remove method if you need confirmation, use discard if confirmation is not needed

my_simple_list = ["one", "one", "two", "two", "three", "three"]
my_basic_set.update(my_simple_list)
print(my_basic_set)

# the update method can be used to add elements from an iterable object and pass them into the set
# this is useful if you want to check for unique values inside a list
check_unique_values: set = {0}
check_unique_values.clear()
check_unique_values.update(my_simple_list)
print(check_unique_values)
# you can actually cast your list as a set to get the unique values as well
# this does not change our initial list: we can still access it despite having cast it as a set object
print(set(my_simple_list))
print(my_simple_list)

