################################################
#           spacing and indentation
################################################

x = 1 + 2
print(x)  # 3

x = 1
+ 2
print(x)  # 1

x = 1 \
  + 2
print(x)  # 3

def say_hello():
  print("Hello there!")
print(say_hello())  # Hello there! None (in different lines)

def say_hello2(): print("Hello there!")
print(say_hello2())  # Hello there! None

#def say_hello():
#print("Hello there!")   #incorrect
#
#  def say_hello():
#print("Hello there")    #incorrect

################################################
#                variables
################################################

del x
# print(x)    # name 'x' not defined

x, y = 10, 20
print(x, y)  # 10 20
print(x + y)  # 30
del (x, y)

################################################
#           data types (5)
################################################

# numeric (integer, float, complex number)
# sequence (string, list, tuples)
# dictionary
# boolean
# set

x = 10 + 2j
print(x)    # (10+2j)
print(type(x))  # <class 'complex'>

x = 'Alok'
y = "Shandilya"
print(type(x))  # <class 'str'>
print(x + y)    # AlokShandilya
print(x, y)     # Alok Shandilya
print(x + " " + y)  # Alok Shandilya
print("Hello, {} {}".format(x, y))  # Hello, Alok Shandilya

x = [3, 4, 5, "A", 777.7, "Shandilya"]      # list - [] square brackets
print(x[5])     # Shandilya
print(type(x))  # <class 'list'>
print(type(x[3]), type(x[4]))   # <class 'str'> <class 'float'>
x[3] = 7    # in list, we can change values
for i in x:
  print(i)    # 3, 4, 5, 7, 777.7, Shandilya (different lines)

x = (1, 2, "A", "Shandilya")
#x[1] = "hurray"   # type error (tuples doesn't support item assignment)
print(type(x))  # <class 'tuple'>
for i in x:
  print(i)    # 1, 1, A, Shandilya (different lines)

myDict = {1: 777, '2a': "A", 3: "Shandilya"}
print(type(myDict))  # <class 'dict'>
print(myDict)   # {1: 777, '2a': 'A', 3: 'Shandilya'}
print(x)    # (1, 2, 'A', 'Shandilya')
print(myDict[1])        # 777
print(myDict["2a"])     # A
for i in myDict:
  print(i)        # 1, 2a, 3 (different lines) (displays keys)

print(type(False))  # <class 'bool'>
print(type("True")) # <class 'str'>
del x
del myDict

# A set is a collection which is unordered, unchangeable, and unindexed.
# but you can remove items and add new items.
mySet = {1, 2, "Alok", "Shandilya"}
print(type(mySet))  # <class 'set'>
# print(mySet[0])     # 'set' object is not subscriptable

################################################
#           some inbuilt functions
################################################
# print(), len(), str(), int(), float(), input() etc.

name = "Alok " \
       "Shandilya"
print(len(name))    # 14

myString = "7"
print(myString + str(9))     # 79 (type cast)
myString = int(myString)    # type cast
print(myString + 70)     # 77
print(myString + float(myString))   # 14.0 (implicit type conversion), float(myString) is explicit
#print('7' + float(myString))   # type error (can only concatenate str to str not float)

#print("Where do you live? ")
#location = input()  # eg. New Delhi
#print("You live in " + location)    # You live in New Delhi

################################################
#           type casting
################################################

# int(): Converts a value to an integer.
# str(): Converts a value to a string.
# float(): Converts a value to a floating-point number.
# ord(): Returns the Unicode code point of a character.
# hex(): Converts an integer to a hexadecimal string.
# oct(): Converts an integer to an octal string.
# tuple(): Creates an immutable ordered collection.
# set(): Creates an unordered collection of unique elements.
# list(): Creates a mutable ordered collection.
# dict(): Creates a mutable collection of key-value pairs (dictionary).

print(ord("A"))     # 65
print(10 == 10.0)   # True
num1 = input("Enter num1: ")    # let 10
num2 = input("Enter num2: ")    # let 20
print("The sum is :", num1 + num2)    # 1020 (everything typed in input() is converted to string in python)
print("The sum is :", float(num1) + float(num2))    # The sum is : 30.0
print("The sum is : " + str(float(num1) + float(num2)))     # The sum is : 30.0
# implicit type conversion works on + operator with strings, integers, floats (not in combination)

################################################
#         user input, console output
################################################

# print() Syntax
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# print() Parameters
# objects - object to the printed. * indicates that there may be more than one object
# sep - objects are separated by sep. Default value: ' '
# end - end is printed at last
# file - must be an object with write(string) method.
# (If omitted, sys.stdout will be used which prints objects on the screen)
# flush - If True, the stream is forcibly flushed. Default value: False

# Note: sep, end, file, and flush are keyword arguments. If you want to use sep argument, you have to use
#print(*objects, sep = 'separator')
#print(*objects, 'separator') is incorrect