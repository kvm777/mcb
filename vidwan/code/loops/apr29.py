# sum of ele in array

arr = [10, 30, 15, 7, 13, 65]

print(f"sum of arr using inbuilt method {sum(arr)}")

sum_value = 0 # 10+30 -> 40+15 -> 65 .....
for ele in arr:
    sum_value += ele
print(f"sum of arr using forloop is {sum_value}")


# product of array

product_value = 1
for ele in arr:
    product_value *=ele
print(f"product of arr is {product_value}")


