import os
import dotenv
import praw

dotenv.load_dotenv()

# Another approach using the praw library


def reddit_worldnews_fetcher():
    """ This function will crawl top 25 news of the day from the subreddit worldnews"""
    reddit = praw.Reddit(client_id=os.getenv("client_id"),
                         client_secret=os.getenv("client_secret"),
                         user_agent=os.getenv("user_agent"),
                         username=os.getenv("username"),
                         password=os.getenv("password"))
    subreddit = reddit.subreddit('worldnews')
    top_subreddit = subreddit.top(time_filter='day', limit=25)
    cols = []
    for submission in top_subreddit:
        title = submission.title
        cols.append(title)
    return " ".join(cols)
