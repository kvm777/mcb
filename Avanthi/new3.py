#i/p --- "jjJYTBuguY7788Iihh"

def strconvert(s):
    #write your code..
    l = ""
    u = ""
    n = ""
    sp = ""
    for i in s:
        if i.isupper():
            u+=i
        elif i.islower():
            l+=i
        elif i.isdigit():
            n+=i
        else:
            sp+=i

    return l+u+n+sp

s = input()
print(strconvert(s))


#anagram..
# boataa -- abotaa










