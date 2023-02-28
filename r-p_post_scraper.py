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


#Using dataframes:
url_list = []
title_list = []
author_list = []
date_list = []
timestamp_list = []
text_list = []
sub_list = []
comment_list = []
score_list = []
up_ratio_list = []

for post in top:
    url_list.append(post.url)
    title_list.append(post.title)
    author_list.append(post.author)
    date_list.append(datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d'))
    timestamp_list.append(post.created_utc)
    text_list.append(post.selftext)
    sub_list.append(post.subreddit.name)
    comment_list.append(post.num_comments)
    score_list.append(post.score)
    up_ratio_list.append(post.upvote_ratio)

df = pd.DataFrame({'url': url_list, 'title': title_list, 'author': author_list, 'date': date_list, 'timestamp': timestamp_list, 'text': text_list, 'subreddit': sub_list, 'score': score_list, 'upvote ratio': up_ratio_list})
df.to_csv('data/robloxParentsPosts.csv', index=False)