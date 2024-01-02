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

def say_hello(): print("Hello there!")
print(say_hello())  # Hello there! None

# def say_hello():
# print("Hello there!")   #incorrect
#
#     def say_hello():
# print("Hello there")    #incorrect

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

x = [3, 4, 5, "A", 777.7, "Shandilya"]      # list - [] square brackets
print(x[5])     # Shandilya
print(type(x))  # <class 'list'>
print(type(x[3]), type(x[4]))   # <class 'str'> <class 'float'>
x[3] = 7    # in list, we can change values
for i in x:
    print(i)    # 3, 4, 5, 7, 777.7, Shandilya (different lines)

x = (1, 2, "A", "Shandilya")
# x[1] = "hurray"   # tuples doesn't support item assignment, no error, no output
print(type(x))  # <class 'tuple'>
for i in x:
    print(i)    # 1, 1, A, Shandilya (different lines)

myDict = {1: 777, '2a': "A", 3: "Shandilya"}
print(type(myDict))  # <class 'dict'>
print(myDict)   # {1: 777, '2a': 'A', 3: 'Shandilya'}
print(x)    # (1, 2, 'A', 'Shandilya')
print(myDict[1])        # 777
print(myDict['2a'])     # A
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
#print(mySet[0])     # 'set' object is not subscriptable
