# n = int(input("size"))
# arr =[]
# for i in range(n):
#     x= int(input("value"))
#     arr.append(x)

# print(arr)

# arr = input().split()
# print(arr)
# arr = list(map(int, arr))

arr = list(map(int, input().split()))
print(arr)

print(*arr)

c = 0
for i in arr:
    c+=i
print(c)