################################################
#           spacing and indentation
################################################

x = 1
+ 2
print(x)        # 1

x = 1 \
    + 2
print(x)        # 3


def say_hello():
    print("Hello there!")


print(say_hello())
# Hello there!
# None


def say_hello2():
    print("Hello there!")


print(say_hello2())
# Hello there!
# None


# def say_hello():
# print("Hello there!")     # incorrect


#     def say_hello():
# print("Hello there")      # incorrect


################################################
#                variables
################################################

del x
# print(x)      # name 'x' not defined

x, y = 10, 20
print(x, y)     # 10 20
print(x + y)    # 30
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
print(x)         # (10+2j)
print(type(x))   # <class 'complex'>

x = "Alok"
y = "Shandilya"
print(type(x))      # <class 'str'>
print(x + y)        # AlokShandilya
print(x, y)         # Alok Shandilya
print(x + " " + y)  # Alok Shandilya
print("Hello, {} {}".format(x, y))      # Hello, Alok Shandilya

x = [3, 4, 5, "A", 777.7, "Shandilya"]  # list - [] square brackets
print(x[5])         # Shandilya
print(type(x))      # <class 'list'>
print(type(x[3]), type(x[4]))   # <class 'str'> <class 'float'>
x[3] = 7            # in list, we can change values
for i in x:
    print(i)        # 3, 4, 5, 7, 777.7, Shandilya (different lines)

x = (1, 2, "A", "Shandilya")
# x[1] = "hurray"   # type error (tuples doesn't support item assignment)
print(type(x))      # <class 'tuple'>
for i in x:
    print(i)        # 1, 1, A, Shandilya (different lines)

myDict = {1: 777, "2a": "A", 3: "Shandilya"}
print(type(myDict))     # <class 'dict'>
print(myDict)           # {1: 777, '2a': 'A', 3: 'Shandilya'}
print(x)                # (1, 2, 'A', 'Shandilya')
print(myDict[1])        # 777
print(myDict["2a"])     # A
for i in myDict:
    print(i)            # 1, 2a, 3 (different lines) (displays keys)

print(type(False))      # <class 'bool'>
print(type("True"))     # <class 'str'>
del x
del myDict

# A set is a collection which is unordered, unchangeable, and unindexed.
# but you can remove items and add new items.
mySet = {1, 2, "Alok", "Shandilya"}
print(type(mySet))      # <class 'set'>
# print(mySet[0])       # 'set' object is not subscriptable

################################################
#           some inbuilt functions
################################################
# print(), len(), str(), int(), float(), input() etc.

name = "Alok " \
       "Shandilya"
print(len(name))    # 14

myString = "7"
print(myString + str(9))     # 79 (type cast)
myString = int(myString)     # type cast
print(myString + 70)         # 77

# implicit type conversion, float(myString) is explicit
print(myString + float(myString))       # 14.0

# type error (can only concatenate str to str not float)
# print('7' + float(myString))

# print("Where do you live? ")
# location = input()  # eg. New Delhi
# print("You live in " + location)      # You live in New Delhi

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
num1 = input("Enter num1: ")  # let 10
num2 = input("Enter num2: ")  # let 20

# 1020 (everything typed in input() is converted to string in python)
print("The sum is :", num1 + num2)
print("The sum is :", float(num1) + float(num2))  # The sum is : 30.0
print("The sum is : " + str(float(num1) + float(num2)))  # The sum is : 30.0
# implicit type conversion works on + operator with strings, integers, floats
# but not in combination

# perhaps, you could have casted with input
# num1 = int(input("Enter num1: "))

################################################
#         user input, console output
################################################

# print() syntax
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# print() Parameters
# objects - object to the printed. * means may be more than one object
# sep - objects are separated by sep. Default value: ' '
# end - end is printed at last
# file - must be an object with write(string) method.
# (If omitted, sys.stdout will be used which prints objects on the screen)
# flush - If True, the stream is forcibly flushed. Default value: False

# sep, end, file, and flush are keyword arguments.
# If you want to use sep argument, you have to use
# print(*objects, sep = 'separator')
# print(*objects, 'separator') is incorrect


################################################
#                 operators
################################################

# math operators

