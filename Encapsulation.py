class Base:
	def __init__(self):
		self._a = 2

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("protected member of base class: ",self._a)
		self._a = 3
		print(" protected member outside class: ",self._a)

a= Derived()

b= Base()

print("Accessing protected member of obj1: ", a._a)
print("Accessing protected member of obj2: ", b._a)
