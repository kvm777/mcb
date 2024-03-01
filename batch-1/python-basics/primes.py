def primes(m,n):
    arr = []
    for i in range(m,n+1):
        c = 0
        for j in range(1,i+1):
            if i%j == 0:
                c+=1
        if c==2:
            arr.append(i)

    # print(arr)
    return arr

# primes(2,50)
# primes(100,200)
# primes(300,500)

print(primes(100,200))