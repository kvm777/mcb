from abc import *


class abstract:
    @abstractmethod
    def abs(self):
        None

class concrete(abstract):
    def abs(self):
        print("something...")

obj = concrete()
obj.abs()
