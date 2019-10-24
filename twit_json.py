# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import twint
import pandas as pd
import os
import json
import csv
import nest_asyncio
from os import listdir
import openpyxl
nest_asyncio.apply()
#Enter Twitter Handler


def user_input():
    start = input("Enter a date for Tweets since: ")
    end = input("Enter a date for Tweets until: ")
    return start, end

def set_paths():
    directory = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    fileName = 'account_list.csv'
    path = os.path.join(directory, 'data')
    acctPath = os.path.join(path, fileName)
    return directory, acctPath, path, fileName

def load_users(acctPath):
    accounts = pd.read_csv(acctPath, encoding='utf8')
    with open(acctPath, 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
        accounts = [val for sublist in l for val in sublist]
    return accounts

def get_tweets(path, start,end, i):
    c = twint.Config()
    c.Since = '2019-01-01'
    c.Until = '2019-10-31'
    c.Username = i
    c.Store_json = True
    c.Retweets = True
    c.Hide_output = True
    c.Output = os.path.join(path, i +'.json')
    twint.run.Search(c)

def search_tweets():
    for i in accounts:
        get_tweets(path, start, end ,i)
        
def get_files(path, suffix=".json" ):
    files = listdir(path)
    return [ files for files in files if files.endswith( suffix ) ]
        

def load_tweets(path):
    tweets = []
    for i in files:
        for line in open(os.path.join(path, i), 'r', encoding='utf8'):
            tweets.append(json.loads(line))
    return tweets

def parse_tweets(tweets):
    data = pd.DataFrame(tweets)
    return data

def clean_data(data):
    cols = ['mentions', 'urls', 'photos', 'cashtags', 'hashtags', 'reply_to']
    data[cols] = data[cols].astype(str).replace(r"\[|\]|\['|\']|'",
                                                '',
    regex=True)
    return data

def to_Excel(data):
    data.to_excel(os.path.join(path,'tweets_2015.xlsx'), sheet_name="raw",index=False)

start, end = user_input()
directory, acctPath, path, fileName = set_paths()
accounts = load_users(acctPath)
search_tweets()
files = get_files(path)
tweets = load_tweets(path)
data = parse_tweets(tweets)
data = clean_data(data)
to_Excel(data)





