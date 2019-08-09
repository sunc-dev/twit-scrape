import twint
import os
#Enter Twitter Handler


def set_path():
    path = r"C:\Users\csunj\OneDrive\Documents\Github\Repository\twit-scrape"
    dl = os.path.join(path, 'data')
    return dl


def user_input():
    handler = input("Enter a twitter handler: ")
    start = input("Enter a date to start the search: ")
    end = input("Enter a date to end the search: ")
    return handler, start, end


def handlers(handler):
    handlers = []
    handlers.append(handler)
    return handlers


def get_tweets(handler, dl):
    c = twint.Config()
    c.Username = handler
    c.Custom = [
        'id', 'date', 'time', 'timezone', 'user_id', 'username', 'tweet',
        'replies', 'retweets', 'likes', 'hashtags', 'link', 'retweet',
        'user_rt', 'mentions'
    ]

    c.Store_csv = True
    c.Output = handler + ".csv"
    twint.run.Profile(c)


handler, start, end = user_input()
dl = set_path()
get_tweets(handler, dl)
