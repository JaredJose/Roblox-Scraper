import praw
import pandas as pd
import csv
from datetime import datetime

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
#Data headers: url, author, date, timestamp, score, upvotes, downvotes, golds, comment, comment_id
with(open('robloxParentsComments.csv'), 'a') as f:
    headers = ['url', 'author', 'date', 'timestamp', 'score', 'upvotes', 'downvotes', 'golds', 'comment', 'comment_id']
    writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore', dialect='excel')
    writer.writeheader()
    for post in top:
        comments = list(post.comments)
        for comment in comments:
            data = {'url: {}, author: {}, date: {}, timestamp: {}, score: {}, comment: {}, comment_id: {}'.format(post.url, comment.author.name, datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'), comment.created_utc, comment.score, comment.body, comment.id)}
            writer.writerow(data)