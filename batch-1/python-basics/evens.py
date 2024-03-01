# def iseven(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# print(even(15))
    
def evens(x, y):
    c = 0
    arr = []

    while (c<y):
        x+=1
        if x%2==0:
            arr.append(x)
            c+=1

    return arr


n = int(input())    #50
k = int(input())    #5
print(evens(n,k))