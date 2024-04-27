"""
Dictionary in Python

- Key-Value Pairs: Each entry in a dictionary consists of a key and its corresponding value.
- Unique Keys: Keys must be unique within a dictionary.
- Unordered: Dictionaries are unordered collections; they do not preserve the order of elements.
- Data Types: Keys and values can be of any data type.
- Definition Syntax: Dictionaries are defined using curly braces {} and key-value pairs separated by colons (:).
"""

# Example usage of dictionaries
d = {"a": 10, "b": 20, "c": 30, "a": 50, "d": 20}
print("Dictionary:", d)     # Output: {'a': 50, 'b': 20, 'c': 30, 'd': 20}

print("\nDictionary Methods:")
print("Keys:", d.keys())        # Output: Keys: dict_keys(['a', 'b', 'c', 'd'])
print("Values:", d.values())    # Output: Values: dict_values([50, 20, 30, 20])
print("Items:", d.items())      # Output: Items: dict_items([('a', 50), ('b', 20), ('c', 30), ('d', 20)])


# Accessing values using keys
print("\nAccessing Values:")
print("Value of 'a':", d['a'])   # Output: Value of 'a': 50
print("Value of 'd':", d['d'])   # Output: Value of 'd': 20

print("\n modification dict")
print(d)
d["a"] = 100
print(d)

d["e"] = 200
print(d)



"""
doubts..

slicing concept.. list, strings

list... append, insert, remove, pop, index, count, sort 
tuple.. index, count
set.. used to remove duplicates
dict.. key:value...
strings..  

"""







