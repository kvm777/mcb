"""
i/p -- "saikumar"
    aiua
    auia
o/p - "saukimar"

"""

def reverseVowels(strng):
    s = strng
    v = 'aeiouAEIOU'

    vow = []
    idx = []
    for ele in s:
        if ele in v:
            vow.append(ele)
            idx.append(s.index(ele))

    # vow = vow[::-1]
    s1 = ''
    for ele in s:
        if s.index(ele) in idx:
            s1+=vow[-1]
            vow.pop()
        else:
            s1+=ele
    return s1

s = input()
output = reverseVowels(s)
print(output)
