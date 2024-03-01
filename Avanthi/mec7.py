
"""
#and
print("values for and")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()
#and
print("values for and")
print(1 and 1)
print(1 and 0)
print(0 and 1)
print(0 and 0)


print()
#or
print("values for or")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print()
#or
print("values for or")
print(1 or 1)
print(1 or 0)
print(0 or 1)
print(0 or 0)


print()
#xor
print("values for XOR")
print(1 ^ 1)
print(1 ^ 0)
print(0 ^ 1)
print(0 ^ 0)
"""
"""
n = int(input("enter a number"))

c = 0
p = 1
for i in range(1,n+1): # 0 to n
    c+=i
    p*=i
print(c)
print(p)
"""

"""
break
continue
pass
"""


for i in range(50):
    if i%4==0:
        #continue
        pass
    if i==30:
        break

    print(i)
    















