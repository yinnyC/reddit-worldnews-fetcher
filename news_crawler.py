#! usr/bin/env python3
import pandas as pd
import datetime as dt
import csv
import requests
import time


def to_epoch(str_time):
    return int(dt.datetime.strptime(str_time, '%Y-%m-%d').timestamp())


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
        today_epoch = int(date.timestamp())
        nextday_epoch = today_epoch + (60*60*24)
        top_news = self.top25news(today_epoch, nextday_epoch)
        return " ".join(top_news[1:])

    @staticmethod
    def historical_data(period1, period2=str(dt.date.today())):
        """
        This function will fetch the top25 news of a given time span
        Input: time span. Format is yyyy-mm-dd. 
               If leave period2 empty, period2 will be the current date
        Output: Will create news.csv and story all the entries there.
        """
        current_time = to_epoch(period1)
        period2 = to_epoch(period2)
        with open('news.csv', mode='w') as csv_file:
            csvwriter = csv.writer(csv_file)
            while current_time < period2:
                next_day = current_time + (60*60*24)
                top25news = reddit_worldnews_fetcher.top25news(
                    current_time, next_day)
                if top25news != None:
                    csvwriter.writerow(top25news)
                time.sleep(1)  # To avoid error 429: Too Many Requests
                current_time = next_day
