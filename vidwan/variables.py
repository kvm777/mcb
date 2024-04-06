>>> x = 2
>>> x + 3  # Adding 3 to x
5

>>> y = 10
>>> x + y  # Adding x and y
12

>>> x = 15  # Assigning a new value to x
>>> x + y  # Adding the new value of x and y
25

>>> x = x + 10  # Adding 10 to x and reassigning it to x
>>> x + y  # Adding the updated value of x and y
35

>>> name  # Trying to access a variable 'name' which isn't defined yet
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    name
NameError: name 'name' is not defined

>>> name = "mahesh"  # Defining a new variable 'name' with the value "mahesh"
>>> name  # Displaying the value of 'name'
'mahesh'

>>> name + "korada"  # Concatenating 'name' with "korada"
'maheshkorada'

>>> name, "korada"  # Displaying both 'name' and "korada"
('mahesh', 'korada')

>>> print(name, "korada")  # Printing 'name' and "korada"
mahesh korada

>>> a = 10  # Defining a new variable 'a' with the value 10
>>> "a"  # Displaying the string "a"
'a'

>>> print("a", a)  # Printing the string "a" followed by the value of 'a'
a 10
