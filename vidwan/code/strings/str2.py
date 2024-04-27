s = "Hello WorlD"

# String methods for case manipulation
print("Uppercase:", s.upper())        # Output: HELLO WORLD     
print("Lowercase:", s.lower())        # Output: hello world
print("Capitalized:", s.capitalize())   # Output: Hello world    
print("Titlecased:", s.title())        # Output: Hello World
print("Swapcased:", s.swapcase())     # Output: hELLO wORLd

# Checking string properties
print("\nChecking String Properties:")
s1 = "hello"
print("Is lowercase?", s1.islower())     # Output: True

s2 = "Hello"
print("Is titlecased?", s2.istitle())     # Output: True
print("Is uppercase?", s2.isupper())     # Output: False

s3 = "HELLO"
print("Is uppercase?", s3.isupper())     # Output: True
print("Is alphanumeric?", s3.isalnum())     # Output: True

s4 = "hello123"
print("Is alphanumeric?", s4.isalnum())     # Output: True
print("Is digit?", s3.isdigit())     # Output: False

# Sorting and joining strings
s5 = "mahesh"
s6 = sorted(s5)
print("Sorted characters:", s6)               # Output: ['a', 'e', 'h', 'h', 'm', 's']
# ''.join(arr) method should be used when all elements are strings
print("Joined sorted characters:", ''.join(s6))      # Output: aehhms

s7 = s6[::-1]
print("Reversed joined sorted characters:", ''.join(s7))      # Output: smhhea



print()
print("hello".find("ll"))
print("hello".index("ll"))