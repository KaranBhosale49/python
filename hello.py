from pymongo import MongoClient
class A:
    id=0
    name=""
    salary=0
    l1=[]
    def item(self,id,name,sal):
        self.id = id
        self.name = name
        self.salary = sal
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sal(self):
        return self.salary

    def set_id(self,id):
       self.id=id

    def set_name(self,name):
       self.name=name

    def set_sal(self,sal):
        self.salary=sal

    def add(self,lst):
        self.l1.append(lst)
    def get(self):
        return self.l1

a=A()
for i in range(2):
    print('enter for index',i,)
    a.set_id(input("id :"))
    a.set_name(input("name :"))
    a.set_sal(input("sal : "))

    lst=("id:",a.get_id()+" ","name",a.get_name(),"sal",a.get_sal())
    a.add(lst)
print(a.get())
