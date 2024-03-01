class A:
    a = 10
    _b = 20
    __c = 30

    def fun1(self):
        print("fun1")


obj = A()
print(obj.a)
# obj._b = 30
print(obj._b)
print(obj.__c)