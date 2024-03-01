# n = int(input("enter n value:"))
# k = int(input("enter k value:"))

# r = n%k     # 27 % 7 = 6

# if r ==0:
#     # print("n is divisble by k")
#     # print(n, "is divisble by", k)
#     print(f"{n} is divisible by {k}")
# else:
#     # print("n is not divisble by k")
#     # print(n, "is not divisble by", k)
#     print(f"{n} is not divisible by {k}")



"""
n -- input (0 - 100)

if n not in b/w 0 to 100 -->>invalid

80-100 -->> grade a
60 - 80 -->> grade b
40 -60 -->> grade c
less than 40 -->> fail



"""

# n = int(input())

# if n<=100:
#     if n>=80:
#         print("grade A")
# if n<80:
#     if n>=60:
#         print("grade B")
# if n<60:
#     if n>=40:
#         print("grade C")
# if n<40:
#     print("fail")
# else:
#     print("invalid")


# n = int(input())
# if n<0 or n>100:
#     print("invalid")

# elif n>=80 :
#     print("grade A")

# elif n>=60 :
#     print("grade B")

# elif n>=40:
#     print("grade c")

# else:
#     print("fail")


# n = int(input())

# if n <=100 and n>=0:
#     if n>=80:
#         print("grade A")
#     elif n>=60:
#         print("grade B")
#     elif n>=40:
#         print("grade C")
#     else:
#         print("fail")

# else:
#     print("invalid")


n = int(input())
if n%3==0 or n%5==0:
    if n%3==0 and n%5!=0:
        print("only 3")
    elif n%3!=0 and n%5==0:
        print("only 5")
    else:
        print("both")
else:
    print("not by both")