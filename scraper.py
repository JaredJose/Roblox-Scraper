import praw
import pandas as pd
import csv

reddit = praw.Reddit(client_id="dh55NhdB6Swr9fPZLfBkxw",      # your client id
                     client_secret="Lk2HgqcAENPI5a--643zQi5BcdCN6Q",  #your client secret
                     user_agent="my user agent") #user agent name

robloxparents = reddit.subreddit("robloxparents")
top = robloxparents.top(limit=5)

#https://praw.readthedocs.io/en/stable/code_overview/models/submission.html#praw.models.Submission

# for submission in top:
#     print("Title:\t" + submission.title)
#     print("Text:\t" + submission.selftext)
#     for comment in submission.comments:
#         print("Comment:\t" + comment.body)

headers = ['url', 'author', 'date', 'timestamp', 'text', 'subreddit', 'score', 'upvotes', 'downvotes', 'up_ratio', 'awards', 'comments']
writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore', dialect='excel')
writer.writeheader()