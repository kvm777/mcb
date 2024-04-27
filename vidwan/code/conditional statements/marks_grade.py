"""
m<0 or m>100 --invalid

else:
    m>80 - A
    m>60 - B
    m>40 - C
    else: - fail

"""

# marks = 400

# if marks<0 or marks>100:
#     print("invalid")
# else:
#     if marks > 80:
#         print("A grade")
#     elif marks >60:
#         print("B grade")
#     elif marks > 40:
#         print("C grade")
#     else:
#         print("Fail")

 
# Get the marks (assuming this is provided by user input or another function)
marks = -5

# Validate that marks are within the correct range
if 0 <= marks <= 100:
    # Assign grades based on the marks
    if marks > 80:
        print("Grade: A")
    elif marks > 60:
        print("Grade: B")
    elif marks > 40:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    # Handle invalid input
    print("Error: Marks should be between 0 and 100.")




