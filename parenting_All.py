import praw
import pandas as pd
import csv
from datetime import datetime

reddit = praw.Reddit(client_id="dh55NhdB6Swr9fPZLfBkxw",      # your client id
                     client_secret="Lk2HgqcAENPI5a--643zQi5BcdCN6Q",  #your client secret
                     user_agent="my user agent") #user agent name

type_list = []
url_list = [] 
author_list = []
title_list = []
date_list = []
timestamp_list = []
score_list = []
text_list = []
comment_id_list = []
parent_id_list = []
i = 0

for post in reddit.subreddit("parenting").search(query = "roblox", limit=None):
    print(i)
    i += 1
    if post is None:
        print("deleted post")
        continue
    
    type_list.append('Post')
    url_list.append(post.url)
    title_list.append(post.title)
    if post.author is None:
        print("deleted post author")
        author_list.append('N/A')
    else:
        author_list.append(post.author.name)
    date_list.append(datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d'))
    timestamp_list.append(post.created_utc)
    score_list.append(post.score)
    text_list.append(post.title + '\n' + post.selftext)
    comment_id_list.append('N/A')
    parent_id_list.append('N/A')
    
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        if comment is None:
            print("deleted comment")
            continue
        type_list.append('comment')
        url_list.append(post.url)
        title_list.append('N/A')  
        if comment.author is None:
            print("deleted comment author")
            author_list.append('N/A')
        else:
            author_list.append(comment.author.name)
        date_list.append(datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'))
        timestamp_list.append(comment.created_utc)
        score_list.append(comment.score)
        text_list.append(comment.body)
        comment_id_list.append(comment.id)

        par = comment.parent()
        if type(par) is praw.models.Submission:
            parent_id_list.append('N/A')
        else:
            parent_id_list.append(par.id)


df = pd.DataFrame({'type': type_list, 'url': url_list, 'title': title_list, 'author': author_list, 'date': date_list, 'timestamp': timestamp_list, 'score': score_list, 'text': text_list, 'comment_id': comment_id_list, 'parent_id': parent_id_list})
df.to_csv('data/ALLParenting.csv', index=False)