class Parent:
    def __init__(self):
        print("construcor")
    def func1(self):
        print("func1 from parent class")


class Child(Parent):
    def func1(self):
        print("method is overrided")

# obj1 = Parent()
# obj1.func1()
obj2 = Child()
obj2.func1()
