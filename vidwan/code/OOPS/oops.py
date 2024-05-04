"""
OOP's - object Oriented Programming
    - it is the methodology of writing/design program using classes and objects
    
    class - 
    object -


    it has four concepts on OOPs...
        - Inheritance
            - single level
            - multi level
            - multiple level
        - Polymorphism
            - method overriding
            - method overloading
        - Encapsulation
        - Abstraction


parent - child

1   +   2 =   3
"1" + "2" = "12"

"""

# class - it is the logical entity and its blue print of object
# class contains atributes and methods


# object - it's the physical entity, it creates the instance of class


# imheritance - a mechanism that allows a class to inherit properties and behaviors from another class.

# single level

class ParentClass:
    a = 10

    def fun1(self):
        return "from parentClass fun1"
    

class ChildClass(ParentClass):
    b = 20

    def fun2(self):
        return "from childclass fun2"


# obj1 = ParentClass()
# print(obj1.a)
# print(obj1.fun1())


obj2 = ChildClass()
print(obj2.b)
print(obj2.fun2())
print(obj2.a)
print(obj2.fun1())

