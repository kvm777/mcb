class A:
    count = 0
    def __init__(self):
        A.count += 1
        print(self.count)
        
    @classmethod
    def fun1(cls):
        print("from fun1")
    
    @staticmethod
    def fun2():
        print("from fun2")

    def fun3(self):
        print("fun3")


    def fun4(self):
        pass


class B(A):
    def fun4(self):
        print(6776)
    

obj2 = B()
obj2.fun4()

# A.fun2()
# A.fun1()

# obj = A()
# obj.fun1()
# obj.fun2()