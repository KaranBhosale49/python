
from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["karan"]
collection = db["Student"]
mylist = [
{ "_id": 5, "name": "Karan", "Roll No": "105", "Branch":"E&tc"},
{ "_id": 6, "name": "Suraj", "Roll No": "106", "Branch":"CS"},
]

collection.insert_many(mylist)
