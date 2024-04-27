# List concatenation
arr1 = [10, 20, 30, 40]
arr2 = ["mahesh", True, 5.6]

# Concatenating two lists using the '+' operator
arr3 = arr1 + arr2
print(f"arr3 is {arr3}")  # Output: arr3 is [10, 20, 30, 40, 'mahesh', True, 5.6]

# List repetition
arr4 = arr1 * 3
print(f"arr4 is {arr4}")  # Output: arr4 is [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]

# Checking if an element is in the list or not
print(10 in arr1)  # Output: True
print(100 not in arr1)  # Output: True



# Sorting and reversing a list
a = [10, 40, 20, 5, 60, 15]

# Sorting the list in ascending order
a.sort()  
# Reversing the sorted list
a = a[::-1]
print(a)  # Output: [60, 40, 20, 15, 10, 5]

# Sum of the least 3 elements in the list
a = [10, 40, 20, 5, 60, 15]
a.sort()  # Sorting the list
a2 = a[:3]  # Selecting the first 3 elements
print(a2)  # Output: [5, 10, 15]
print(sum(a2))  # Output: 30

# Finding the 2nd largest and 2nd smallest elements in the list
a = [10, 40, 20, 5, 60, 15]
a.sort()  # Sorting the list
second_largest = a[-2]  # 2nd largest element
second_smallest = a[1]  # 2nd smallest element
print(second_largest)  # Output: 40
print(second_smallest)  # Output: 10

# Finding the indexes of the largest and smallest elements
a = [10, 40, 20, 5, 60, 15]

# min_ele = min(a) # 5
# max_ele = max(a) # 60

# min_ele_idx = a.index(min_ele)
# max_ele_idx = a.index(max_ele)

# print(f"min ele is {min_ele} and its idx is {min_ele_idx}")
# print(f"max ele is {max_ele} and its idx is {max_ele_idx}")


# Using built-in functions to get the index of the largest and smallest elements
index_of_max = a.index(max(a))
index_of_min = a.index(min(a))
print(index_of_max)  # Output: 4 (index of largest element, which is 60)
print(index_of_min)  # Output: 3 (index of smallest element, which is 5)


