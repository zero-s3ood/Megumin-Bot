import requests
import os
import feedparser

RAPIDSOS_KEY= os.getenv('RAPIDSOS_API_KEY')

newsfeed = {"The Guardian": "https://www.theguardian.com/rss",
            "New York Times":  "https://rss.nytimes.com/services/xml/rss/nyt/World.xml" }

def covid_stats(country = ''):
    params= {'country': country}
    headers = {'x-rapidapi-region': 'AWS - us-east-1', 'X-RapidAPI-Host': 'covid-19-coronavirus-statistics.p.rapidapi.com',  'X-RapidAPI-Key': RAPIDSOS_KEY}
    res = requests.request('GET', 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total', params=params, headers=headers)
    return res.json()['data']

def news_feed(feed = "The Guardian", limit = 5):
    news = feedparser.parse(newsfeed[feed])
    return news.entries[:limit]