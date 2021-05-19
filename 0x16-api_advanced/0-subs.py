#!/usr/bin/python3
"""
Function to query a Reddit API and returns the number of subcribers.
If an invalid subreddit is given the function will return 0.
"""
import sys
import requests


def number_of_subscribers(subreddit):
    try:
        subscribers = requests.get('https://www.reddit.com/r/{}/about.json'
                                   .format(subreddit),
                                   headers={'User-Agent': "My-User-Agent"},
                                   allow_redirects=False)
        if subscribers.status_code >= 300:
            return 0

        return subscribers.json().get('data').get('subscribers')
    except:
        return 0
