"""
i/p - abc3fg2jk3

o/p -- abcabcabcfgfgjkjkjk

"""

def func(s):
    s = str(s)
    out = ''
    temp = ''
    for i in s:
        if i.isalpha():
            temp+=i
        elif i.isdigit():
            out+= temp*int(i)
            temp = ''
    return out

s = input()
print(func(s))

