#!/usr/bin/python3
""" contains function top ten"""
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""
    qu = ('https://www.reddit.com/r/' + subreddit +
          '/hot.json?limit=10')
    r = get(qu, headers={'User-Agent': 'Super Meat-Boys'},
            allow_redirects=False)
    if r.status_code == 200:
        ri = r.json().get('data').get('childern')
        for rii in ri:
            print(rii.get('data').get('title'))
        return
    print(None)
