# Membership operators: in, not in

arr1 = [10, 20, 30]
s = "mahesh"

# Check if 20 is present in arr1
print("Is 20 present in arr1?", 20 in arr1)  # Output: True

# Check if "sh" is present in string s
print("Is 'sh' present in s?", "sh" in s)  # Output: True

# Check if 40 is not present in arr1
print("Is 40 not present in arr1?", 40 not in arr1)  # Output: True

# Check if "v" is not present in string s
print("Is 'v' not present in s?", "v" not in s)  # Output: True

# Using 'not in' operator
print("Is 20 not present in arr1?", 20 not in arr1)  # Output: False
print("Is 'v' not present in s?", "v" not in s)  # Output: False
