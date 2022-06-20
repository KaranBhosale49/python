import pymongo
mystudent = pymongo.MongoClient('localhost', 27017)
mydb = mystudent["karan"]
mycol = mydb["Student"]
x = mycol.find_one()
y = mycol.find().sort('name')
for i in y:
    print(i)

