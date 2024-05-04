def isArmstrong(num):
    #write your code
    s = str(num) # 153 -- "153"

    val = 0
    for i in s:
        val += int(i)**3 # "1" -- 1
    
    if val == num:
        return "armstrong"
    else:
        return "not an armstrong.."

n = int(input())
print(isArmstrong(n))

