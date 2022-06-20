from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Practice1"]
collection = db["Employee"]
n=0
while n<=4:
    print("Press 1 to add employee")
    print("Press 2 to see all employee")
    print("Press 3 find employee by name")
    print("Press 4 to remove employee")
    print("Press 5 to exit")
    n=int(input("enter your choice"))
    if n==1:
        eid =int(input("enter id for employee :"))
        name=input("enter name :")
        location=input("enter location : ")
        post=input("enter post : ")
        mylist = { "_id": eid, "name": name, "location": location, "Post":post}
        collection.insert_one(mylist)
    elif n==2:
        y=collection.find()
        for i in y:
            print(i)
    elif n==3:
        scname=input("enter name to get employee details : ")
        ite = collection.aggregate([{'$match':{'name':scname}}])
        for i in ite:
            print(i)
    elif n==4:
        de= int(input("enter id you want to remove : "))
        d=collection.delete_one({'_id':de})