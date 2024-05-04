# recursive function..

def fact(num):
    if num == 0 :
        return 1
    return num * fact(num-1)

print(fact(10))

"""
5 * fact(4)-> 5 * 4 * fact(3) -> 5*4*3*2*1
"""

# factorial of a num without using recurcive func


# lambda func

def sum(a, b):
    return a+b

lambdaSum = lambda a,b: a+b

print(sum(10, 20))
print(lambdaSum(10,20))


