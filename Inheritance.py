class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Karan", "Bhosale")
x.printname()