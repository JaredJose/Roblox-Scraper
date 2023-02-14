import praw
import pandas as pd

reddit = praw.Reddit(client_id="",      # your client id
                     client_secret="",  #your client secret
                     user_agent="my user agent", #user agent name
                     username = "",     # your reddit username
                     password = "")     # your reddit password