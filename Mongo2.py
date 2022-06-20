
from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["karan"]
collection = db["Student"]
mylist = [
{ "_id": 1, "name": "Karan", "Roll No": "101", "Branch":"E&tc"},
{ "_id": 2, "name": "Pranav", "Roll No": "102", "Branch":"It"},
{ "_id": 3, "name": "Ashish", "Roll No": "103", "Branch":"Cs"},
{ "_id": 4, "name": "Rushab", "Roll No": "1004", "Branch":"Me"},
]

collection.insert_many(mylist)
