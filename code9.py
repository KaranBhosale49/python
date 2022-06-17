class A:
    def __init__(self):
        self._course='java'
        self.__des='java description'
    def get_course(self):
        return self.__course
a=A()
print(a._A__course)