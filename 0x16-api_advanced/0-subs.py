#!/usr/bin/python3
""" makes query to reddit"""

from requests import get


def number_of_subscribers(subreddit):
    """ gets the number of subscribers"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {'User-Agent': 'Dennis'}
    r = get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    return 0
