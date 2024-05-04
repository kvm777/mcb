# Prompt the user to enter a number to generate a multiplication table

num = int(input("Enter the multiplication table you want: "))  
# Get the desired multiplication table number from user

# Initialize the starting index for the loop
i = 1

# Use a while loop to generate the multiplication table from 1 to 10
while i <= 10:  # The loop runs from 1 to 10
    # Calculate the multiplication result for the current step
    result = num * i  # Multiplication of the input number with the current index
    
    # Display the formatted output
    print(f"{num} * {i} = {result}")  # Formatted multiplication expression
    
    # Increment the index for the next step
    i += 1  # Go to the next iteration (increment by 1)



# Expected Output:
# If the user inputs '3', the output will be:
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30
