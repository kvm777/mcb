"""
Data Types...
    int - # Whole numbers without any decimal points
            - Examples: 0, 1, 2, 3, ...
    float - Decimal numbers, represented as floating-point numbers
            - Examples: 2.4, 5.0, 10.564
    Boolean - Represents logical values indicating either true or false
            - Examples: True, False
    string - A sequence of characters enclosed within quotes
            - Examples: "mahesh", "hello world"
    
    ...CONTINUES...
    
    list - Lists: ordered and changeable collections allowing duplicate elements.
            - Example: [1, 2, 'a', 'b']
    tuple - Tuples: ordered and unchangeable collections allowing duplicate elements.
            - Example: (1, 2, 'a', 'b')
    set - unordered and unindexed collections not allowing duplicate elements.
            - Example: {1, 2, 'a', 'b'}
    dictionary -Dictionaries: unordered, changeable, and indexed collections with keys and values.
            - Example: {'name': 'mahesh', 'age': 25, 'city': 'vizag'}
    range - represents a sequence of numbers.
            - Example: range(0, 10)
"""
#all the above are comment are not excicuted while we run the code



# Declaring and printing an integer variable
a = 10  # 10 is stored in variable a
print(a)  # Output: 10
print(type(a))  # Output: <class 'int'>

print()  # Empty print method to print a blank line and move to the next line

# Declaring and printing a float variable
b = 3.5
print(b)  # Output: 3.5
print(type(b))  # Output: <class 'float'>

print()

# Printing the types of True and False
print(type(True))  # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>

print()

# Declaring and printing a string variable
c = "mahesh"
print(c, type(c))  # Output: mahesh <class 'str'>
print("10", type("10"))  # Output: 10 <class 'str'>

# Declaring and printing a string variable which appears like a float
d = "3.67"
print(d, type(d))  # Output: 3.67 <class 'str'>

"""
OUTPUT: 
    10
    <class 'int'>

    3.5
    <class 'float'>

    <class 'bool'>
    <class 'bool'>

    mahesh <class 'str'>
    10 <class 'str'>
    3.67 <class 'str'>
"""


# previous datatypes all above...

print()
# list - Ordered, changeable collection of data that allows duplicates
arr = [10, "mahesh", True, 3.6, 20, 10]  # Creating a list containing various data types
print(arr)  # Printing the list
print(type(arr))  # Printing the type of 'arr' which should be <class 'list'>

print()

# tuple - Ordered, unchangeable collection that allows duplicates
t = (10, "mahesh", True, 3.6, 20, 3.6, 3.6)  # Creating a tuple
print(t)  # Printing the tuple
print(type(t))  # Printing the type of 't' which should be <class 'tuple'>

print()

# set - Unordered, unindexed collection that doesn't allow duplicates
s = {10, 20, 30, 10, 40, 1, 2, 1, 2, 40}  # Creating a set
print(s)  # Printing the set
print(type(s))  # Printing the type of 's' which should be <class 'set'>

print()

# dictionary - Data stored in key-value pairs, changeable
dic = {"name": "mahesh", "age": 20}  # Creating a dictionary
print(dic)  # Printing the dictionary
print(type(dic))  # Printing the type of 'dic' which should be <class 'dict'>
print(dic.keys())  # Printing the keys of the dictionary
print(dic.values())  # Printing the values of the dictionary
print(dic.items())  # Printing the key-value pairs of the dictionary

print()

# range - A sequence of numbers
print(list(range(5)))  # Printing a list of numbers from 0 to 4
print(list(range(1, 5)))  # Printing a list of numbers from 1 to 4
print(list(range(11, 11)))  # Printing an empty list as start and end are the same
print(list(range(0, 11, 2)))  # Printing a list of even numbers from 0 to 10
print(list(range(1, 11, 2)))  # Printing a list of odd numbers from 1 to 10
print(list(range(3, 11, 3)))  # Printing a list of numbers from 3 to 10 with a step of 3
print(list(range(10, 1, -1)))  # Printing a list of numbers from 10 to 2 in reverse order

"""
OUTPUT:
    [10, 'mahesh', True, 3.6, 20, 10]
    <class 'list'>

    (10, 'mahesh', True, 3.6, 20, 3.6, 3.6)
    <class 'tuple'>

    {1, 2, 40, 10, 20, 30}
    <class 'set'>

    {'name': 'mahesh', 'age': 20}
    <class 'dict'>
    dict_keys(['name', 'age'])
    dict_values(['mahesh', 20])
    dict_items([('name', 'mahesh'), ('age', 20)])

    [0, 1, 2, 3, 4]
    [1, 2, 3, 4]
    []
    [0, 2, 4, 6, 8, 10]
    [1, 3, 5, 7, 9]
    [3, 6, 9]
    [10, 9, 8, 7, 6, 5, 4, 3, 2]

"""
