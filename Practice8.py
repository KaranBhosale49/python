from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Practice1"]
collection = db["test1"]
i=1
for i in range(1,5,1):
    print("index",i,)
    id =i
    name=input("enter name")
    rollNumber=input("enter rollno")
    branch=input("enter branch")
    f=open('savingdata','a')
    mylist = { "_id": id, "name": name, "Roll No": rollNumber, "Branch":branch}

    collection.insert_one(mylist)
y=collection.find()
for i in y:
    print(i)
