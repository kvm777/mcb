# s = "rajesekhar"

# output: RAjEsEkhAR

# s = input()         #rajsekhar
# print(s)

# out = ""
# for e in s:
#     if s.count(e) == 1:
#         out += e.lower()
#     else:
#         out += e.upper()

# print(out)



arr = list(map(int, input().split()))
f = arr[0]

out = []
for i in range(1, len(arr)):
    if arr[i]%f == 0:
        # print(arr[i], end=" ")
        out.append(arr[i])

print(*out)



""""
input:
    [44,0,7,9,5,-8,5,8,0,-10,7,6,40,-85,6,9]

output: 
    [-8, -10, -85, 0, 0, 44,7,9,5,5,8,7,6,40,6,9]

"""
"""
product of all digits in a number
"""
"""
input: a2b3c5
output: aabbbccccc
"""





