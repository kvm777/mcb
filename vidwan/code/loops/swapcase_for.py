"""
swapcase...
MahEsH  -> mAHeSh
"""

s = "MahEsH"
print(f"using inbuilt method {s.swapcase()}")

s1 =""
for ele in s:
    if ele.islower():
        # print(ele.upper())
        s1 += ele.upper()
    else:
        # print(ele.lower())
        s1 += ele.lower()

"""
s1 ="" --> "m" -> "mA" --.... "mAHeSh"

"""

print(f"without using  inbuilt method {s1}")




"""
explination:
        10 -> 10/2=5 -> 5-1=4 -> 4/2=2 -> 2/2=1  
input : 10
output : 4

explination:
        15 -> 15-1=14 -> 14/2=7 -> 7-1=6 -> 6/2=3 ->3-1=2 ->2/2=1
input : 15
output : 6

"""


