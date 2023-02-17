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

#https://stackoverflow.com/questions/58977105/how-to-write-multiple-lines-of-reddit-data-using-praw-to-csv-txt-file
with open('postFetch.csv','a', newline='') as f:
    headers = ['url', 'title', 'author', 'timestamp', 'text', 'subreddit', 'comments', 'score', 'up_ratio']
    writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore', dialect='excel')
    writer.writeheader()
    for post in top:
        data = {'url' : post.url,
                'title' : post.title,
                'author' : post.author,
                'timestamp' : post.created_utc,
                'text' : post.selftext,
                'subreddit' : post.subreddit.name,
                'comments' : post.num_comments,
                'score' : post.score,
                'up_ratio' : post.upvote_ratio
                }
    writer.writerow(data)