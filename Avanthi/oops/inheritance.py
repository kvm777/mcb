
#Inheritance...

class A:
    a = 10
    def __init__(self):
        print("constructor is called")
    def fun1(self):
        print(20,"from fun1 in class A")

class B():
    b = 30
    def fun2(self):
        print(40, "from fun2 in classB")
        print(self.a,"from A clas")

class C(A,B):
    c = 50
    def fun3(self):
        print(60,"from fun3 in class C")
        print(self.a+self.b)
    def fun4(self):
        return self.fun1()

    
obj = C()

print(obj.a)
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
