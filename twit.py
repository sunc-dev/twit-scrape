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
nest_asyncio.apply()
#Enter Twitter Handler


def user_input():
    handler = input("Enter a twitter handler: ")
    start = input("Enter a date for Tweets since: ")
    end = input("Enter a date for Tweets until: ")
    return handler, start, end


def set_paths():
    directory = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    fileName = 'account_list.csv'
    path = os.path.join(directory, 'data')
    acctPath = os.path.join(path, fileName)
    return directory, acctPath, path, fileName


def load_users(acctPath):
    accounts = pd.read_csv(acctPath)

    with open(acctPath, 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
        accounts = [val for sublist in l for val in sublist]
    return accounts


def get_tweets(path, i):
    c = twint.Config()
    c.Username = i
    c.Store_json = True
    c.Retweets = True
    c.Hide_output = True
    c.Output = path
    twint.run.Search(c)


def search_tweets():
    for i in accounts:
        get_tweets(path, i)


def load_tweets(path):
    tweets = []
    for line in open(os.path.join(path, 'tweets.json'), 'r', encoding='utf8'):
        tweets.append(json.loads(line))
    return tweets


def parse_tweets(tweets):
    data = pd.DataFrame(tweets)
    return data


def clean_data(data):
    cols = ['mentions', 'urls', 'photos', 'cashtags', 'hashtags']
    data[cols] = data[cols].astype(str).replace(r"\[|\]|\['|\']|'",
                                                '',
                                                regex=True)
    return data


directory, acctPath, path, fileName = set_paths()
accounts = load_users(acctPath)
search_tweets()
tweets = load_tweets(path)
data = parse_tweets(tweets)
data = clean_data(data)
