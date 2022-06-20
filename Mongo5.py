from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["karan"]
Collection = db["Student"]

cursor = Collection.find({"name": "Karan"})

print("finding with name")
for record in cursor:
    print(record)


