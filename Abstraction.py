from abc import ABC, abstractmethod
class Car(ABC):
    def milage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 40km Tesla")
class Honda(Car):
    def mileage(self):
        print("The mileage is 25km Honda")
class Toyota(Car):
     def mileage(self):
          print("The mileage is 20km Toyota")

class Ford(Car):
    def mileage(self):
            print("The mileage is 25km Ford ")

t= Tesla ()
t.mileage()
h = Honda()
h.mileage()
to = Toyota()
to.mileage()
f = Ford()
f.mileage()