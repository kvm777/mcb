# """
# Set in Python

# A set is an unordered collection of unique elements in Python. Unlike lists or tuples, sets do not preserve the order of elements, as they are not indexed. Sets allow elements of any data type and do not allow duplicates. They are defined by enclosing elements within curly braces {}.

# """

# # Example usage of sets
# s = {1, True, 0, False, 2}
# print("Set with mixed types:", s) 

# s1 = {10, 20, 1, True, 5.6, 0, 0.0}
# print("Set with mixed numeric types:", s1)

# # Converting list to set and set to list
# arr = [10, 30, 40, 20, 30, 40, 10]
# arr1 = set(arr)     # Converting list to set
# arr2 = list(arr1)   # Converting set back to list
# print("Original List:", arr)
# print("Converted Set:", arr1)
# print("Converted List:", arr2)


# print("\nOther methods:")
# s3 = {10, 30, 40, 20, 30, 40, 10}
# print(f"Sum of elements in set: {sum(s3)}")      # Output: Sum of elements in set: 150
# print(f"Length of elements in set: {len(s3)}")   # Output: Length of elements in set: 4
# print(f"Maximum element in set: {max(s3)}")      # Output: Maximum element in set: 40
# print(f"Minimum element in set: {min(s3)}")      # Output: Minimum element in set: 10

# # Modifying a set
# s3.add(50)
# print("After adding 50:", s3)      # Output: After adding 50: {40, 10, 50, 20, 30}
# s3.remove(10)
# print("After removing 10:", s3)    # Output: After removing 10: {40, 50, 20, 30}

# # Discarding an element safely
# s3.discard(60)
# print("After discarding 60:", s3)   # Output: After discarding 60: {40, 50, 20, 30}

# # Sorting strings and sets
# s = "mahesh"
# print("Sorted characters in string:", sorted(s))  # Output: Sorted characters in string: ['a', 'e', 'h', 'h', 'm', 's']
# print("Sorted elements in set:", sorted(s3))      # Output: Sorted elements in set: [20, 30, 40, 50]

print()
s3 = {40, 50, 20, 30}
print("Original set:", s3)          # Output: Original set: {40, 50, 20, 30}

# Concatenation operation not supported in sets
# print([10, 20] + [30, 40])

# Adding elements from another set using update method
s3.update({40, 30, 50, 60})
print("Updated set:", s3)           # Output: Updated set: {40, 50, 20, 30, 60}

# Removing and returning an arbitrary element from the set using pop method
print("Popped element:", s3.pop())  # Output: Popped element: 40
print("Set after pop:", s3)         # Output: Set after pop: {50, 20, 30, 60}

