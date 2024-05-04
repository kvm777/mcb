for i in range(10):
    print(i, end=" ")
print() #next print statement move to mext line


"""
# # # #
# # # #
# # # #
# # # #

"""

for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print()

print()

for i in range(4): #i ---0 to 3
    for j in range(4): # j --- 0 to 3
        print(f"{i,j} --", end=" ")
    print()



"""
i - 0 -->  j -- 0, 1, 2, 3
i - 1 -->  j -- 0, 1, 2, 3
i - 2 -->  j -- 0, 1, 2, 3
i - 3 -->  j -- 0, 1, 2, 3
"""



for i in range(5): #i ---0 to 3
    for j in range(5): # j --- 0 to 3
        print(i+1, end=" ")
    print()

print()

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# 5 5 5 5


for i in range(5):
    for j in range(5): 
        print(j+1, end=" ")
    print()

print()


# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


for i in range(5):
    for j in range(i+1): 
        print(j+1, end=" ")
    print()

print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(5):
    for j in range(i+1): 
        print("#", end=" ")
    print()

print()

"""
    #
    # #
    # # #
    # # # #
    # # # # #
"""

c = 1
for i in range(5):
    for j in range(i+1): 
        print(c, end=" ")
        c+=1
    print()

print()


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15