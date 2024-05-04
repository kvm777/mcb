"""
i/p - 10 40 60 33 54 50 55 70

only 10 divibles.. space separated..
o/p - 10 40 60 50 70

"""

arr = list(map(int, input().split()))
print(arr)

divs = []
for ele in arr:
    if ele%10 == 0:
        divs.append(ele)

print(divs)
print(*divs)



"""
factorial of number...

i/p - 5
o/p - 120

i/p - 6
o/p - 720

5! = 5*4*3*2*1


"""

def factorial(num):
    # write your code
    if num == 0 or num == 1:
        return 1
    else:
        f = 1
        for i in range(1,num+1): #1 to 5
            f *= i
        return f

n = int(input())
print(factorial(n))

