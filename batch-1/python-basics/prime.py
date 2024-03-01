# n = int(input())
# c=0
# for i in range(1,n+1):
#     if n%i == 0:
#         c+=1

# if c==2:
#     print("prime")
# else:
#     print("not prime")


# n= int(input())

# if n ==0 or n ==1:
#     print("not prime")

# elif n == 2:
#     print("prime")

# else:
#     for i in range(2,n):
#         if n%i == 0:
#             print("not prime")
            

n = int(input())

if n ==0 or n==1:
    print("not prime")

elif n==2:
    print("prime")

else:
    for i in range(2,n//2):
        if n%i == 0:
            print("not prime")
            break
    else:
        print("prime")
    

