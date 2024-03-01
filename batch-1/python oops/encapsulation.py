class A:
    # public varible
    a = 10
    # private variable
    __b = 20
    def __privateFunc(self):
        print("private function")

    def publicFunction(self):
        print(self.__b)
        self.__privateFunc()
        print("public function")
obj = A()
# print(obj.a)
# print(obj.__b)
obj.publicFunction()
# obj.__privateFunc()