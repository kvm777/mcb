# user defined functions..

"""
default arguments
positional arguments
named arguments

"""
# def printingHello(name="rajesh"):
#     print("hello",name)

# printingHello("mahesh")
# printingHello()


# positional arguments

# def fun1(a,b):
#     print("a:", a)
#     print("b:", b)

# fun1("b value","a value")

# keyword arguments

# def fun1(a,b):
#     print("a:", a)
#     print("b:", b)

# fun1(b = "b value",a = "a value")


# def sum(*a):
#     c=0
#     for i in a:
#         c+=i
#     print(c)

# sum(10,23,4,6,6,56,5)



# Recursive function..

# 5! = 120 = 1*2*3*4*5

# factorial code..


# def factorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f*=i

#     # print(f)
#     return f

# n = int(input())
# output = factorial(n)
# print(output)


# recursive fuction...
# def recfun(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*recfun(n-1)

# print(recfun(5))


"""
5 * rec(4)

5 * ( 4 * rec(3))

5 * ( 4 * ( 3 * rec(2)))

5 * ( 4 * ( 3 * (2 * rec(1))))

5 * ( 4 * ( 3 * (2 * 1)))



"""

# lambda function...

add = lambda x,y : print(x+y)

add(5,10)
