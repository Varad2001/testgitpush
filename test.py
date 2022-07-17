import pymongo
"""client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
"""
client = pymongo.MongoClient("mongodb+srv://varad2001:Yadnesh2008@cluster0.kfkoz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : 'varad',
    'email' : 'varad@gmail.com',
    'age' : 20
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)

