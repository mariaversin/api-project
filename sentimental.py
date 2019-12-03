#!/usr/bin/env python
import requests
import json
from mongo import db, coll
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
import requests
from mongo import db, coll
import bottle as bottle
from bottle import route, run, get, post, request
import json

@get("/chat/<chat_id>/sentiment")
def get_sentiment(chat_id):
    chat = get_chat(chat_id)
    return chat
    





run(host='localhost', port=8080, debug=True)