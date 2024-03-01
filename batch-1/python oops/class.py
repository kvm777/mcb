class Student:
    a = 10
    b = 20
    def fun1(self):
        print("from function one")
    def fun2(self):
        return "from function 2"

obj1 = Student()
print(obj1.a)
print(obj1.b)
obj1.fun1()
print(obj1.fun2())