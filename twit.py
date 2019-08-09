# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import twint
import os
import nest_asyncio
nest_asyncio.apply()
#Enter Twitter Handler


def set_path():
    path = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    dl = os.path.join(path, 'data')
    return dl


def user_input():
    handler = input("Enter a twitter handler: ")
    return handler


def handlers(handler):
    handlers = []
    handlers.append(handler)
    return handlers


def get_tweets(handler, dl):
    c = twint.Config()
    c.Username = handler

    c.Store_csv = True
    c.Limit = 10
    c.Output = os.path.join(dl, handler + ".csv")
    twint.run.Profile(c)


handler = user_input()
dl = set_path()
get_tweets(handler, dl)
