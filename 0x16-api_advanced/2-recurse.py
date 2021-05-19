#!/usr/bin/python3
"""
Recursive function to query a Reddit API parse through the hot articles, and
print a sorted count of given keywords
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    try:
        titles = requests.get('https://www.reddit.com/r/{}/hot.json'
                              .format(subreddit),
                              params={'count': count, 'after': after},
                              headers={'User-Agent': 'My-User-Agent'},
                              allow_redirects=False)
        if titles.status_code >= 400:
            return None

        new_hot_list = hot_list + [child.get('data').get('title')
                                   for child in titles.json().get('data')
                                   .get('children')]
        info = titles.json()

        if not info.get('data').get('after'):
            return new_hot_list

        return recurse(subreddit, new_hot_list, info.get('data').get('count'),
                       info.get('data').get('after'))

    except:
        return None
