# def add(a,b=0,c=0):
#     print(a+b+c)

# add(2,3,7)
# add(20)
# add(2,5)


def sum(*args):
    output = 0
    for ele in args:
        output+=ele
    print(output)

sum(2,4,5,6,7)
sum(10,20)