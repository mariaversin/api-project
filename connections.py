from pymongo import MongoClient
import getpass
import json
import os
from mongo import db, coll2
#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://Maria:{}@cluster0-zs6n0.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll



connectCollection("chats",coll2)

