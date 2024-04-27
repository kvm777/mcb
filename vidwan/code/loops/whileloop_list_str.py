# Given array of integers
arr = [10, 30, 40, 50, 100, 60]

# Initialize a variable to store the running total
sum_value = 0

# Initialize index for while loop
i = 0

# Iterate while index is less than the length of the array
while i < len(arr):
    # Display the current index and the value at that index
    print(f"Index: {i}, Current Value: {arr[i]}")

    # Add the current value to the running total
    sum_value += arr[i]

    # Increment index to move to the next element
    i += 1

# After exiting the loop, print the final sum
print(f"Total Sum of Array: {sum_value}")


"""
Expected output:

Index: 0, Current Value: 10
Index: 1, Current Value: 30
Index: 2, Current Value: 40
Index: 3, Current Value: 50
Index: 4, Current Value: 100
Index: 5, Current Value: 60
Total Sum of Array: 290

"""


# Initialize a variable to store the running product (start with 1)
product_value = 1

# Reset the index for the while loop
i = 0

# Iterate while index is less than the length of the array
while i < len(arr):
    # Multiply the current value with the running product
    product_value *= arr[i]

    # Increment index to move to the next element
    i += 1

# After exiting the loop, print the final product
print(f"Total Product of Array: {product_value}")


#Output:  Total Product of Array: 10 * 30 * 40 * 50 * 100 * 60 = 36000000
