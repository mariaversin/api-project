#!/usr/bin/env python
import bottle as bottle
from bottle import route, run, get, post, request
import json
import random
import bson
from bson.json_util import dumps
import requests
from mongo import db, coll, coll2
import re
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
from functools import reduce

# # este decorador route, vincula un codigo a una URL

@post('/user/create')
def newUser():
    name = str(request.forms.get("name"))
    new_id = int(request.forms.get("idUser"))
    new_user = {
        "idUser": new_id,
        "userName": name,
    }
    coll.insert_one(new_user)
    print(f"{name} added to collection with id {new_id}")


@post("/chat/<chat_id>/addmessage")

def addMessage(chat_id):
    new_idMessage = max(coll.distinct("idMessage")) + 1
    idUser = int(request.forms.get("idUser"))
    message = str(request.forms.get("text"))
    fields = list(coll.find({"idUser":idUser},{"userName":1, "idUser":1, "_id":0,"idChat":1}))
    print(fields)
    name = fields[0]["userName"]
    for f in fields:
        if f["userName"] == name:
            new_idUser = f["idUser"]
        else:
            name = name
    new_message = {
        "idUser" : idUser,
        "userName" : name,
        "idChat" : int(chat_id),
        "idMessage" : new_idMessage,
        "text" : message
    }
    print(new_message)
    new_user = {
        "idUser" : new_idUser,
        "userName" : name
    }
    print(new_user)
    coll.insert_one(new_message)

@post('/chat/<chat_id>/adduser')

def addUserToChat(idChat):
    idUser = coll.distinct("idUser")[-1] + 1
    name = str(request.forms.get("userName"))
    idMessage = coll.distinct("idMessage")[-1] + 1
    idChat = int(idChat)
    text = str(request.forms.get("text"))
    document = {"idUser":idUser,
            "userName":name,
            "idMessage":idMessage,
            "idChat":idChat,
            "text":text}
    coll.insert_one(document)
    print("New user added to chat{}".format(idChat))
    

@get("/")
def index():
    return dumps(coll.find())


@get("/<tipo>")
def conver(tipo):
    return dumps(coll.find({'userName': tipo}))

@post('/user')
def newUser():
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_idmessage = coll.distinct("idMessage")[-1] + 1
    #new_chat = int(request.forms.get("idChat"))
    text = str(request.forms.get("text"))
    new_user = {
        "idUser": new_id,
        "userName": name,
        "idMessage": new_idmessage,
        "idChat": new_chat,
        "text": text
    }
    coll.insert_one(new_user)
    print(f"{name} added to collection with id {new_id}")

@get("/chat/<chat_id>/list")
def get_chat(chat_id):
    return dumps(coll.find({"idChat":int(chat_id)},{"_id":0}))


@get("/chat/<user>/")
def get_user(user):
    return dumps(coll.find({"userName":str(user)},{"text":0}))




run(host='localhost', port=8080, debug=True)
