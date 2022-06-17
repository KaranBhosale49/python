from math import pi

class Rectangle:
   def __init__(self, length, breadth):
      self.l = length
      self.b = breadth
   def peri(self):
      return 2*(self.l + self.b)
   def area(self):
      return self.l * self.b

class Circle:
   def __init__(self, radius):
      self.r = radius
   def peri(self):
      return 2 * pi * self.r
   def area(self):
      return pi * self.r ** 2

r = Rectangle(5,3)
c = Circle(4)
print("Perimter of rectangel: ",r.peri())
print("Area of rectangel: ",r.area())
print("Perimter of Circle: ",c.peri())
print("Area of Circle: ",c.area())