# copied code from the other 4 python scripts to create one long csv

import praw
import pandas as pd
import csv
from datetime import datetime

reddit = praw.Reddit(client_id="dh55NhdB6Swr9fPZLfBkxw",      # your client id
                     client_secret="Lk2HgqcAENPI5a--643zQi5BcdCN6Q",  #your client secret
                     user_agent="my user agent") #user agent name

robloxparents = reddit.subreddit("robloxparents")
new = robloxparents.new(limit=None)

sub_list = []
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

#r/robloxparents
for post in new:
    print(i)
    i += 1
    alltext = post.title + '\n' + post.selftext
    if post is None:
        print("deleted post")
        continue
    if "korblox" in alltext.lower() or "beast mode" in alltext.lower():
        print("misc spam")
        continue
    
    sub_list.append("r/robloxparents")
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
    text_list.append(alltext)
    comment_id_list.append('N/A')
    parent_id_list.append('N/A')
    
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        if comment is None or comment.body == "[removed]" or comment.body == "[deleted]":
            print("deleted comment")
            continue
        sub_list.append("r/robloxparents")
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
            
#r/parenting
for post in reddit.subreddit("parenting").search(query = "roblox", limit=None):
    print(i)
    i += 1
    if post is None:
        print("deleted post")
        continue
    
    sub_list.append("r/parenting")
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
        if comment is None or comment.body == "[removed]" or comment.body == "[deleted]":
            print("deleted comment")
            continue
        sub_list.append("r/robloxparents")
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
            
#r/roblox
for post in reddit.subreddit("roblox").search(query = "parent OR son OR daughter OR niece OR nephew", limit=None):
    print(i)
    i += 1
    alltext = post.title + '\n' + post.selftext
    if post is None:
        print("deleted post")
        continue
    if post.author.name == "AutoModerator" or post.author.name == "BloxBot":
        print("ignore automod")
        continue
    if "script" in alltext.lower():
        print(alltext)
        continue
    
    sub_list.append("r/roblox")
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
    text_list.append(alltext)
    comment_id_list.append('N/A')
    parent_id_list.append('N/A')
    
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        if comment is None or comment.body == "[removed]" or comment.body == "[deleted]":
            print("deleted comment")
            continue
        sub_list.append("r/robloxparents")
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
            
#r/roblox - weekly questions
sub = reddit.subreddit("roblox")
query = sub.search(query="weekly question thread", limit=None)
for post in query:
    print(i)
    i += 1
    if post is None:
        #print("NONE TYPE NONE TYPE")
        break
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        if comment is None:
            #print("NONE TYPE NONE TYPE")
            continue
        if comment.author == "AutoModerator":
            print("ignore automod")
            continue
        if comment is None or comment.body == "[removed]" or comment.body == "[deleted]":
            print("deleted comment")
            continue
        if "script" in comment.body.lower():
            continue
        s = comment.body.lower().split()
        for word in s:
            if word.startswith("parent") or word == "son" or "daughter" in word or "nephew" in word or word == "niece":
                sub_list.append("Weekly Questions thread on r/roblox")
                type_list.append('comment')
                url_list.append(post.url)
                title_list.append('N/A')
                #postdate_list.append(datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d'))
                #post_id_list.append(post.id)

                if comment.author is None:
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
                break

df = pd.DataFrame({'subreddit': sub_list, 'type': type_list, 'url': url_list, 'title': title_list, 'author': author_list, 'date': date_list, 'timestamp': timestamp_list, 'score': score_list, 'text': text_list, 'comment_id': comment_id_list, 'parent_id': parent_id_list})
df.to_csv('data/cumulative.csv', index=False)