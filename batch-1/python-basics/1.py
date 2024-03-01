#single line comment

"""
multi line
comment
"""
'''
s = "simhadri"

#l = list(s)

print(s[::-1])
print(len(s))
'''
#dictionary..
#item ---> (key:value) pair
d = {}
print(type(d))
d = {"blue":20, "red":30,"green":30, "blue":50}
"""
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d['blue'])
"""
for item in d.items():
    print(item)
    print("key:",item[0],"; value:", item[1])
    print(f"key: {item[0]} ; value: {item[1]}")




































