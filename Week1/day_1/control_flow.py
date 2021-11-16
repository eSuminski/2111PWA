phrase = "Hello World"

print(phrase)

# a for loop is used to determine how long a bit of code should run

my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number)

# if you use range you need to remember that the code will only iterate up to the value you provide
for number in range(0, 11):
    print(number)

# you can use a while loop to do functionally the same thing as a for loop, but it works a bit differently
x = 0
while x < 10:
    print(x)
    x += 1  # same thing as writing x = x + 1

# to exit this infinite loop you can press ctr + c to kill your code
# don't create infinite loops: it is bad practice
# while True:
#     print("oops")

# use for loops when you are working with data collections
# use while loops when you are making logical operations

# if elif else blocks are great when you have multiple possible scenarios you need to account for. Because the
# interpreter works line by line you should put the code that has priority at the top of the list
x = 8
y = 8
if x < y:
    print("Y is larger")
elif x == y:
    print("They are the same value")
elif x == 8:
    print("X is equal to 8")
else:
    print("X is larger")

my_name = "Eric"
sibling_name = "Eric"

# If blocks run if their statement is True, which can sometimes be confusing to understand

if my_name is sibling_name:
    print("we have the same name")
else:
    print("we do not have the same name")

if my_name is not sibling_name:
    print("we do not have the same name")
else:
    print("we have the same name")

# you can get wild with your if statements

x = 5
y = 7
z = 43
if y > x > z:
    print("neat")
elif x < y and x < z:
    print("that is a lot of comparisons")
