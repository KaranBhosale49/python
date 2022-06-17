class A:
    aa=0
    b=''
    @classmethod
    def set(cls,age,name):
        cls.aa=age
        cls.b=name

    @classmethod
    def get(cls):
      return cls.aa,cls.b

a=A()
a.set(age=25,name='karan')
print(a.get())