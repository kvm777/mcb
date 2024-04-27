"""
Tuple in Python

A tuple is an ordered collection of items in Python. Unlike lists, tuples are immutable, meaning once they are created, their elements cannot be changed. They are defined using parentheses ().

Features of tuples:
- Tuples can contain elements of any data type: (10, True, "mahesh", 20.5).
- Elements in a tuple are accessed using indexing, starting from 0.
- Tuples support both positive and negative indexing.
- Tuples support slicing to retrieve subsets of elements.
- Tuples allow duplicate elements and can also contain other tuples, lists, dictionaries, or any other data type.

"""

# Example tuple
tup = (10, "mahesh", True, 25, 10.5, 10)

# Print type and content of the tuple
print(type(tup))
print(tup)

# Accessing elements of the tuple
print("\nAccessing elements:")
print(tup[2])  # Accessing the third element
print(tup[1])  # Accessing the second element

# Finding index and count of elements
print(tup.index(25))  # Finding the index of the element 25
print(tup.count(10))  # Counting the occurrences of the element 10

# Various operations on tuples
t1 = (10, 4, 20, 25, 30, 15)

print(f"Length of tuple t1 is {len(t1)}")
print(f"Maximum element in tuple t1 is {max(t1)}")
print(f"Minimum element in tuple t1 is {min(t1)}")
print(f"Sum of elements in tuple t1 is {sum(t1)}")


