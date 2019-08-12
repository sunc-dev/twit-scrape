# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import twint
import pandas as pd
import os
import json
import nest_asyncio
nest_asyncio.apply()
#Enter Twitter Handler


def set_path():
    path = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    fName = 'tweets.json'
    fPath = os.path.join(path, 'data', fName)
    return fPath,fName


def user_input():
    handler = input("Enter a twitter handler: ")
    start = input("Enter a date for Tweets since: ")
    end = input("Enter a date for Tweets until: ")
    return handler, start, end


def handlers(handler):
    handlers = []
    handlers.append(handler)
    return handlers


def get_tweets(handler, fPath):
    c = twint.Config()
    c.Username = handler
    c.Store_json = True
    c.Retweets = True
    c.Limit = 1
    c.Hide_output=True
    c.Output = fPath
    twint.run.Search(c)

def load_tweets(fPath):
    tweets=[]
    for line in open(fPath, 'r',encoding='utf8'):
        tweets.append(json.loads(line))
    return tweets


def parse_tweets(tweets):
    data=pd.DataFrame(tweets)
    return data

handler, start, end = user_input()
fPath, fName = set_path()
get_tweets(handler, fPath)
tweets = load_tweets(fPath)
data = parse_tweets(tweets)
