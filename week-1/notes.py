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

del (x)
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
