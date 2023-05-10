#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0

if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers != 0:
        print(f"Number of subscribers in {subreddit}: {subscribers}")
    else:
        print(f"Subreddit {subreddit} not found or API error.")
