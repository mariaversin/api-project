from pymongo import MongoClient
import getpass
import json
import os
from dotenv import load_dotenv
load_dotenv()

#Get Password
connect = os.getenv('connection')
#Connect to DB
client = MongoClient(connect)
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