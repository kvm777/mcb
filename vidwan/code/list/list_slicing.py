# Slicing demonstration in Python

# List slicing
a = [10, 40, 50, 30, 40, 70, 90, 30]
#     0   1   2   3   4   5   6   7

# Basic slicing examples
print("Basic slicing examples:")
print(a[0:4])  # Output: [10, 40, 50, 30]
print(a[3:6])  # Output: [30, 40, 70]
print(a[2:7])  # Output: [50, 30, 40, 70, 90]
print(a[:6])   # Output: [10, 40, 50, 30, 40, 70]
print(a[4:])   # Output: [40, 70, 90, 30]
print(a[:])    # Output: [10, 40, 50, 30, 40, 70, 90, 30]

print("\nAfter step:")
# Slicing with step examples
print(a[1:7:2])  # Output: [40, 30, 70]
print(a[0:8:3])  # Output: [10, 30, 90]
print(a[::2])    # Output: [10, 50, 40, 90]
print(a[::3])    # Output: [10, 30, 90]
print(a[6:2:-1]) # Output: [90, 70, 40, 30]
print(a[::-1])   # Output: [30, 90, 70, 40, 30, 50, 40, 10]
print(a[::-2])   # Output: [30, 70, 30, 40]
print(a[::])     # Output: [10, 40, 50, 30, 40, 70, 90, 30]

# String slicing
s = "hello World"
#    0123456789 10

# Basic string slicing examples
print("\nBasic string slicing examples:")
print(s[4:8])   # Output: "o Wo"
print(s[:5])    # Output: "hello"
print(s[6:])    # Output: "World"
print(s[2:11])  # Output: "llo World"
print(s[:10])   # Output: "hello Worl"

print("\nUsing step:")
# String slicing with step examples
print(s[2:8:2]) # Output: "l o"
print(s[::-2])  # Output: "drWolh"
print(s[::-1])  # Output: "dlroW olleh"
