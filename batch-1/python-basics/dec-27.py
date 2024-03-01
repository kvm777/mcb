# n = int(input()) #1234

# print(n + int(str(n)[::-1]))

def fun1(n):
    s = str(n)
    a = int(s[0]) + int(s[-1])
    b = 0
    for i in s[1:len(s)-1]:  #"12345"
        b += int(i)

    print("a: ", a)
    print("b: ", b)

n = int(input())

fun1(n)