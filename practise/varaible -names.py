# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)
# on more than one variable "simultaneously" on the same line
name = "chaithra"
a, b = 3, 4
print(a, b)

age = 6
marks = 90.50

print(name)
print(age)
print(marks)
# Accessing an index
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1 which prints next number excluding 0 index
print(mylist[1]) # prints 2
print(mylist[2])
print(mylist[2])

# using basic addition, subtraction, multiplication, and division operators
number = 1 + 2 * 3 / 4.0
# print(number)
# Using two multiplication symbols
squared = 7 ** 2
cubed = 2 ** 3
# print(squared)
# print(cubed)
# Using Operators with Lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
# print(all_numbers)
# "%" operator is used to format a set of variables into single element
name = "John"
age = 44
# print("Hello, %s!" % name)
# print("Hello, %d!" % age)
# string using function
astring = "Hello world!"
astring2 = 'Hello world!'
# print(astring2)
string = "Hello world!"
# print(string.index("o"))
# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
# Boolean operators
x = 2
# print(x == 2)
# print(x < 3)
# print(x == 4)
name = "John"
if name in ["John", "Rick"]:
# print("Your name is either John or Rick.")
# using if else function
    x = 2
    if x == 2:
        print("x equals two!")
    else:
        print("x does not equal to two.")