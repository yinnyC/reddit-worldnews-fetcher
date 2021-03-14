#! usr/bin/env python3
import pandas as pd
import datetime as dt
import csv
import requests
import time

# -------------------------------#
#        Global Variables        #
# -------------------------------#

CURRENTDIR = os.path.dirname(os.path.realpath(__file__))
ONDDAY_IN_SECS = 60 * 60 * 24

# -------------------------------#
#        Helper Functions        #
# -------------------------------#
def to_epoch(str_time):
    """Take in string time(yyyy-mm-dd) and convert to epoch time."""
    return int(dt.datetime.strptime(str_time, "%Y-%m-%d").timestamp())


def get_today_epoch():
    """Return epoch time of today's date."""
    today = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())
    epoch_today_gmt = int(today.timestamp()) - ONDDAY_IN_SECS
    return epoch_today_gmt


def get_last_weekday_epoch(epochtime):
    """Return the previous workday's date in epoch time."""
    epochtime = dt.datetime.fromtimestamp(epochtime)
    offset = max(1, (epochtime.weekday() + 6) % 7 - 3)
    timedelta = dt.timedelta(offset)
    most_recent = epochtime - timedelta
    most_recent = int(most_recent.timestamp()) - ONDDAY_IN_SECS
    return most_recent

# -------------------------------#
#    reddit_worldnews_fetcher    #
# -------------------------------#

class reddit_worldnews_fetcher:
    @staticmethod
    def top25news(start_date, end_date):
        """
        This function will fetch the top25 news of a given date
        Input: Time span start_date and end_date
        Out: A list of the givendata and top25news
            [data,new1,new2,...]
        """
        url = ("https://api.pushshift.io/reddit/search/submission"
               "?subreddit=worldnews"
               "&sort_type=score"
               f"&after={start_date}"
               f"&before={end_date}"
               "&sort=desc"
               "&size=25"
               "&fields=title")
        page = requests.get(url)
        print(page)
        if page == None:
            return None
        content = page.json()['data']
        news_entry = []
        news_entry.append(dt.datetime.fromtimestamp(
            start_date).strftime("%b %d %Y"))
        for news in content:
            news_entry.append(news['title'])
        return news_entry

    @staticmethod
    def topnews_today():
        """
        This function returns the top news of today
        output:  a string of 25 top news seperated by spaces
                'news1 news2 news3 ...'
        """
        date = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())
        today_epoch = int(date.timestamp())
        nextday_epoch = today_epoch + (60*60*24)
        top_news = self.top25news(today_epoch, nextday_epoch)
        return " ".join(top_news[1:])

    @staticmethod
    def historical_data(period1, period2=str(dt.date.today()),save_path=CURRENTDIR):
        """
        This function will fetch the top25 news of a given time span
        Input: time span. Format is yyyy-mm-dd. 
               If leave period2 empty, period2 will be the current date
        Output: Will create news.csv and story all the entries there.
        """
        current_time = to_epoch(period1)
        period2 = to_epoch(period2)
        with open(os.path.join(save_path, "news.csv"), mode="w") as csv_file:
            csvwriter = csv.writer(csv_file)
            while current_time < period2:
                next_day = current_time + (60*60*24)
                top25news = reddit_worldnews_fetcher.top25news(
                    current_time, next_day)
                if top25news != None:
                    csvwriter.writerow(top25news)
                time.sleep(1)  # To avoid error 429: Too Many Requests
                current_time = next_day



reddit_worldnews_fetcher.historical_data('2021-2-20')
