"""
and ---all the conditions should be True... it gives True
        
        Eg: True and True and True and False and True ----- False

or --- if atleast one should be True.. it gives True

        Eg: False or True or True or False or False ----- True

and -   True and True   - True
        True and False  - False
        False and True  - False
        False and False - False

or -   True or True   - True
        True or False  - True
        False or True  - True
        False or False - False

"""

# Evaluating expressions using logical operators

# Using 'and' operator: all conditions should be True for the result to be True
val = 10 < 15 and 15 <= 15
print(f"Result of 10 < 15 and 15 <= 15: {val}")  

# Using 'or' operator: at least one condition should be True for the result to be True
val1 = 10 < 15 or 15 <= 15
print(f"Result of 10 < 15 or 15 <= 15: {val1}")  

val2 = 10 < 15 or 15 < 15
print(f"Result of 10 < 15 or 15 < 15: {val2}")  

val3 = 10 < 15 and 15 < 15
print(f"Result of 10 < 15 and 15 < 15: {val3}")  

# Modulo operator (%) gives the remainder of the division
val4 = (11 % 2 == 0)  # Here, 11 % 2 equals 1, so it's not equal to 0
print(f"Result of 11 % 2 == 0: {val4}")  

        
"""
Output:
    Result of 10 < 15 and 15 <= 15: True
    Result of 10 < 15 or 15 <= 15: True
    Result of 10 < 15 or 15 < 15: True
    Result of 10 < 15 and 15 < 15: False
    Result of 11 % 2 == 0: False
"""