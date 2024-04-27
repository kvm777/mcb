# gap btw two nums

a = 60
b = 100

if a>b:
    print(a-b)
else:
    print(b-a)


# Calculate the difference (this might be negative if a < b)
difference = a - b

# The absolute difference ensures the result is always positive, regardless of the order
absolute_difference = abs(a - b)

# Output the results
print("Difference (a - b):", difference)  # This could be negative
print("Absolute difference:", absolute_difference)  # This is always positive

