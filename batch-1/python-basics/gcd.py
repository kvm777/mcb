# print("hello")


"""
10 -- 1,2,5, 10

30 - 1,2,3,5,6,10,15, 30

"""


def gcd(input1 ,input2):
    #write your code...
    m = input1
    n = input2
    minval = min(m,n)
    """
    m =10
    n = 30
    minval = 10
    loop --- 10 -> 0
    i --- 10,9,8,....1
    """
    for i in range(minval, 0, -1):
        if m%i==0 and n%i ==0 :
            return i
    pass

# a, b = map(int, input().split())
# print(gcd(a,b))


# gcd by using diviors....


def divisors(num):
    arr = []
    for i in range(1,num+1):
        if num%i==0:
            arr.append(i)
    # print(arr)
    return arr


# n = int(input())
# divisors(n)
# print(divisors(n))
# print(*divisors(n))


def gcdTwo(m,n):
    arr1 = divisors(m)
    arr2 = divisors(n)

    if m<n:
        finarr = arr1
        otharr = arr2
    else:
        finarr = arr2
        otharr = arr1

    finarr = finarr[::-1]
    for ele in finarr:
        if ele in otharr:
            return ele


a = int(input())
b = int(input())
print(gcdTwo(a,b))