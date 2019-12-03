#!/usr/bin/env python
import bottle as bottle
from bottle import route, run, get, post, request
import json
import random
import bson
from bson.json_util import dumps
import requests
from mongo import db, coll
import re
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
from functools import reduce


@get('/chat/<chat_id>/sentiment')
def getSentiment(chat_id):
    query = list(coll.find({'idChat':int(chat_id)}, {"userName":1,"idUser":1,"text": 1,"_id":0}))
    sid = SentimentIntensityAnalyzer()
    total_info=[]
    for text in query:
        info={}
        info["userName"]=text["userName"]
        info["idChat"]=int(chat_id)
        info["text"]=text["text"]
        info["sentiment"]=sid.polarity_scores(text["text"])
        total_info.append(info)
    print(total_info)
    return dumps(total_info)
    """comp_sent = [s['sentiment']['compound'] for s in total_info]
    avg = reduce((lambda x, y: x+y), comp_sent)/len(comp_sent)
    return dumps({"Sentiments": total_info,

                  "compound sentiments": comp_sent,

                  "avg sentiment values:[-1, 1]": avg})"""



run(host='localhost', port=8080, debug=True)