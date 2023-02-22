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
# with open('robloxParentsComments.csv', 'a') as f:
#     headers = ['url', 'author', 'date', 'timestamp', 'score', 'upvotes', 'downvotes', 'golds', 'comment', 'comment_id']
#     writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore', dialect='excel')
#     writer.writeheader()
#     url_list, author_list, date_list, timestamp_list, score_list, comment_list, comment_id_list

#     for post in top:
#         comments = list(post.comments)
#         for comment in comments:
#             url_list.append(post.url)
#             author_list.append(comment.author.name)
#             date_list.append(datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'))
#             timestamp_list.append(comment.created_utc)
#             score_list.append(comment.score)
#             comment_list.append(comment.body)
#             comment_id_list.append(comment.id)

            #data = {'url: {}, author: {}, date: {}, timestamp: {}, score: {}, comment: {}, comment_id: {}'.format(post.url, comment.author.name, datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'), comment.created_utc, comment.score, comment.body, comment.id)}
            #writer.writerow(data)    for post in top:
url_list = [] 
author_list = []
date_list = []
timestamp_list = []
score_list = []
comment_list = []
comment_id_list = []
parent_id_list = []
for post in top:
    comments = post.comments.list()
    #comments = list(post.comments)
    for comment in comments:
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
df.to_csv('robloxParentsComments.csv', index=False)