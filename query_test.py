#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = 'mongodb+srv://Maria:{}@cluster0-zs6n0.mongodb.net/test?retryWrites=true&w=majority'.format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('chats','test')

query = {'idChat':0}
test_query = coll.find(query)
print(list(test_query))



