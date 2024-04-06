# Identity operators: is, is not

# Comparison using `==` (equality operator)
# print(10 == 10)

arr1 = [10, 20]
arr2 = [10, 20]
arr3 = arr1  # arr3 points to the same object as arr1

# Print memory addresses of the lists
print("Memory address of arr1:", id(arr1))
print("Memory address of arr2:", id(arr2))
print("Memory address of arr3:", id(arr3))

# Using the 'is' operator to check if arr1 and arr2 point to the same object
print("Is arr1 the same object as arr2?", arr1 is arr2)  # Output: False
# Explanation: Although arr1 and arr2 have the same values, they are distinct objects in memory, so 'is' returns False.

# Using the 'is' operator to check if arr1 and arr3 point to the same object
print("Is arr1 the same object as arr3?", arr1 is arr3)  # Output: True
# Explanation: arr3 is assigned to arr1, meaning they both refer to the same list object in memory, so 'is' returns True.
