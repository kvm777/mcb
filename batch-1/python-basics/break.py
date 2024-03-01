# break --- it terminates the loop...
# continue -- it terminates the iteration...
# pass -- empty

def fun(a):
    pass

# n = int(input())
# for i in range(n):
#     if i%3==0 or i%5==0:
#         pass
#     else:
#         print(i)


n = int(input())

for i in range(1,n): #1-20
    print("start",i)
    if i==5:
        break
    print("done",i)
