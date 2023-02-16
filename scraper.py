import praw
#import pandas as pd

#https://www.reddit.com/prefs/apps
reddit = praw.Reddit(client_id="dh55NhdB6Swr9fPZLfBkxw",      # your client id
                     client_secret="Lk2HgqcAENPI5a--643zQi5BcdCN6Q",  #your client secret
                     user_agent="my user agent") #user agent name

subreddit = reddit.subreddit("robloxparents")
hot = subreddit.hot(limit=5)

for submission in hot:
    print(submission.title)