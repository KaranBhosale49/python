
from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["karan"]
collection = db["testing"]

record = { "_id": 1,
		"name": "karan",
		"Roll No": "1059",
		"Branch": "E&TC"}

rec_id1 = collection.insert_one(record)
