# Theory: Understanding `while` Loops
# A `while` loop in Python allows you to execute a block of code repeatedly as long as the given condition is `True`.
# The loop typically consists of:
#   1. Initialization: Setting an initial value for the variable(s) involved in the condition.
#   2. Condition: The boolean expression that determines if the loop should continue running.
#   3. Increment: A step that updates the condition variable(s) to avoid infinite loops.
# Be careful to include an increment or similar mechanism to ensure the loop eventually stops.

# Example 1: Using a `while` loop to print a message 10 times
count = 1  # Step 1: Initialization
while count <= 10:  # Step 2: Condition
    # This block runs as long as count is less than or equal to 10
    print(count, "hello")
    # Step 3: Increment
    count += 1

# Expected Output:
# 1 hello
# 2 hello
# 3 hello
# ...
# 10 hello

# Example 2: Using a `while` loop to print cubes of numbers from 1 to 10
c = 1  # Step 1: Initialization
while c <= 10:  # Step 2: Condition
    # Calculate and print the cube of the current value of c
    print(c ** 3)
    # Step 3: Increment
    c += 1

# Expected Output:
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000

# Example 3: Using a `while` loop to iterate over a list of numbers
arr = [10, 20, 30, 40, 50, 70, 200]  # An array to iterate over
i = 0  # Step 1: Initialization
while i < len(arr):  # Step 2: Condition
    # Access and print the current element in the list
    print(arr[i])
    # Step 3: Increment to move to the next item in the list
    i += 1

# Expected Output:
# 10
# 20
# 30
# 40
# 50
# 70
# 200


