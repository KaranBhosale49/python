from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["karan"]
Collection = db["Student"]

cursor = Collection.find({"_id": {"$gt":2 }})

print("The data having id greater than or equal 2:")
for record in cursor:
    print(record)

cursor = Collection.find({"_id": {"$lte": 2}})

print("\nThe data having id less than 2")
for record in cursor:
    print(record)
