import praw
import pandas as pd
import csv
from datetime import datetime

reddit = praw.Reddit(client_id="dh55NhdB6Swr9fPZLfBkxw",      # your client id
                     client_secret="Lk2HgqcAENPI5a--643zQi5BcdCN6Q",  #your client secret
                     user_agent="my user agent") #user agent name

robloxparents = reddit.subreddit("robloxparents")
top = robloxparents.top(limit=1000)

url_list = [] 
author_list = []
date_list = []
timestamp_list = []
score_list = []
comment_list = []
comment_id_list = []
parent_id_list = []
for post in top:
    if post is None:
        #print("NONE TYPE NONE TYPE")
        break
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        if comment is None:
            #print("NONE TYPE NONE TYPE")
            break
        if comment.author is None:
            #print("NOPE")
            break
        #print('we balling')
        url_list.append(post.url)   
        author_list.append(comment.author.name)
        date_list.append(datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'))
        timestamp_list.append(comment.created_utc)
        score_list.append(comment.score)
        comment_list.append(comment.body)
        comment_id_list.append(comment.id)
        # if isinstance(comment.parent(), Submission):
        #           parent_id_list.append('N/A')
        # else:
        #     parent_id_list.append(comment.parent().id)
        par = comment.parent()
        if type(par) is praw.models.Submission:
            parent_id_list.append('N/A')
        else:
            parent_id_list.append(par.id)


df = pd.DataFrame({'url': url_list, 'author': author_list, 'date': date_list, 'timestamp': timestamp_list, 'score': score_list, 'comment': comment_list, 'comment_id': comment_id_list, 'parent_id': parent_id_list})
df.to_csv('data/robloxParentsComments.csv', index=False)