# Addition (+)          ->   Adds two numbers.
# Subtraction (-)       ->   Subtracts the right operand from the left operand.
# Multiplication (*)    ->   Multiplies two numbers.
# Division (/)          ->   remember, result is a float
# Floor Division (//)   ->   eg. 15 // 2 gives 7, while -17 // 3 gives -6
# Modulus (%)           ->   Returns the remainder of the division.
# Exponentiation (**)   ->   left operand to the power of the right operand.
# Assignment (=)        ->   Assigns a value to a variable.

# logical operators

# Logical AND (and)     ->   Returns True if both operands are true.
# Logical OR (or)       ->   Returns True if at least one operand is true.
# Logical NOT (not)     ->   Returns the opposite boolean value of the operand.

################################################
#        conditional - if, elif, else
################################################

# control flow via conditional and loops

myAge = input("Enter your age : ")
myAge = int(myAge)

if myAge >= 13 and myAge < 18:
    print("You are a teen, but not eligible to vote")
elif myAge >= 18:
    isVoterCard = input("Do you have Voter ID card? (0 / 1) : ")
    # bool(0) is False, bool(1) is True
    # bool("1"), bool("0") are True (intput() accepts as string)
    # bool("") is False
    isBusy = input("Are you busy on election day? (0 / 1) : ")
    if int(isVoterCard) and not int(isBusy):
        print("You are eligible to vote, do vote in election")
    elif int(isVoterCard) and int(isBusy):
        print("Postpone your plans, and do vote on election day")
    else:
        print("You are eligible to vote, make your Voter ID card")
elif myAge >= 1 and myAge < 13:
    print("You are not a teen, grow old")
else:
    print("Invlid age")

################################################
#              switch / match
################################################
# match compares a value to several different conditions until one is met

match myAge:
    case 18:
        print("Just turned 18, congratulations")
        print("You can vote")
    case n if n > 18:
        print("You can vote")
    case _:
        print("You can't vote")

################################################
#             looping constructs
################################################
# for, while loop
# while loop, when to repeat a block of code as long as condition is true

# range(start, stop, step)
# start: The starting value of the sequence (optional, default is 0).
# stop: The end value of the sequence (exclusive).
# step: The step or increment between values (optional, default is 1).

print("##########################")

my_list = ["alok", 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")

# for fixing output issues with end=" "
# otherwise, output : alok 2 3 4 5 0 because of next loop's 0
print()

for i in range(5):      # range from 0 to 4
    print(i, end=" ")
print()

for i in range(1, 6):   # range from 1 to 5 (exclusive)
    print(i, end=" ")
print()

# print numbers from 1 to 5 using a while loop
counter = 1
while counter <= 5:
    print(counter, end=" ")
    counter += 1
print()

# use of break and continue in a loop
# prints 1 and 3
for i in range(1, 11):
    if i == 5:
        # break (terminates the loop prematurely)
        break       # Exit the loop when is 5
    if i % 2 == 0:
        # continue (skips rest of code inside loop for current iteration and
        # moves to next iteration)
        continue    # Skip even numbers
    print(i, end=" ")
print()

print("##########################")

################################################
#             enumerate()
################################################

# enumerate() function is used to iterate over a sequence while keeping track
# of the index of the current item. It returns tuples containing both the index
# and the corresponding element in the sequence.

# enumerate() syntax : enumerate(iterable, start=0)
# iterable: The sequence you want to iterate over
# start (optional): The index value from which counting starts, defaults to 0

# prints
# index : 0, value : Alok
# index : 1, value : MCA
# index : 2, value : Tezpur University
favourites = {"Alok", "MCA", "Tezpur University"}
for index, item in enumerate(favourites):
    print(f"index : {index}, value : {item}")       # format strings

################################################
#             pass statement
################################################

# pass statement is a null operation, serves as a placeholder where
# syntactically some code is required but you don't want to execute
# any instructions. It is often used as a stub when you are designing
# a function or a class and want to leave the implementation for later.


def my_function():
    pass        # TODO: Add implementation later


# in a conditional statement
choise = input("Enter for False / True as (0 / 1): ")
if int(choise):
    pass        # TODO: Handle this case later
else:
    # Your actual code for the else case
    print("condition is not met.")

# pass is generally used for having a syntactically correct structure that you
# can fill in with actual code later.
