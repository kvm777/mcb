# arr = input().split()

# print(arr)

# arr1 = list(map(int, arr))
# print(arr1)



# l = [1,2,3,4,5,6,7]

# l1 = []

# for ele in l:
#     l1.append(ele*ele)

# print(l1)


# l = list(range(1,11))


# def square(n):
#     return n*n

# sqrs = list(map(square, l))
# print(f"sqrs: {sqrs}")


# sqrs1 = list(map(lambda x:x*x, l))
# print(f"sqrs1 {sqrs1}")



"""
lcm gcd

"""



# def lcm(m,n):
#     maxval = max(m,n)

#     while True:
#         if maxval % m==0 and maxval % n == 0:
#             return maxval
#         maxval+=1


def lcm(m,n):
    maxval = max(m,n)
    b = True
    while b:
        if maxval % m==0 and maxval % n == 0:
            out = maxval
            b = False
        maxval+=1

    return out

a, b = map(int, input().split())
print(lcm(a,b))


