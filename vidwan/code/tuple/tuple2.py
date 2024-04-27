t = (10, 30, 40, 50, 2, 50)

# Example usage of tuples
print(t)          # Printing the entire tuple
print(t[:3])      # Slicing to get the first three elements
print(t[-1])      # Accessing the last element
print(t[:6])      # Slicing beyond the length of the tuple
print(t[4:5])     # Slicing to get a single element
print(t[4:])      # Slicing from index 4 to the end
print(t[::-2])    # Reversing and skipping every second element

print("\nConcatenation in Tuples:")
t1 = (10, 30, 50)
t2 = (93, 3, 35)
print(t1 + t2)    # Concatenating two tuples

print("\nRepetition of Tuples:")
print(t1 * 3)     # Repeating a tuple three times
