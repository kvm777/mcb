"""
prime nums..
    it has factors of 1 and itself...(2 factors)
    2 3 5 7 11 13 17 19

    
"""
# check wether the num is prime or not

num = 0

if num == 0 or num == 1:
    print("not prime")
elif num == 2:
    print("prime")
else:
    for i in range(2, num):
        if num%i == 0:
            print("not prime")
            break
    else:
        print("prime")

