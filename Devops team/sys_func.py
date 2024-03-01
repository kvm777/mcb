# import sys

# def add(a, b):
#     return a+b


# n1 = sys.argv[1]
# n2 = sys.argv[3]

# print(add(n1,n2))

# import sys

# print("Script name:", sys.argv[0])
# print("Arguments:", sys.argv[1:])




# if we work with sensitive information... we use the environment varibles... as below
# if we run command -->>  env , we get the environment variables 
# we will give the values to env using following command..
#       export name="rajesh"

# import os

# print(os.getenv("name"))



import os

f = input().split()

for _ in f:
    files = os.listdir(_)
    print(files)