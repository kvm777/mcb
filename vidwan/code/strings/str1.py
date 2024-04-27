"""
Strings in Python

A string is a sequence of characters, which can be letters, numbers, or symbols, enclosed within quotes ('' or ""). 

"""

# Example usage of strings
print(10 + 20)        # This prints the sum of two numbers
print("10" + "20")    # This concatenates two strings
print('abc')          # This prints the string 'abc'

print("\nString Concatenation:")
s1 = "mahesh"
s2 = "rajesh"
print(s1 + s2)        # Concatenating two strings
print(s1, s2)         # Printing two strings separated by a space

# String slicing and reversing
print(s1[:4])         # Slicing to get the first four characters
print(s1[::-1])       # Reversing the string


print("\nAccessing Characters:")
print(s1[5])          # Accessing the character at index 5

# Finding the length of a string
print(f"Length of s1 is {len(s1)}")

# Modifying strings
s1 = "mahesh"
s1 = s1[:2] + s1[3:]  # Removing the character at index 2
print(s1)


