import requests
import os

RAPIDSOS_KEY= ""


def covid_stats(country = ''):
    params= {'country': country}
    headers = {'x-rapidapi-region': 'AWS - us-east-1', 'X-RapidAPI-Host': 'covid-19-coronavirus-statistics.p.rapidapi.com',  'X-RapidAPI-Key': RAPIDSOS_KEY}
    res = requests.request('GET', 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total', params=params, headers=headers)
    return res.json()['data']
