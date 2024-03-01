"""
Conditional Statements...

if
elif (else if)
else

"""
marks = int(input("Enter Your Marks:"))

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







    
