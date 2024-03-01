"""
Conditional Statements...

if
elif (else if)
else

"""
"""
marks = int(input("Enter Your Marks:"))
#55
if marks>100 or marks<0:
    print("Enter a marks btw 0 to 100")
    
elif marks>80 and marks<=100:
    print("grade A")

elif marks> 60 and marks<=80:
    print("Grade B")

elif marks> 40 and marks<=60:
    print("Grade C")

else:
    print("Fail")

"""

m = int(input())

if m > 100 or m < 0:
    print("Invalid")
else:
    if m>40:
        if m>60:
            if m>80:
                print("grade A")
            else:
                print("grade B")
        else:
            print("grade C")
    else:
        print("Fail")
    










    
