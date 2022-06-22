import pymongo

client= pymongo.MongoClient('localhost',27017)
db=client['checking']
col=db['check']
yy={"_id":1}
val=[{"$set":{"name":"pranav"}},{"$set":{"location":"mumbai"}}]
f=col.update_one(yy,val)
f= col.find_one()
print(f)