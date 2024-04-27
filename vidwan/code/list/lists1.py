"""
Additional List Methods

More methods for manipulating lists in Python:

- index(): Find the index of a specific element.
- count(): Find the count of a specific element.
- sort(): Sort all elements in ascending order.
- copy(): Create a new object with the same data.
- reverse(): Reverse the order of elements.
    arr.method()
"""

# Given list
a = [10, 40, 50, 30, 90, 5, 55, 30, 40, 70, 90, 30]
print(a)

# index()
print(a.index(30))  # Output: 3
# count()
print(a.count(30))  # Output: 3
print(a.count(40))  # Output: 2


# sort()
print("\nAfter sort method")
a.sort()
# sorted list
print(f"a arr is {a}")  # Output: a arr is [5, 10, 30, 30, 30, 40, 40, 50, 55, 70, 90, 90]

# copy()
b = a.copy()
print(f"b arr is {b}")  # Output: b arr is [5, 10, 30, 30, 30, 40, 40, 50, 55, 70, 90, 90]

# Assigning by reference
c = a
print(f"c arr is {c}")  # Output: c arr is [5, 10, 30, 30, 30, 40, 40, 50, 55, 70, 90, 90]

# Check the IDs
print(id(a))    # Output: 2600764233856
print(id(b))    # Output: 2600764554240 
print(id(c))    # Output: 2600764233856 

# reverse()
print("\nAfter reverse method")
a.reverse()
print(f"a arr is {a}")  # Output: Reversed list
                        # Output: a arr is [90, 90, 70, 55, 50, 40, 40, 30, 30, 30, 10, 5]
print(f"b arr is {b}")  # Output: b arr is [5, 10, 30, 30, 30, 40, 40, 50, 55, 70, 90, 90]
print(f"c arr is {c}")  # Output: c arr is [90, 90, 70, 55, 50, 40, 40, 30, 30, 30, 10, 5]

"""
Other useful list methods:

- sum(): Find the sum of all elements in the list.
- max(): Find the maximum element in the list.
- min(): Find the minimum element in the list.
- len(): Find the size of the list.
"""

# Other useful methods
print(f"Sum of elements in arr is {sum(a)}")# Output: Sum of elements in arr is 540
print(f"Max element in arr is {max(a)}")    # Output: Max element in arr is 90
print(f"Min element in arr is {min(a)}")    # Output: Min element in arr is 5
print(f"Length of arr is {len(a)}")         # Output: Length of arr is 12




