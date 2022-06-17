from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def greet(self):
        pass
class B(A):
    def hello(self):
        print("hello")

    def greet(self):
            print('world')

a=A()
b=B()
b.greet()
b.hello()