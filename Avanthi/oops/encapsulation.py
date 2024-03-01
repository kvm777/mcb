
#encapsulation...

"""
access modifiers...
private

    vatiables... __var
    methods... __method()
   -->>scope... within class
public
    vatiables... var
    methods... method()
   -->>scope... within class and outside of the class
"""


class A:
    a = 10
    __b = 20

    def fun(self):
        print("public function")
        print(self.__b,"private variable")
    def __fun1(self):
        print("private function")
    def fun2(self):
        return self.__fun1()
    

obj = A()

obj.fun2()


