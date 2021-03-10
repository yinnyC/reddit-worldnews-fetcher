# Reddit r/Worldnews Top 25 News Fetching Web Bot

This program fetches the top 25 news from the subreddit - Worldnews with the API [Pushshift](https://github.com/pushshift/api)

## How to use?

- Nevigate to news_crawler
- All the methods are static method, to call any method, just do class_name.method

  ```python
  reddit_worldnews_fetcher.topnews_today()
  ```

## Methods

- top25news(start_date, end_date): fetch the the top25 news of a given date
  - Input: Time span start_date and end_date
  - Output: A list of the givendata and top25news [data,new1,new2,...]
- topnews_today(): returns the top news of today
  - Output: a string of 25 top news seperated by spaces 'news1 news2 news3 ...'
- historical_data(period1,period2): fetch the top25 news of a given time span
  - Input: time span. Format is yyyy-mm-dd.
    - If leave period2 empty, period2 will be the current date
  - Output: Will create news.csv and story all the entries there.
