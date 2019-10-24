# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:39:23 2019

@author: csunj
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

#define tags

tags = ['#canadadebates2019']

#set paths


def set_paths():
    directory = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    path = os.path.join(directory, 'data\hashtag')
    return directory, path


def get_tweets(path, i):
    c = twint.Config()
    c.Since = '2018-12-31'
    c.Until = '2019-10-31'
    c.Search = i
    c.Store_json = True
    c.Retweets = True
    c.Hide_output = True
    c.Output = os.path.join(path, i + '.json')
    twint.run.Search(c)


def search_tweets():
    for i in tags:
        get_tweets(path, i)


def get_files(path, suffix=".json"):
    files = listdir(path)
    return [files for files in files if files.endswith(suffix)]


def load_tweets(path):
    tweets = []
    for i in files:
        for line in open(os.path.join(path, i), 'r', encoding='utf8'):
            tweets.append(json.loads(line))
    return tweets


def parse_tweets(tweets):
    data = pd.DataFrame(tweets)
    return data


def to_Excel(data):
    data.to_excel(os.path.join(path, 'tweets_hash_2019.xlsx'),
                  sheet_name="raw",
                  index=False)


directory, path = set_paths()
search_tweets()
files = get_files(path)
tweets = load_tweets(path)
data = parse_tweets(tweets)
to_Excel(data)
