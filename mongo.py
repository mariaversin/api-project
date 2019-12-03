from pymongo import MongoClient
import getpass
import json
import os

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://Maria:{}@cluster0-zs6n0.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll


db, coll = connectCollection('chats','test')
db, coll = connectCollection('chats','users')


with open('chats.json') as f:
    chats_json = json.load(f)

if coll == 0:
    coll.insert_many(chats_json)