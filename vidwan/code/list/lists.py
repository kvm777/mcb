"""
Lists in Python

A list is an ordered collection of items in Python. Items in a list can be of any data type, such as numbers, floats, strings, tuples, dictionaries, or even other lists.

Features of lists:
- Lists are defined with square brackets: []
- Lists can contain elements of any data type: [10, True, "mahesh", 20.5]
- Lists are mutable, meaning their elements can be changed.
- Lists have various methods for manipulation.

"""

# Creating a list
arr = [10]
print(arr)  # Output: [10]

# Insertion methods - append(), insert(), extend()

# append() - Inserts data at the end of the list
arr.append(20)
print(arr)  # Output: [10, 20]
arr.append(40)
print(arr)  # Output: [10, 20, 40]

# extend() - Adds multiple values at the end of the list
arr.extend([10, 20, 30])
print(arr)  # Output: [10, 20, 40, 10, 20, 30]

# Indexing
"""
Indexing:
[10, 20, 40, 10, 20, 30]
0-10  (-6)
1-20  (-5)
2-40  (-4)
3-10  (-3)
4-20  (-2)
5-30  (-1)
"""
print(arr)  # Output: [10, 20, 40, 10, 20, 30]
print(arr[0])  # Output: 10
print(arr[3])  # Output: 10
print(arr[5])  # Output: 30
print(arr[-4])  # Output: 40
# print(arr[10]) # Index Out of range Error
print(arr[-1])  # Output: 30

# insert() - Inserts data at a specific index
arr.insert(2, 5.5)
print(arr)  # Output: [10, 20, 5.5, 40, 10, 20, 30]
arr.insert(4, "mahesh")
print(arr)  # Output: [10, 20, 5.5, 40, 'mahesh', 10, 20, 30]

print("\nAfter deletion methods")



# Deletion methods - remove(), pop(), clear()

arr.pop()  # Removes the last element
print(arr)  # Output: [10, 20, 5.5, 40, 'mahesh', 10, 20]

arr.pop(3)  # Removes the element at index 3
print(arr)  # Output: [10, 20, 5.5, 'mahesh', 10, 20]

arr.remove('mahesh')  # Removes the specified element
print(arr)  # Output: [10, 20, 5.5, 10, 20]

arr.remove(10)  # Removes the first occurrence of the specified value
print(arr)  # Output: [20, 5.5, 10, 20]

arr.clear()  # Clears the list
print(arr)  # Output: []


# print()
print("\n modify the ele in list")

a = [10, 20, 30, 40, 50]
print(a)
print(a[4])
a[4] = 400
print(a)