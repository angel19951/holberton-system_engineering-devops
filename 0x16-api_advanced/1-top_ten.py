#!/usr/bin/python3
"""
Function to query a Reddit API and returns the number of subcribers.
If an invalid subreddit is given the function will return 0.
"""
import sys
import requests


def top_ten(subreddit):
    subscribers = requests.get('https://www.reddit.com/r/{}.json?sort=hot&limit=10'
                              .format(subreddit),
                              headers={'User-Agent': "My-User-Agent"},
                              allow_redirects=False)
    if subscribers.status_code >= 300:
        print('None')
    else:
        [print(child.get('data').get('title'))
         for child in subscribers.json().get('data').get('children')]
