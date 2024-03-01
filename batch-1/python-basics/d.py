d = { "10":0}

l = [ 10,20,30,5]

for i in l:
    if i%5 == 0:
        if d.get('5'):
            d['5'] +=1
        else:
            d['5'] = 0

print(d)